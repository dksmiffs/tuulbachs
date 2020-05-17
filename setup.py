# trick to install package needed by setup.py itself found here:
#    https://stackoverflow.com/a/49817738
import pip
pip.main(['install', 'PyYAML'])

import os
from   setuptools      import setup, find_packages
import sys

# follow https://github.com/pyca/cryptography's model for placing packages in
#    src subdirectory
base_dir = os.path.dirname(__file__)
src_dir = os.path.join(base_dir, 'src')
sys.path.insert(0, src_dir)

from   tuulver.version import emit_version

setup(
  name='tuulbachs',
  version=emit_version('version.yaml'),
  long_description=open('README.md').read(),
  package_dir={'': 'src'},
  packages=find_packages(where='src'),
  setup_requires=['wheel']
)
