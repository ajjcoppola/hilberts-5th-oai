#!/usr/bin/env python3
"""Build docs/BLOG_HILBERT_SMITH_DEV_STORY.pdf from the public essay.

AI-assisted / AI-generated with Cursor (Grok, Anthropic, and OpenAI models).
Direction: Alan J. Coppola.
"""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
SRC = DOCS / "BLOG_HILBERT_SMITH_DEV_STORY.md"
OUT = DOCS / "BLOG_HILBERT_SMITH_DEV_STORY.pdf"
BUILD = ROOT / "build" / "blog_pdf"

HEADER = r"""---
title: "Hilbert's 5th and the Hilbert--Smith Conjecture: Solved?"
author:
  - Alan J. Coppola
  - Ajjax (joint author and AI assistant; Cursor with Grok, Anthropic, Google, and OpenAI tools)
date: "22 October 2026"
geometry: margin=1in
fontsize: 11pt
linestretch: 1.15
header-includes:
  - \usepackage{amsmath,amssymb}
  - \usepackage{microtype}
  - \usepackage{graphicx}
  - \usepackage{float}
  - \floatplacement{figure}{H}
  - \usepackage{xurl}
  - \usepackage{hyperref}
  - \hypersetup{colorlinks=true,linkcolor=black,urlcolor=blue}
  - \setkeys{Gin}{width=0.98\linewidth,keepaspectratio}
  - \urlstyle{same}
---

A development story: learning, verification, and questions. Not a proof.

"""


def find_tectonic() -> str:
    for cand in (
        shutil.which("tectonic"),
        str(Path.home() / "miniconda3/envs/sr/bin/tectonic"),
        "/Users/ajjc/miniconda3/envs/sr/bin/tectonic",
    ):
        if cand and Path(cand).is_file():
            return cand
    raise SystemExit("tectonic not found")


def find_pandoc() -> str:
    pandoc = shutil.which("pandoc") or "/opt/homebrew/bin/pandoc"
    if not Path(pandoc).is_file():
        raise SystemExit("pandoc not found")
    return pandoc


def body_from_essay(text: str) -> str:
    """Drop the markdown title/byline; pandoc YAML supplies those."""
    lines = text.splitlines()
    i = 0
    if lines and lines[0].startswith("# "):
        i = 1
    while i < len(lines) and lines[i].strip() == "":
        i += 1
    # Skip Date / Authors block through the first ---
    if i < len(lines) and lines[i].startswith("Date:"):
        while i < len(lines) and lines[i].strip() != "---":
            i += 1
        if i < len(lines) and lines[i].strip() == "---":
            i += 1
    body = "\n".join(lines[i:]).strip() + "\n"
    # Italic captions immediately after images become figure captions.
    body = body.replace(
        "![The 2-adic solenoid nested in a solid torus](figures/padic_solenoid.png)\n\n"
        "*p = 2 in the picture; a general prime winds p times. The solenoid is the infinite nested intersection. A meridional slice meets each stage in p disks, and the fiber is a Cantor set.*",
        "![p = 2 in the picture; a general prime winds p times. The solenoid is the infinite nested intersection. A meridional slice meets each stage in p disks, and the fiber is a Cantor set.](figures/padic_solenoid.png)",
    )
    body = body.replace(
        "![The p-adic solenoid as an inverse limit of ×p maps on circles](figures/padic_solenoid_inverse_limit.png)\n\n"
        "*Each bonding map is multiplication by p on the circle. Compatible rotations assemble to a free action of the p-adic integers. The orbit space is a circle. The solenoid is compact and connected. It is not a manifold.*",
        "![Each bonding map is multiplication by p on the circle. Compatible rotations assemble to a free action of the p-adic integers. The orbit space is a circle. The solenoid is compact and connected. It is not a manifold.](figures/padic_solenoid_inverse_limit.png)",
    )
    return body


def main() -> None:
    if not SRC.is_file():
        raise SystemExit(f"missing {SRC}")
    BUILD.mkdir(parents=True, exist_ok=True)
    md_path = BUILD / "blog.md"
    md_path.write_text(HEADER + body_from_essay(SRC.read_text(encoding="utf-8")), encoding="utf-8")

    pandoc = find_pandoc()
    tectonic = find_tectonic()
    pdf_tmp = BUILD / "blog.pdf"
    cmd = [
        pandoc,
        str(md_path),
        "-f",
        "markdown+smart+yaml_metadata_block+raw_tex",
        "-t",
        "pdf",
        f"--pdf-engine={tectonic}",
        "--resource-path",
        str(DOCS),
        "-V",
        "documentclass=article",
        "-o",
        str(pdf_tmp),
    ]
    print("Running:", " ".join(cmd))
    proc = subprocess.run(cmd, cwd=DOCS, capture_output=True, text=True)
    if proc.returncode != 0:
        print(proc.stdout)
        print(proc.stderr)
        raise SystemExit(f"pandoc/tectonic failed with code {proc.returncode}")
    shutil.copy2(pdf_tmp, OUT)
    print(f"Wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
