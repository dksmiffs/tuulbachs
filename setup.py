from distutils.core import setup
from version        import emit_version

setup(
  name='tuulbachs',
  version=emit_version(),
  packages=['python',],
  long_description=open('README.md').read(),
)
