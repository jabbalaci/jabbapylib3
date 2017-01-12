# coding: utf-8

from jplib import imgur


def test_get_gallery_images():
    url = "http://imgur.com/a/O4lle"
    res = imgur.get_gallery_images(url)
    assert len(res) == 2
