"""
Git tag the commit on the current branch, *only if* the working tree is clean
"""

import sh
from tuulbachs.exception import TuulError
from tuulgit.check_status import is_clean_working_tree


# -----
def __tag_current_helper(tag, option):
    if not is_clean_working_tree():
        raise TuulError('tag not allowed on unclean working tree')
    else:
        try:
            sh.git.tag(option, '-m', '"tuulgit-generated tag"', tag)
        except sh.ErrorReturnCode_128:
            raise TuulError('Is HEAD a valid reference in your git repo?')


# -----
def tag_current(tag):
    """
    Git tag (annotated) the current commit from a clean working tree

    :raises TuulError: when the caller attempts to tag an unclean working tree
        or to use a tag that already exists on the repo
    """
    __tag_current_helper(tag, '--annotate')


# -----
def tag_current_signed(tag):
    """
    Git tag (signed) the current commit from a clean working tree

    :raises TuulError: when the caller attempts to tag an unclean working tree
        or to use a tag that already exists on the repo
    """
    __tag_current_helper(tag, '--sign')


# -----
def tag_delete_local(tag):
    """
    Delete the named Git tag (local only).  This function does *not* delete
    remote tags

    :raises TuulError: if the tag delete fails
    """
    try:
        sh.git.tag('-d', tag)
    except sh.ErrorReturnCode_1:
        raise TuulError('Did you attempt to delete a non-existent tag?')
