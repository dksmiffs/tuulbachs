"""
tag_current_version.py
===============================
Git tag the commit on the current branch with the current version of this
software
"""

from tuulgit.tag_commit  import tag_current
from tuulver.version     import emit_version


# -----
def tag_product_version(conf_filename):
  """
  Git tag the commit on the current branch with the version of this software
  given in conf_filename
  """
  tag_current(emit_version(conf_filename))


# -----
def main():
  # Show example usage
  tag_product_version('../version.yaml')


# -----
if '__main__' == __name__:
  main()
