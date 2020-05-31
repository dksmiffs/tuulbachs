"""pytest unit tests"""

from pytest import raises
import sh
from tempfile import TemporaryDirectory
from tuulbachs.exception import TuulError
from tuulfile.directory import cd
from tuulgit.check_status import is_working_tree, \
                                 repo_toplevel_path


def test_is_working_tree():
    # non working tree
    with cd('/tmp'):
        with raises(TuulError) as excinfo:
            is_working_tree()
        assert 'no git working tree' in str(excinfo.value)
    # working tree
    with TemporaryDirectory() as p:
        with cd(p):
            sh.git.init()
            is_working_tree()  # should not raise
            assert True


def test_repo_toplevel_path():
    with TemporaryDirectory() as p:
        with cd(p):
            sh.git.init()
            assert repo_toplevel_path() == p
