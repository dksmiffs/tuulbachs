import os
import pip
from setuptools import setup, find_packages
import sys

# trick to install package needed by setup.py itself found here:
#    https://stackoverflow.com/a/49817738
pip.main(['install', 'PyYAML'])

# follow https://github.com/pyca/cryptography's model for placing packages in
#    src subdirectory
base_dir = os.path.dirname(__file__)
src_dir = os.path.join(base_dir, 'src')
sys.path.insert(0, src_dir)

from tuulver.version import emit_version  # noqa: E402

setup(
  name='tuulbachs',
  version=emit_version('version.yaml'),
  long_description=open('README.md').read(),
  package_dir={'': 'src'},
  packages=find_packages(where='src'),
  setup_requires=['wheel']
)
