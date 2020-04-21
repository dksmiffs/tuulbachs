"""
version.py
==================
Utility functions for managing a tuulbachs-formatted version YAML file
"""

import semver
from   tuulyaml.parse               import parse_yaml
from   tuulyaml.update_simple_value import update_value


# -----
def emit_product_name(filename):
  """
  Return the product name value from the input YAML filename
  """
  cfg = parse_yaml(filename)
  return cfg['product_name']


# -----
def emit_version(filename):
  """
  Return the version value from the input YAML filename
  """
  cfg = parse_yaml(filename)
  return str(cfg['version'])


# -----
def bump_major(filename):
  """
  Bump the major portion of the version from the input YAML filename
  """
  v = semver.VersionInfo.parse(emit_version(filename))
  update_value(filename, 'version', str(v.bump_major()))


# -----
def bump_minor(filename):
  """
  Bump the minor portion of the version from the input YAML filename
  """
  v = semver.VersionInfo.parse(emit_version(filename))
  update_value(filename, 'version', str(v.bump_minor()))


# -----
def bump_pre(filename, prebase='pre'):
  """
  Bump the "pre" portion of the version from the input YAML filename
  """
  v = semver.VersionInfo.parse(emit_version(filename))
  if v.prerelease is None:
    new_ver = str(v.replace(prerelease=prebase+'.1'))
  else:
    new_ver = semver.bump_prerelease(version)
  update_value(filename, 'version', new_ver)


# -----
def bump_build(filename):
  """
  Bump the "build" portion of the version from the input YAML filename
  """
  v = semver.VersionInfo.parse(emit_version(filename))
  if v.build is None:
    new_ver = str(v.replace(build='build.1'))
  else:
    new_ver = semver.bump_build(version)
  update_value(filename, 'version', new_ver)


# -----
if '__main__' == __name__:
  fname = '../version.yaml'
  print(emit_product_name(fname) + ' ' + emit_version(fname))
