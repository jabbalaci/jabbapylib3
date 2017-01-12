# coding: utf-8

from pprint import pprint

from jplib import config as cfg
from jplib import torrent

FILE = cfg.TEST_ASSETS_DIR + '/ubuntu.torrent'


def test_torrent():
    t = torrent.process(FILE)
    assert t['info']['name'] == 'ubuntu-11.10-desktop-amd64.iso'
    assert t['info']['length'] == 731164672
