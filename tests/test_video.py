# coding: utf-8

import glob
import os
import re

from jplib import config as cfg
from jplib import video

FILE = cfg.TEST_ASSETS_DIR + '/video.avi'


def test_get_info():
    res = video.get_info(FILE)
    assert type(res) is dict and 'ID_VIDEO_FPS' in res


def test_get_duration():
    delta = 0.05
    assert abs(5.0 - video.get_duration(FILE)) < delta


def test_get_summary():
    res = video.get_summary(FILE)
    match = re.search(r'VIDEO:.*854x480.*23.976 fps', res)
    assert match is not None


def test_make_screenshot():
    res = video.make_screenshot(FILE, 4, outdir=cfg.TEST_TMP_DIR)
    ss_file = cfg.TEST_TMP_DIR + '/' + video.MPLAYER_SCREENSHOT_FILE
    assert res and os.path.exists(ss_file)
    # clean up
    for f in glob.glob(cfg.TEST_TMP_DIR + '/*.jpg'):
        os.unlink(f)
