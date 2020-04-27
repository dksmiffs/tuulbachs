#!/usr/bin/env bash
pushd ..
  pip install . --upgrade
  cd docs
  make html
popd
