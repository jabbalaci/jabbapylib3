#!/usr/bin/env bash

SCRIPT=`realpath $0`
SCRIPTPATH=`dirname $SCRIPT`

export PYTHONPATH=$SCRIPTPATH

# OPTIONS="--continue-on-collection-errors --doctest-modules"

pytest -vs apps/tests/
pytest -vs snippets/tests/
pytest -vs tests/
