#!/usr/bin/env python3

"""
OCR with the Tesseract engine from Google
this is a wrapper around pytesser (http://code.google.com/p/pytesser/)

# from jabbapylib.ocr import ocr
"""

from jplib import config as cfg
from jplib.process import get_simple_cmd_output

TEST_DIR = cfg.TEST_ASSETS_DIR + '/ocr'


def image_file_to_string(fname):
    """Convert an image file to text using OCR."""
    cmd = "{tesseract} {fname} stdout".format(
        tesseract=cfg.TESSERACT,
        fname=fname
    )
    return get_simple_cmd_output(cmd).rstrip('\n')

#############################################################################

if __name__ == "__main__":
    print(image_file_to_string(TEST_DIR + '/fnord.png'))
    print('=' * 20)
    print(image_file_to_string(TEST_DIR + '/fonts_test.png'))
    print('=' * 20)
    print(image_file_to_string(TEST_DIR + '/phototest.png'))
