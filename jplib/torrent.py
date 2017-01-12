#!/usr/bin/env python3

"""
based on http://effbot.org/zone/bencode.htm

# from jplib import torrent
"""

import json
import pprint
import sys

import six

from jplib import utils
from jplib.lib.bencodepy import decode_from_file


def process(fname):
    d = decode_from_file(fname)
    del d[b"info"][b"pieces"]

    if six.PY3:
        d = json.loads(pprint.pformat(d).replace("b'", "'").replace("'", '"'))
    if six.PY2:
        d = json.loads(json.dumps(d))

    return d

#############################################################################

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("{prg}: error: specify a .torrent file".format(prg=sys.argv[0]))
        sys.exit(1)
    # else
    info = process(sys.argv[1])
    pprint.pprint(info)
    print(utils.filesize_fmt(info['info']['length']))
