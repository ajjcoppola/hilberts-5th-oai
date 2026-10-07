#!/usr/bin/env python3
"""Build Hilbert_Smith_Audit.pdf with TeX math and rendered Mermaid diagrams."""

from __future__ import annotations

import json
import re
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUT = DOCS / "Hilbert_Smith_Audit.pdf"
BUILD = ROOT / "build" / "audit_pdf"
FIGS = BUILD / "figures"

SOURCES = [
    ("README", ROOT / "README.md"),
    ("Proof overview (Q1, Q2, Q4, Q6)", DOCS / "01_proof_overview.md"),
    ("Audit ledger (Targets A--C)", DOCS / "02_audit_ledger.md"),
    ("Sponge stress test (Q5)", DOCS / "03_sponge_stress_test.md"),
    ("Public responses (Q3)", DOCS / "04_public_responses.md"),
    ("Lemma dependency ledger", DOCS / "lemma_dependency_ledger.md"),
    ("Sherlock session log", DOCS / "SHERLOCK_HILBERT_SMITH_2026-10-07.md"),
]

UNICODE_MATH = {
    "ℤ": r"\mathbb{Z}",
    "ℚ": r"\mathbb{Q}",
    "ℝ": r"\mathbb{R}",
    "μ": r"\mu",
    "Σ": r"\Sigma",
    "α": r"\alpha",
    "β": r"\beta",
    "π": r"\pi",
    "⊗": r"\otimes",
    "⊆": r"\subseteq",
    "⊂": r"\subset",
    "∈": r"\in",
    "∉": r"\notin",
    "≃": r"\simeq",
    "≡": r"\equiv",
    "≥": r"\ge",
    "≤": r"\le",
    "×": r"\times",
    "·": r"\cdot",
    "→": r"\to",
    "⇒": r"\Rightarrow",
    "≈": r"\approx",
    "⁻¹": r"^{-1}",
    "ū": r"\bar{u}",
    "°": r"^\circ",
}

HEADER = r"""---
title: "Hilbert--Smith Conjecture"
subtitle: "Sherlock Reverse-Verification Audit"
author: "Cursor(Opus 5.5/Grok), driven by: Alan Coppola"
date: "2026-10-07"
geometry: margin=1in
fontsize: 11pt
header-includes:
  - \usepackage{amsmath,amssymb,mathtools}
  - \usepackage{microtype}
  - \usepackage{booktabs}
  - \usepackage{longtable}
  - \usepackage{array}
  - \usepackage{graphicx}
  - \usepackage{float}
  - \usepackage{hyperref}
  - \hypersetup{colorlinks=true,linkcolor=black,urlcolor=blue}
  - \providecommand{\Zp}{\mathbb{Z}_p}
  - \providecommand{\R}{\mathbb{R}}
  - \providecommand{\Q}{\mathbb{Q}}
  - \providecommand{\Z}{\mathbb{Z}}
  - \graphicspath{{figures/}}
---

\begin{center}
{\small\textit{Audit of OpenAI Math Release preprint
\texttt{The Hilbert--Smith conjecture in every finite dimension}}\\
Upstream: \texttt{github.com/openai/math} \quad SHA: \texttt{adc7f12\ldots}}
\end{center}
\vspace{-0.4em}

\section*{Original questions}
\begin{enumerate}
\setlength{\itemsep}{0.15em}
\setlength{\parsep}{0pt}
\item
  Overview: how faithful $p$-adic actions are excluded near the identity
  homeomorphism.
\item
  Geometric argument, or algebraic invariants in every Euclidean
  neighborhood?
\item
  Public / internet responses to this AI-generated proof?
\item
  Categorize the proof; what does it say about the structure of
  $\mathbb{R}^n$?
\item
  Hold/break under Menger-type sponges as $\mathbb{R}^n$ replacements
  (where the theorem is false)?
\item
  Is the contradiction that $\mathbb{R}^n$ cannot factor through an orbit
  space with ``wonky'' local sphere maps?
\end{enumerate}
\vspace{-0.2em}

\section*{TL;DR}
\noindent
OpenAI's preprint claims a proof of the Hilbert--Smith conjecture in every
finite dimension by ruling out faithful continuous actions of the $p$-adic
integers on topological manifolds. The argument is not the classical Yang
orbit-dimension obstruction. Instead it is an integrality-versus-divisibility
contradiction for a sheaf-theoretic Witt/signature invariant: a small open
subgroup $G\cong\mathbb{Z}_p$ acts on a Euclidean chart, the action is
stabilized into an odd-dimensional sphere $S^d$, and averaging near the
identity produces a degree-one test through the orbit space. Character
symmetry then forces that orientation class to split into arbitrarily fine
equal rational pieces, which cannot fit inside a fixed denominator lattice
on $E_d(S^d)$. A targeted audit found no outright failure in the load-bearing
lemmas, though several steps remain weak pending expert or Lean review; on
Menger-type sponges, where faithful $\mathbb{Z}_p$ actions do exist, the
proof correctly refuses to run because Newman and Euclidean-chart hypotheses
fail.

\tableofcontents
\newpage

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


def find_mmdc() -> str:
    local = ROOT / "node_modules" / ".bin" / "mmdc"
    if local.is_file():
        return str(local)
    which = shutil.which("mmdc")
    if which:
        return which
    raise SystemExit(
        "mmdc not found; run: npm install --no-save @mermaid-js/mermaid-cli"
    )


def protect_math_segments(text: str) -> tuple[str, list[str]]:
    chunks: list[str] = []

    def stash(m: re.Match[str]) -> str:
        chunks.append(m.group(0))
        return f"@@MATH{len(chunks) - 1}@@"

    for pat in (
        r"\$\$.*?\$\$",
        r"(?<!\$)\$(?!\$).*?(?<!\$)\$(?!\$)",
        r"\\\(.*?\\\)",
        r"\\\[.*?\\\]",
    ):
        text = re.sub(pat, stash, text, flags=re.DOTALL)
    return text, chunks


def restore_math(text: str, chunks: list[str]) -> str:
    for i, chunk in enumerate(chunks):
        text = text.replace(f"@@MATH{i}@@", chunk)
    return text


def wrap_bare_unicode_math(text: str) -> str:
    parts = re.split(r"(```.*?```)", text, flags=re.DOTALL)
    out: list[str] = []
    for part in parts:
        if part.startswith("```"):
            out.append(part)
            continue
        protected, chunks = protect_math_segments(part)

        def repl_run(m: re.Match[str]) -> str:
            tex = m.group(0)
            for u, t in UNICODE_MATH.items():
                tex = tex.replace(u, t)
            return f"${tex}$"

        keys = sorted(UNICODE_MATH, key=len, reverse=True)
        class_chars = "".join(re.escape(k) for k in keys)
        protected = re.sub(
            rf"(?:[{class_chars}][A-Za-z0-9_^{{\}}\+\-\/=]*)+",
            repl_run,
            protected,
        )
        for u, t in UNICODE_MATH.items():
            protected = protected.replace(u, f"${t}$")
        out.append(restore_math(protected, chunks))
    return "".join(out)


def render_mermaid_blocks(md: str, stem: str) -> str:
    """Replace ```mermaid blocks with rendered PNG images for pandoc."""
    FIGS.mkdir(parents=True, exist_ok=True)
    mmdc = find_mmdc()
    puppeteer_cfg = BUILD / "puppeteer.json"
    # Prefer system Chrome if present (avoids downloading Chromium)
    chrome_candidates = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
        "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    ]
    cfg: dict = {"args": ["--no-sandbox"]}
    for chrome in chrome_candidates:
        if Path(chrome).is_file():
            cfg["executablePath"] = chrome
            break
    puppeteer_cfg.write_text(json.dumps(cfg), encoding="utf-8")

    counter = 0

    def repl(m: re.Match[str]) -> str:
        nonlocal counter
        counter += 1
        src = m.group(1).strip() + "\n"
        base = f"{stem}_{counter}"
        mmd_path = FIGS / f"{base}.mmd"
        png_path = FIGS / f"{base}.png"
        mmd_path.write_text(src, encoding="utf-8")
        cmd = [
            mmdc,
            "-i",
            str(mmd_path),
            "-o",
            str(png_path),
            "-b",
            "white",
            "-s",
            "2",
            "-p",
            str(puppeteer_cfg),
        ]
        print("Mermaid:", " ".join(cmd))
        proc = subprocess.run(cmd, capture_output=True, text=True)
        if proc.returncode != 0 or not png_path.is_file():
            print(proc.stdout)
            print(proc.stderr)
            raise SystemExit(f"mmdc failed for {mmd_path}")
        # Path relative to BUILD (pandoc cwd); graphicspath also has figures/
        return (
            f"\n\\begin{{figure}}[H]\n"
            f"\\centering\n"
            f"\\includegraphics[width=0.92\\linewidth]{{{base}.png}}\n"
            f"\\end{{figure}}\n"
        )

    return re.sub(r"```mermaid\n(.*?)```", repl, md, flags=re.DOTALL)


def normalize_md(md: str, stem: str) -> str:
    md = re.sub(
        r"\[([^\]]+)\]\(/Users/ajjc/\.cursor/projects/[^)]+\)",
        r"\1",
        md,
    )
    md = re.sub(r"\[([^\]]+)\]\((?:\.\./)?docs/[^)]+\)", r"\1", md)
    md = re.sub(r"\[([^\]]+)\]\((?:\./)?[^)]+\.md\)", r"\1", md)
    md = render_mermaid_blocks(md, stem)
    md = md.replace(r"\setminus", r"\backslash")
    md = re.sub(r"_\\mathbb\{([A-Za-z]+)\}", r"_{\\mathbb{\1}}", md)
    md = re.sub(r"_\\mathrm\{([^}]+)\}", r"_{\\mathrm{\1}}", md)
    md = re.sub(r"_\\operatorname\{([^}]+)\}", r"_{\\operatorname{\1}}", md)
    md = wrap_bare_unicode_math(md)
    return md


def combine_markdown() -> str:
    parts = [HEADER]
    for title, path in SOURCES:
        if not path.exists():
            continue
        stem = path.stem.replace(" ", "_")
        body = normalize_md(path.read_text(encoding="utf-8"), stem)
        body = re.sub(r"^# ", "## ", body, count=1, flags=re.MULTILINE)
        parts.append(f"\\newpage\n\n# {title}\n\n{body}\n")
    return "\n".join(parts)


def main() -> None:
    pandoc = find_pandoc()
    tectonic = find_tectonic()
    BUILD.mkdir(parents=True, exist_ok=True)
    FIGS.mkdir(parents=True, exist_ok=True)

    md_path = BUILD / "Hilbert_Smith_Audit.md"
    md_path.write_text(combine_markdown(), encoding="utf-8")

    tex_path = BUILD / "Hilbert_Smith_Audit.tex"
    pdf_tmp = BUILD / "Hilbert_Smith_Audit.pdf"

    cmd = [
        pandoc,
        str(md_path),
        "-f",
        "markdown+tex_math_dollars+tex_math_single_backslash+pipe_tables+yaml_metadata_block+raw_tex",
        "-t",
        "pdf",
        f"--pdf-engine={tectonic}",
        "-V",
        "documentclass=article",
        "-o",
        str(pdf_tmp),
    ]
    print("Running:", " ".join(cmd))
    proc = subprocess.run(cmd, cwd=BUILD, capture_output=True, text=True)
    if proc.returncode != 0:
        subprocess.run(
            [
                pandoc,
                str(md_path),
                "-f",
                "markdown+tex_math_dollars+tex_math_single_backslash+pipe_tables+yaml_metadata_block+raw_tex",
                "-t",
                "latex",
                "-s",
                "-o",
                str(tex_path),
            ],
            cwd=BUILD,
            check=False,
        )
        print(proc.stdout)
        print(proc.stderr)
        raise SystemExit(f"pandoc/tectonic failed with code {proc.returncode}")

    shutil.copy2(pdf_tmp, OUT)
    print(f"Wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
