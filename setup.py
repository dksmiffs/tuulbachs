# trick to install package needed by setup.py itself found here:
#    https://stackoverflow.com/a/49817738
import pip
pip.main(['install', 'PyYAML'])

from distutils.core import setup
from version        import emit_version

setup(
  name='tuulbachs',
  version=emit_version(),
  long_description=open('README.md').read(),
)
