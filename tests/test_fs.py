# coding: utf-8

import os
import re
import sys

from jplib import config as cfg
from jplib import fs

FILE = cfg.TEST_ASSETS_DIR + '/text.txt'
JSON = cfg.TEST_ASSETS_DIR + '/json.json'
NFO1 = cfg.TEST_ASSETS_DIR + '/nfo/movie_1.nfo'
NFO2 = cfg.TEST_ASSETS_DIR + '/nfo/movie_2.nfo'


class TestFileSystem(object):

    def test_read_first_line(self):
        res = fs.read_first_line(FILE)
        assert res == 'first line'

    def test_is_local_path(self):
        assert fs.is_local_path(FILE)
        assert not fs.is_local_path('http://google.com')

    def test_is_image_file(self):
        assert fs.is_image_file('/trash/well.jpg')
        assert fs.is_image_file('/trash/well.jpeg')
        assert fs.is_image_file('/trash/well.png')
        assert fs.is_image_file('/trash/well.gif')
        assert fs.is_image_file('/trash/well.JPG')
        assert fs.is_image_file('/trash/well.PNG')
        #
        assert not fs.is_image_file('/trash/well.txt')
        assert not fs.is_image_file('/trash/well.py')
        assert not fs.is_image_file('/trash/well.java')

    def test_get_timestamped_filename(self):
        res = fs.get_timestamped_filename()
        assert re.search('^\d{8}_\d{6}\.txt$', res)

    def test_remove_file_silently(self):
        fname = '/stupid_directory_name/doesnt_exist.txt'
        assert fs.remove_file_silently(fname)
        assert fs.touch(cfg.TMP_FILE)
        assert os.path.exists(cfg.TMP_FILE)
        assert fs.remove_file_silently(cfg.TMP_FILE)

    def test_touch(self):
        assert fs.remove_file_silently(cfg.TMP_FILE)
        #
        assert fs.touch(cfg.TMP_FILE)
        assert os.path.exists(cfg.TMP_FILE)
        #
        assert fs.remove_file_silently(cfg.TMP_FILE)
        assert fs.touch(cfg.TMP_FILE, mode=0o644)
        assert fs.get_oct_mode(cfg.TMP_FILE) in ('0644', '0o644')
        #
        assert fs.remove_file_silently(cfg.TMP_FILE)

    def test_get_oct_mode(self):
        assert fs.remove_file_silently(cfg.TMP_FILE)
        #
        assert fs.touch(cfg.TMP_FILE, mode=0o755)
        assert fs.get_oct_mode(cfg.TMP_FILE) in ('0755', '0o755')
        #
        assert fs.remove_file_silently(cfg.TMP_FILE)

    def test_set_mode_to(self):
        assert fs.remove_file_silently(cfg.TMP_FILE)
        #
        assert fs.touch(cfg.TMP_FILE, mode=0o600)
        assert fs.get_oct_mode(cfg.TMP_FILE) in ('0600', '0o600')
        assert fs.set_mode_to(cfg.TMP_FILE, 0o755)
        assert fs.set_mode_to(cfg.TMP_FILE, 0o700)
        #
        assert fs.remove_file_silently(cfg.TMP_FILE)

    def test_store_content_in_file(self):
        content = "0123456789"
        assert not os.path.exists(cfg.TEST_TMP_FILE)
        fs.store_content_in_file(content, cfg.TEST_TMP_FILE)
        assert os.path.getsize(cfg.TEST_TMP_FILE) > 0
        os.unlink(cfg.TEST_TMP_FILE)

    def test_which(self):
        if sys.platform.startswith('linux'):
            cmd = 'bash'
            assert '/bin/bash' in fs.which(cmd)     # can be /usr/bin/bash too
        else:
            print("# test_which is passed on this podium (TODO)")

    def test_read_json(self):
        d = fs.read_json(JSON)
        assert d['name'] == 'Jabba Laci'

    def test_is_binary(self):
        assert fs.is_binary('/bin/bash')
        assert fs.is_binary('/bin/cat')
        assert fs.is_binary('/bin/date')
        #
        assert not fs.is_binary('/etc/fstab')
        assert not fs.is_binary('/etc/hosts')
        assert not fs.is_binary('/etc/passwd')

    def test_extract_urls(self):
        assert fs.extract_urls(NFO1) == ["http://www.imdb.com/title/tt2911666/"]
        assert fs.extract_urls(NFO2, "latin1") == ['http://tinyurl.com/m7ku59t', 'http://www.imdb.com/title/tt0458481/']

    def test_get_free_space(self):
        val = fs.get_free_space("/", humanize=False)
        assert val > 0
        assert isinstance(val, int)
        #
        val = fs.get_free_space("/", humanize=True)
        assert isinstance(val, str)
        val = fs.get_free_space("/")
        assert isinstance(val, str)
