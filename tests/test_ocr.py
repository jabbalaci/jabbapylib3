# coding: utf-8

from unipath import Path

from jplib import config as cfg
from jplib import ocr

TEST_DIR = Path(cfg.TEST_ASSETS_DIR, 'ocr')

PHOTOTEST_TIF = """This is a lot of 12 point text to test the
ocr code and see if it works on all types
of file format.

The quick brown dog jumped over the
lazy fox. The quick brown dog jumped
over the lazy fox. The quick brown dog
jumped over the lazy fox. The quick
brown dog jumped over the lazy fox."""


def test_image_file_to_string():
    res = ocr.image_file_to_string(Path(TEST_DIR, 'fnord.png')).strip()
    assert res == 'fnord'
    #
    res = ocr.image_file_to_string(TEST_DIR + '/fonts_test.png')
    words = ["12 pt", "24 pt", "Courier", "Times", "Arial", "jukeboxes"]
    for w in words:
        assert w in res
    #
    res = ocr.image_file_to_string(Path(TEST_DIR, 'phototest.png')).strip()
    assert res == PHOTOTEST_TIF
