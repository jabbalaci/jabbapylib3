#!/usr/bin/env bash

SCRIPT=`realpath $0`
SCRIPTPATH=`dirname $SCRIPT`

export PYTHONPATH=$SCRIPTPATH

# OPTIONS="--continue-on-collection-errors --doctest-modules"

# pytest -vs apps/tests/
# pytest -vs snippets/tests/test_detect_language.py
# pytest -vs tests/test_web.py
# pytest -vs tests/test_ocr.py
# pytest -vs tests/test_utils.py
# pytest -vs tests/number/
# pytest -vs tests/test_audio.py
# pytest -vs tests/test_video.py
# pytest -vs tests/test_ini.py
pytest -vs tests/test_jhash.py
# pytest -vs tests/test_fs.py
# pytest -vs tests/test_imgur.py
# pytest -vs tests/test_dateandtime.py
# pytest -vs tests/test_torrent.py
# pytest -vs tests/test_web.py
# pytest -vs tests/test_network.py
