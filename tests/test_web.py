import os

from jplib import config as cfg
from jplib import web

GOOGLE = 'http://google.com'
GOOGLE_HTML = ''
JS_TEST_PAGE = 'http://www.isjavascriptenabled.com/'


def setup_module(module):
    """runs just once per module"""
    global GOOGLE_HTML
    GOOGLE_HTML = web.get_page(GOOGLE)
    try:
        os.unlink(cfg.TEST_TMP_FILE)
    except:
        pass    # maybe it didn't exist

#############################################################################

def test_get_page():
    assert '<title>Google</title>' in GOOGLE_HTML


def test_get_js_page():
    js_ok = '</script><h1 id="yes">YES</h1>'
    js_missing = '<noscript><h1 id="no">NO!</h1>'
    #
    res = web.get_js_page(JS_TEST_PAGE)
    assert js_ok in res and js_missing not in res
    # can be called again:
    res = web.get_js_page(JS_TEST_PAGE)
    assert js_ok in res and js_missing not in res
    # without JavaScript
    res = web.get_page(JS_TEST_PAGE)
    assert js_ok not in res and js_missing in res


def test_download_to():
    assert not os.path.exists(cfg.TEST_TMP_FILE)
    web.download_to(GOOGLE, cfg.TEST_TMP_FILE)
    assert os.path.getsize(cfg.TEST_TMP_FILE) > 0
    os.unlink(cfg.TEST_TMP_FILE)
