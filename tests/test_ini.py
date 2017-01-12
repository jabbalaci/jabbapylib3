# coding: utf-8

from unipath import Path

from jplib import config as cfg
from jplib import ini


def test_read_ini():
    ini_file = Path(cfg.TEST_ASSETS_DIR, "profiles.ini")
    p0 = ini.read_section('Profile0', ini_file)
    assert p0["path"] == "oihdZqSc.default"
