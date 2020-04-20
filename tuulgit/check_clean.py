"""
check_clean.py
===============================
Check the Git working tree
"""

from tuulpy.subprocess import subpResult


def is_clean_working_tree():
  """
  Return a boolean indicating whether the Git working tree is clean or not
  """
  dirty = subpResult.run('git status --porcelain')
  return not dirty  


def main():
  # Show example usage
  if is_clean_working_tree():
    print('clean')
  else:
    print('NOT clean')


# -----
if '__main__' == __name__:
  main()
