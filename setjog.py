#!/usr/bin/env python3
# encoding: utf-8

"""
Python 3 project
"""

import os
import re
from unipath import Path


def chmod(pattern, mode, fullname):
    if re.search(pattern, fullname):
        print("{f} => {m:o}".format(f=fullname, m=mode))
        fullname.chmod(mode)


def process(p):
    """
    The pattern is matched against the path of a file. If you want to
    match just the name of the file, start the pattern with a ".*/".
    """
    chmod(r"\.py$", 0o755, p)
    chmod(r"\.sh$", 0o755, p)
    chmod(r".*/__init__.py$", 0o644, p)
    chmod(r".*/test_.*\.py$", 0o644, p)
    chmod(r".*/scraper/examples\.py$", 0o644, p)


def traverse(folder):
    for path, _, files in os.walk(folder):
        for f in files:
            fullname = Path(path, f)
#            print(fullname)
            process(fullname)

##############################################################################

if __name__ == "__main__":
    traverse(".")
