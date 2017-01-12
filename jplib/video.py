#!/usr/bin/env python3

"""
Working with video files.
* get video information
* take a screenshot from a video at a given time

# from jplib import video
"""

import os
import re
from pprint import pprint

from jplib import config as cfg
from jplib import process

MPLAYER_SCREENSHOT_FILE = '00000001.jpg'

screenshot = "/usr/bin/mplayer '{0}' -ss '{1}' -noautosub -frames 1 -ao null -vo jpeg:outdir='{2}'"
video_info = "/usr/bin/mplayer '{0}' -ao null -vo null -frames 1 -identify"


def get_info(video_file):
    """Get info about a video.

    The info is returned by mplayer. The result is a
    dictionary whose keys start with 'ID_'.
    """
    cmd = video_info.format(video_file)
    output = process.get_simple_cmd_output(cmd)
    return dict(re.findall('(ID_.*)=(.*)', output))


def get_duration(video_file):
    """Get the length of a video in seconds.

    The length is extracted with mplayer.
    The return value is a real number.
    """
    info = get_info(video_file)
    return float(info['ID_LENGTH'])


def get_summary(video_file):
    """Get a one-line summary of the video file.

    Example: 'VIDEO:  [WMV3]  320x240  24bpp  1000.000 fps  386.0 kbps (47.1 kbyte/s)'
    """
    cmd = video_info.format(video_file)
    output = process.get_simple_cmd_output(cmd)
    return re.findall("VIDEO\:.*", output)[0]


def make_screenshot(video_file, sec, outdir='/tmp', rm=True):
    """Make a screenshot from a video at a given time.

    Work is done with mplayer. Specify the video file,
    the time in seconds when to take the screenshot,
    and the output directory. If rm is True, a previous
    screenshot file is removed first.
    By default, the screenshot is named 00000001.jpg.
    """
    # by default, mplayer saves here the screenshot:
    full_path = os.path.join(outdir, MPLAYER_SCREENSHOT_FILE)
    if rm and os.path.exists(full_path):
        os.remove(full_path)

    cmd = screenshot.format(video_file, sec, outdir)
    #print cmd
    if process.get_return_code_of_simple_cmd(cmd) == 0:
        if os.path.exists(full_path):
            return full_path
    # else
    return None

#############################################################################

if __name__ == "__main__":
    video = cfg.TEST_ASSETS_DIR + '/video.avi'
    pprint(get_info(video))
    print(make_screenshot(video, 4))
    print(get_duration(video))
    print(get_summary(video))
