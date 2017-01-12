#!/usr/bin/env python3

"""
Playing audio (and video too) files.

# from jplib import audio
"""

import os

if __name__ == "__main__":
    import sys
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from pathlib import Path
from pprint import pprint

from jplib import config as cfg
from jplib.lib.pymediainfo import MediaInfo


def get_info(fname):
    """
    >>> isinstance(get_info(str(Path(cfg.TEST_ASSETS_DIR, 'audio.mp3'))), dict)
    True
    >>> 'bit_rate' in get_info(str(Path(cfg.TEST_ASSETS_DIR, 'audio.mp3')))
    True
    """
    media_info = MediaInfo.parse(fname)
    for track in media_info.tracks:
        if track.track_type == 'Audio':
            return(track.to_data())


def get_duration(fname):
    """
    >>> get_duration(str(Path(cfg.TEST_ASSETS_DIR, 'audio.mp3')))
    8.228
    """
    media_info = MediaInfo.parse(fname)
    for track in media_info.tracks:
        if track.track_type == 'General':
            return track.duration / 1000


def play(audio_file, background=False, debug=False):
    """Play an audio file with mplayer."""
    cmd = '{player} "{audio}"'.format(player=cfg.PLAYER, audio=audio_file)
    if not debug:
        cmd += ' 1>/dev/null 2>&1'
    if background:
        cmd += ' &'
    os.system(cmd)

#############################################################################

if __name__ == "__main__":
    audio = str(Path(cfg.TEST_ASSETS_DIR, 'audio.mp3'))
#    play(audio, background=True)
    print(audio)
    print("-" * len(audio))
    pprint(get_info(audio))
    print(get_duration(audio))
