#!/usr/bin/env bash

SCRIPT=`realpath $0`
SCRIPTPATH=`dirname $SCRIPT`

export PYTHONPATH=$SCRIPTPATH

# py.test -vs apps/tests/
# py.test -vs snippets/tests/test_detect_language.py
# py.test -vs tests/test_web.py
# py.test -vs tests/test_ocr.py
# py.test -vs tests/test_utils.py
# py.test -vs tests/number/
# py.test -vs tests/test_audio.py
# py.test -vs tests/test_video.py
# py.test -vs tests/test_ini.py
# py.test -vs tests/test_jhash.py
# py.test -vs tests/test_fs.py
# py.test -vs tests/test_imgur.py
# py.test -vs tests/test_dateandtime.py
# py.test -vs tests/test_torrent.py
py.test -vs tests/test_web.py
# py.test -vs tests/test_network.py
