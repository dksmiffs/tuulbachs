"""
tag_commit.py
===============================
Git tag the commit on the current branch, *only if* the working tree is clean
"""

import re
from   tuulbachs.exception import TuulError
from   tuulgit.check_clean import is_clean_working_tree
from   tuulpy.subprocess   import subpResult


# -----
def tag_current(tag):
  """
  Git tag (annotated) the current commit from a clean working tree

  :raises TuulError: when the caller attempts to tag an unclean working tree
      or to use a tag that already exists on the repo
  """
  if not is_clean_working_tree():
    raise TuulError('tag not allowed on unclean working tree')
  else:
    res = subpResult.run('git tag --annotate -m "annotated tag" ' + tag)
    if re.search(b'^fatal.*already exists$', res):
      raise TuulError('cannot apply tag that already exists in the repo')


# -----
def tag_delete_local(tag):
  """
  Delete the named Git tag (local only).  This function does *not* delete
  remote tags

  :raises TuulError: if the tag delete fails
  """
  res = subpResult.run('git tag -d ' + tag)
  if re.search(b'^error', res):
    raise TuulError('failed to delete tag')


# -----
def main():
  # Show example usage
  try:
    atag = 'temptag'
    tag_current(atag)
    print('tag successful')
    try:
      tag_current(atag)
    except TuulError:
      print('reusing same tag failed as expected')
    tag_delete_local(atag)
    print('delete tag successful')
    try:
      tag_delete_local(atag)
    except TuulError:
      print('deleting non-existent tag failed as expected')
  except TuulError as e:
    raise e


# -----
if '__main__' == __name__:
  main()
