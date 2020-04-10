#!/usr/bin/env bash

# This tuulbachs script is intended as a wrapper.  Do the minimum possible work
#    in this script to get into Python as quickly as possible, and to avoid
#    modifying the calling user's shell environment directly.

# Some environments require positive action to make Python available
. ./kickpy.config
[[ ! -z "$enable_python" ]] && $enable_python

# Now find Python
pycmd=$(which python3)
[[ -z "$pycmd" ]] && pycmd=$(which python)
if [[ -z "$pycmd" ]]; then
  echo "ERROR:  Couldn't find Python, exiting."
  exit 1
fi

# Pass along all arguments
$pycmd $@
