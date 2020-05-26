"""
check_status.py
===============================
Check the status of the local git working tree
"""

# Guidance:  https://stackoverflow.com/a/2659808

from io import StringIO
import sh
from tuulbachs.exception import TuulError


def is_working_tree():
    """
    Check if this is a git working tree at all

    :raises TuulError: when the caller attempts to use this function outside of
        a git working tree
    """
    try:
        sh.git.status()
    except sh.ErrorReturnCode_128:
        raise TuulError('There is no git working tree here')


def repo_toplevel_path():
    """
    Return a string containing the path of the repo's top-level directory
    """
    buf = StringIO()
    # Guide:  https://stackoverflow.com/a/957978
    sh.git('rev-parse', '--show-toplevel', _out=buf)
    return buf.getvalue().rstrip()


def has_staged_uncommitted():
    """
    Return a boolean indicating whether the repository has staged, but
    uncommitted changes
    """
    try:
        sh.git('diff-index', '--quiet', '--cached', 'HEAD', '--')
        return False
    except sh.ErrorReturnCode_1:
        return True


def has_unstaged_changes():
    """
    Return a boolean indicating whether the working tree has unstaged changes
    """
    try:
        sh.git('diff-files', '--quiet', '--')
        return False
    except sh.ErrorReturnCode_1:
        return True


def has_untracked_unignored_files():
    """
    Return a boolean indicating whether the working tree has untracked,
    unignored files
    """
    top = repo_toplevel_path()
    try:
        # Guide: https://stackoverflow.com/a42884225
        sh.grep(sh.git('ls-files', top, '--exclude-standard', '--others'),
                '-q', '^')
        return True
    except sh.ErrorReturnCode_1:
        return False


def is_clean_working_tree(check_if_working_tree=True):
    """
    Return a boolean indicating whether the Git working tree is clean or not
    """
    if check_if_working_tree:
        is_working_tree()
    return not has_untracked_unignored_files() and \
        not has_unstaged_changes() and \
        not has_staged_uncommitted()


def main():
    # Show example usage
    if is_clean_working_tree():
        print('clean')
    else:
        print('NOT clean')


# -----
if '__main__' == __name__:
    main()
