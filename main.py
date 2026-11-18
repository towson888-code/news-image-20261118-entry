#!/usr/bin/env python3
"""News-image entry for make.fun news-image-20261118 (Python 3.13, stdlib only).

The entry image is the entry.png beside this file: a newspaper-style front
page summing up Wednesday 18 November 2026 world news. The program copies it
to /output/entry.png. No network, no dependencies, deterministic.
Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil

_HERE = os.path.dirname(os.path.abspath(__file__))
_SRC = os.path.join(_HERE, "entry.png")
_OUTDIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
_DST = os.path.join(_OUTDIR, "entry.png")

os.makedirs(_OUTDIR, exist_ok=True)
shutil.copyfile(_SRC, _DST)
