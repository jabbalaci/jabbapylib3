# coding: utf-8

from jplib import config as cfg
from jplib import audio

FILE = cfg.TEST_ASSETS_DIR + '/audio.mp3'


def test_get_info():
    res = audio.get_info(FILE)
    assert type(res) is dict and 'bit_rate' in res


def test_get_duration():
    res = audio.get_duration(FILE)
    assert 8.0 < res < 8.5
