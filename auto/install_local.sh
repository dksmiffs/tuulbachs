#!/usr/bin/env bash
pushd ..
  python -m pip install . --upgrade --use-feature=in-tree-build
  cd docs
  make clean
  make html
popd
