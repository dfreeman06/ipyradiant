""" packaging information for ipyradiant
"""
import re
import sys
from pathlib import Path

import setuptools

if __name__ == "__main__":
    setuptools.setup(
        version=re.findall(
            r"""__version__ = "([^"]+)"$""",
            (Path(__file__).parent / "src" / "ipyradiant" / "_version.py").read_text(),
        )[0],
    )