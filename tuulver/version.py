# emitter for tuulbachs-formatted version YAML file

import semver
from   tuulyaml.parse import parse_yaml


# -----
def emit_product_name(filename):
  cfg = parse_yaml(filename)
  return cfg['product_name']


# -----
def emit_version(filename):
  cfg = parse_yaml(filename)
  return str(cfg['version'])
  

# -----
def bump_pre(version, prebase='pre'):
  v = semver.VersionInfo.parse(version)
  if v.prerelease is None:
    return str(v.replace(prerelease=prebase+'.1'))
  else:
    return semver.bump_prerelease(version)

# -----
def bump_build(version):
  return semver.bump_build(semver.replace(version, build='test.0'))


# -----
if '__main__' == __name__:
  fname = '../version.yaml'
  print(emit_product_name(fname) + ' ' + emit_version(fname))
  print('bump pre   ==> ' + bump_pre(emit_version(fname)))
  print('bump build ==> ' + bump_build(emit_version(fname)))
