#!/usr/bin/env python3

"""
Working with Xfce4.
"""

import sys

if __name__ == "__main__":
    import os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))

import shlex
import sys
from subprocess import call

from jplib import process


def get_last_image_properties():
    cmd = "xfconf-query -c xfce4-desktop -l"
    result = [p for p in process.get_simple_cmd_output(cmd).split() if p.endswith("last-image")]
    return result


def set_wallpaper(img):
    """Set the given file as wallpaper."""

    props = get_last_image_properties()

    for p in props:
        cmd = 'xfconf-query -c xfce4-desktop -p {p} -s {img}'.format(p=p, img=img)
        print('#', cmd)
        call(shlex.split(cmd))


def get_wallpaper():
    """Get the path of the file that is set as wallpaper."""

    props = get_last_image_properties()

    res = []
    for p in props:
        cmd = 'xfconf-query -c xfce4-desktop -p {p}'.format(p=p)
#        print('#', cmd)
        uri = process.get_simple_cmd_output(cmd)
        res.append(uri.strip())
    #
    return res

#############################################################################

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(get_wallpaper())
    else:
        img = sys.argv[1]
        set_wallpaper(img)
