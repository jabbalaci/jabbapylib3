#!/usr/bin/env bash

SCRIPT=`realpath $0`
SCRIPTPATH=`dirname $SCRIPT`

export PYTHONPATH=$SCRIPTPATH

OPTIONS="--continue-on-collection-errors"

py.test -vs apps/tests/ $OPTIONS
py.test -vs snippets/tests/ $OPTIONS
py.test -vs tests/ $OPTIONS
