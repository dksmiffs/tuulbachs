#!/usr/bin/env bash
pushd ..
  python -m pip install . --upgrade
  cd docs
  make clean
  make html
popd
