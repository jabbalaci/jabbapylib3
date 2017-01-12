# coding: utf-8

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import re

import bing


def test_extract():
    img_url, save_name = bing.extract(test=True)
    assert 'www.bing.com' in img_url
    #
    assert re.search('^\d{4}_\d\d_\d\d\-.*$', save_name)
