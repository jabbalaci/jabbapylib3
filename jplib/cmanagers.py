#!/usr/bin/env python3

"""
Context managers.

# from jplib.cmanagers import ChDir
"""

import os

from jplib import fs


class ChDir(object):
    """
    Step into a directory temporarily.
    """
    def __init__(self, path):
        self.old_dir = os.getcwd()
        self.new_dir = path

    def __enter__(self):
        os.chdir(self.new_dir)

    def __exit__(self, *args):
        os.chdir(self.old_dir)

##############################################################################

if __name__ == "__main__":
    with ChDir("/tmp/test"):
        fs.touch("test.txt")
    #
    fs.touch("here.txt")
