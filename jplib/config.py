#!/usr/bin/env python3

"""
Configuration part.
"""

__author__ = "Laszlo Szathmary (jabba.laci@gmail.com)"
__version__ = "0.3"
__date__ = "20170112"
__copyright__ = "Copyright (c) 2011-2017 Laszlo Szathmary"
__license__ = "MIT"

import os

from unipath import Path

# # portability tip: in ~/.mozilla/firefox put a symbolic link on
# # ~/.mozilla/firefox/XXXXXXXX.default/cookies.sqlite
# COOKIE_DB = "{home}/.mozilla/firefox/cookies.sqlite".format(home=os.path.expanduser('~'))
# ESPEAK = '/usr/bin/espeak'
PLAYER = '/usr/bin/mpv'
# WGET = '/usr/bin/wget'
# XSEL = '/usr/bin/xsel'
# TIDY = '/usr/bin/tidy'
# LYNX = '/usr/bin/lynx'
TESSERACT = '/usr/bin/tesseract'
XRANDR = '/usr/bin/xrandr'
# FPING = '/usr/bin/fping'
# XDOTOOL = '/usr/bin/xdotool'
#
required_files = (
#     COOKIE_DB,      # to get webpages that are protected with cookies
#     ESPEAK,         # text to speech
     PLAYER,        # play audio/video
#     WGET,           # get webpages
#     XSEL,           # copy to clipboard
#     TIDY,           # tidy up HTML source
#     LYNX,           # for converting HTML to text
     TESSERACT,      # OCR
     XRANDR,         # screen resolution
#     FPING,          # pings hosts, produces readable output
#     XDOTOOL,        # xdotool, command-line X11 automation tool
#                     # (get window ID, put focus on a window, etc.)
)

USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0'
#COOKIES_TXT = '{home}/tmp/cookies_jabbapylib_tmp.txt'.format(home=os.path.expanduser('~'))

ROOT_DIR = os.path.dirname(__file__)

TEST_ASSETS_DIR = Path(ROOT_DIR, '../tests/_assets')
TEST_TMP_DIR = Path(ROOT_DIR, '../tests/_tmp')
TEST_TMP_FILE = Path(ROOT_DIR, '../tests/_tmp/test.tmp')

TMP_DIR = '/tmp/jabbapylib_20120119_tmp'
TMP_FILE = '/tmp/jabbapylib_20120119_tmp.txt'

#HTML2TEXT = Path(ROOT_DIR, 'lib/html2text.py')

# an anonymous API key (find more at http://imgur.com/apps)
IMGUR_KEY = '014fd9069edf931bf1148b80da1cd09e'


def hello():
    print("hello from jplib.config :)")

#############################################################################

if __name__ == "__main__":
    print(TEST_ASSETS_DIR.absolute())
