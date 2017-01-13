#!/usr/bin/env python3
# encoding: utf-8

"""
Working with Gnome 3.
"""

import sys

if __name__ == "__main__":
    import os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))

import shlex
import sys
from subprocess import call

from jplib import process


def set_wallpaper(img):
    """Set the given file as wallpaper."""

    uri = 'file://' + img
    cmd = 'gsettings set org.gnome.desktop.background picture-uri {uri}'.format(uri=uri)
    print('#', cmd)
    call(shlex.split(cmd))


def get_wallpaper():
    """Get the path of the file that is set as wallpaper."""

    cmd = 'gsettings get org.gnome.desktop.background picture-uri'
    print('#', cmd)
    uri = process.get_simple_cmd_output(cmd)
    return uri.replace("'", "").strip()

#############################################################################

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(get_wallpaper())
    else:
        img = sys.argv[1]
        set_wallpaper(img)
