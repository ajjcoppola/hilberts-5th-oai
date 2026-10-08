#!/usr/bin/env python3
"""Build Dabrowski_HS_Audit.pdf with TeX math and rendered Mermaid diagrams."""

from __future__ import annotations

import importlib.util
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HERE = Path(__file__).resolve().parent
DOCS = ROOT / "dabrowski" / "docs"
OUT = DOCS / "Dabrowski_HS_Audit.pdf"
BUILD = ROOT / "build" / "dabrowski_audit_pdf"
FIGS = BUILD / "figures"

spec = importlib.util.spec_from_file_location("auditpdf", HERE / "build_audit_pdf.py")
assert spec is not None and spec.loader is not None
auditpdf = importlib.util.module_from_spec(spec)
spec.loader.exec_module(auditpdf)

auditpdf.ROOT = ROOT
auditpdf.DOCS = DOCS
auditpdf.OUT = OUT
auditpdf.BUILD = BUILD
auditpdf.FIGS = FIGS

BODY_SOURCES = [
    ("Proof overview (Q1, Q2, Q4, Q6)", DOCS / "01_proof_overview.md"),
    ("Audit ledger (Targets A--C)", DOCS / "02_audit_ledger.md"),
    ("Sponge stress test (Q5)", DOCS / "03_sponge_stress_test.md"),
    ("Public responses (Q3)", DOCS / "04_public_responses.md"),
    ("Versus OpenAI", DOCS / "05_vs_openai.md"),
    ("Lemma dependency ledger", DOCS / "lemma_dependency_ledger.md"),
    ("Sherlock session log", DOCS / "SHERLOCK_DABROWSKI_HS_2026-10-08.md"),
]
APPENDIX_SOURCES = [
    ("Directory README", ROOT / "dabrowski" / "README.md"),
    ("Repository README", ROOT / "README.md"),
]

HEADER = r"""---
title: "Response: Dabrowski Hilbert--Smith preprint"
subtitle: "Sherlock reverse-verification notes"
author: "Cursor(Opus 5.5/Grok), driven by: Alan Coppola"
date: "2026-10-08"
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
{\small\textit{Independent read of
\texttt{Integral tail signatures and the Hilbert--Smith conjecture}}\\
Upstream: \texttt{github.com/adbrw/HS\_proof} \quad SHA: \texttt{abb0c44\ldots}\\
PDF SHA-256: \texttt{e305fd47\ldots}\quad
Repo: \texttt{github.com/ajjcoppola/hilberts-5th-oai}}
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
Dabrowski's preprint claims a proof of the Hilbert--Smith conjecture by
ruling out effective continuous $\mathbb{Z}_p$-actions on connected
finite-dimensional manifolds (boundary allowed). The argument is not
Yang's orbit-dimension obstruction and is not Pardon's three-manifold
mapping-class argument. It is an integrality-versus-$p$-divisibility
contradiction for an \emph{integer signature tail} in ultimate quadratic
$L_4$: a small open tail of $\mathbb{Z}_p$ Haar-averages a degree-one
pinch in a Euclidean chart; finite quotients and a character detector
produce a duality-compatible homotopy idempotent on
$S^n\times\mathbb{CP}^2$; iterated Karoubi localization boundaries
recover one copy of $\mathbb{CP}^2$, giving a class whose ordinary
signatures are eventually $1$. Independently, on a fixed compact free
$C_p$-space, permutation-tensoring is locally $p$ copies of the identity
and is nilpotent after Mayer--Vietoris, so every $L_4$ class has
eventually $p$-divisible signatures. Hence $1\in p\mathbb{Z}$. This is
the same obstruction family as the OpenAI (2026-09-23) Witt-sheaf
argument, with different packaging. A targeted audit found no outright
failure in the load-bearing PDF lemmas; several steps remain weak
(negative $K$ / tail extraction, nilpotence of $\nu$, the graph corner,
$\mathbb{CP}^2$ evaluation, and an independently printed Lean axiom
list). On Menger-type sponges, where faithful $\mathbb{Z}_p$ actions
exist, the writeup correctly refuses to run because chart and
combinatorial dual-cell hypotheses fail. The claimed Lean 4 certificate
was not rerun in this session.

\newpage

"""

FOOTER = r"""
\newpage
\appendix
\section*{Appendix: contents}
\tableofcontents

"""


def combine_markdown() -> str:
    parts = [HEADER]
    for title, path in BODY_SOURCES:
        if not path.exists():
            continue
        stem = path.stem.replace(" ", "_")
        body = auditpdf.normalize_md(path.read_text(encoding="utf-8"), stem)
        body = __import__("re").sub(r"^# ", "## ", body, count=1, flags=__import__("re").MULTILINE)
        parts.append(f"\\newpage\n\n# {title}\n\n{body}\n")
    parts.append(FOOTER)
    for title, path in APPENDIX_SOURCES:
        if not path.exists():
            continue
        stem = path.stem.replace(" ", "_")
        body = auditpdf.normalize_md(path.read_text(encoding="utf-8"), stem)
        body = __import__("re").sub(r"^# ", "## ", body, count=1, flags=__import__("re").MULTILINE)
        parts.append(f"\\newpage\n\n# {title}\n\n{body}\n")
    return "\n".join(parts)


def main() -> None:
    pandoc = auditpdf.find_pandoc()
    tectonic = auditpdf.find_tectonic()
    BUILD.mkdir(parents=True, exist_ok=True)
    FIGS.mkdir(parents=True, exist_ok=True)

    md_path = BUILD / "Dabrowski_HS_Audit.md"
    md_path.write_text(combine_markdown(), encoding="utf-8")

    tex_path = BUILD / "Dabrowski_HS_Audit.tex"
    pdf_tmp = BUILD / "Dabrowski_HS_Audit.pdf"

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
