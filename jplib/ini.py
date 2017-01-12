#!/usr/bin/env python3

"""
Process .ini configuration files.

# from jplib import ini
"""

from unipath import Path

from jplib import config as cfg
from six.moves import configparser


def read_section(section, fname):
    """Read the specified section of an .ini file."""
    conf = configparser.ConfigParser()
    conf.read(fname)
    val = {}
    try:
        val = dict((v, k) for v, k in conf.items(section))
        return val
    except configparser.NoSectionError:
        return None

#############################################################################

if __name__ == "__main__":
    ini_file = Path(cfg.TEST_ASSETS_DIR, "profiles.ini")
    print(read_section('Profile0', ini_file))
