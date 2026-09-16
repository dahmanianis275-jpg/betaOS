#!/usr/bin/env python3
"""
HybridOS – Terminal Operating System Simulator
Windows + Linux in one masterpiece terminal experience.

Run:  python3 main.py
"""

import sys
from pathlib import Path

# Make sure the package root is on the path
ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT))

from core.shell import HybridShell

def main():
    shell = HybridShell()
    shell.run()

if __name__ == "__main__":
    main()
