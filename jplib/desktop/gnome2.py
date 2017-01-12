#!/usr/bin/env python3
# encoding: utf-8

"""
Working with Gnome 2.
"""

import shlex
import sys
from subprocess import call

from jplib import process


def set_wallpaper(img, mode='stretched'):
    """Set the given file as wallpaper.

    Possible modes: wallpaper, centered, scaled, stretched."""
    cmd1 = "gconftool-2 --type=string --set /desktop/gnome/background/picture_options {mode}".format(mode=mode)
    cmd2 = "gconftool-2 --type=string --set /desktop/gnome/background/picture_filename {img}".format(img=img)

    print('#', cmd1)
    call(shlex.split(cmd1))
    print('#', cmd2)
    call(shlex.split(cmd2))


def get_wallpaper():
    """Get the path of the file that is set as wallpaper."""

    cmd = "gconftool-2 --get /desktop/gnome/background/picture_filename"
    print('#', cmd)
    return process.get_simple_cmd_output(cmd).strip()

#############################################################################

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(get_wallpaper())
    else:
        img = sys.argv[1]
        set_wallpaper(img)
