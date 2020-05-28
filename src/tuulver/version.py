"""
version.py
==================
Utility functions for managing a tuulbachs-formatted version YAML file
"""

import semver
from tuuldevops.update_version import update_product_version
from tuulyaml.parse import parse_yaml


# -----
def create_version_file(filename, product_name):
    """
    Create an initial tuulbachs-formatted version YAML file
    """
    out = open(filename, 'w')
    print('# tuulbachs-formatted version file', file=out)
    print('product_name: ' + product_name, file=out)
    print('version: 0.0.0', file=out)
    out.close()


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
    update_product_version(filename, str(v.bump_major()))


# -----
def bump_minor(filename):
    """
    Bump the minor portion of the version from the input YAML filename
    """
    v = semver.VersionInfo.parse(emit_version(filename))
    update_product_version(filename, str(v.bump_minor()))


# -----
def bump_patch(filename):
    """
    Bump the patch portion of the version from the input YAML filename
    """
    v = semver.VersionInfo.parse(emit_version(filename))
    update_product_version(filename, str(v.bump_patch()))


# -----
def bump_pre(filename, prebase='pre'):
    """
    Bump the "pre" portion of the version from the input YAML filename
    """
    v = semver.VersionInfo.parse(emit_version(filename))
    if v.prerelease is None:
        new_ver = str(v.replace(prerelease=prebase+'.1'))
    else:
        new_ver = str(v.bump_prerelease(token=prebase))
    update_product_version(filename, new_ver)


# -----
def bump_build(filename):
    """
    Bump the "build" portion of the version from the input YAML filename
    """
    v = semver.VersionInfo.parse(emit_version(filename))
    if v.build is None:
        new_ver = str(v.replace(build='build.1'))
    else:
        new_ver = str(v.bump_build())
    update_product_version(filename, new_ver)


# -----
if '__main__' == __name__:
    fname = '../../version.yaml'
    print(emit_product_name(fname) + ' ' + emit_version(fname))
