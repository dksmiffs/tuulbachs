from pathlib import Path
from pytest import raises
import sh
from tempfile import TemporaryDirectory
from tuulbachs.exception import TuulError
from tuulfile.directory import cd
from tuulgit.check_status import has_staged_uncommitted, \
                                 is_working_tree, \
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


def test_has_staged_uncommitted():
    with TemporaryDirectory() as p:
        with cd(p):
            sh.git.init()
            assert not has_staged_uncommitted()
            fname = './file.txt'
            Path(fname).touch()
            assert not has_staged_uncommitted()
            sh.git.add('./file.txt')
            assert has_staged_uncommitted()
            sh.git.commit('-m', 'first commit')
            assert not has_staged_uncommitted()
