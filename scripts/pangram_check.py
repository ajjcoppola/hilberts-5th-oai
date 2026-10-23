#!/usr/bin/env python3
"""Submit text to Pangram (pangram.com) and print the AI-detection summary."""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request

BASE = "https://text.external-api.pangram.com"


def req(method: str, url: str, key: str, body: dict | None = None) -> dict:
    data = None if body is None else json.dumps(body).encode("utf-8")
    headers = {"x-api-key": key}
    if data is not None:
        headers["Content-Type"] = "application/json"
    r = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(r, timeout=60) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        err = e.read().decode("utf-8", errors="replace")
        raise SystemExit(f"Pangram HTTP {e.code}: {err}") from e


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--text-file", help="UTF-8 file to check")
    p.add_argument("--text", help="Literal text to check")
    p.add_argument("--model", default="", help="Override model selector")
    args = p.parse_args()
    key = os.environ.get("PANGRAM_API_KEY", "").strip()
    if not key:
        raise SystemExit(
            "PANGRAM_API_KEY is not set. Create a key at "
            "https://www.pangram.com/apikey and export it, or paste the sample "
            "into the Pangram dashboard."
        )
    if args.text_file:
        text = open(args.text_file, encoding="utf-8").read()
    elif args.text:
        text = args.text
    else:
        text = sys.stdin.read()
    text = text.strip()
    if len(text) < 40:
        raise SystemExit("Need at least ~40 characters of prose.")

    models = req("GET", f"{BASE}/models", key).get("models") or ["default"]
    model = args.model or ("pangram-4" if "pangram-4" in models else models[0])
    task = req(
        "POST",
        f"{BASE}/task",
        key,
        {"text": text, "model": model, "public_dashboard_link": False},
    )
    task_id = task.get("task_id")
    if not task_id:
        raise SystemExit(f"No task_id in {task}")
    for _ in range(40):
        result = req("GET", f"{BASE}/task/{task_id}", key)
        stage = result.get("stage", "")
        if stage == "STAGE_SUCCESS":
            print(
                json.dumps(
                    {
                        "headline": result.get("headline"),
                        "prediction_short": result.get("prediction_short"),
                        "fraction_ai": result.get("fraction_ai"),
                        "fraction_ai_assisted": result.get("fraction_ai_assisted"),
                        "fraction_human": result.get("fraction_human"),
                        "model": model,
                    },
                    indent=2,
                )
            )
            return
        if stage == "STAGE_FAILED":
            raise SystemExit(f"Pangram task failed: {result}")
        time.sleep(1.5)
    raise SystemExit("Timed out waiting for Pangram.")


if __name__ == "__main__":
    main()
