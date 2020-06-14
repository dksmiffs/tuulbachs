from pathlib import Path
from pytest import raises
import sh
from tempfile import TemporaryDirectory
from tuulbachs.exception import TuulError
from tuulfile.directory import cd
from tuulgit.check_status import has_staged_uncommitted, \
                                 has_unstaged_changes, \
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


def test_has_unstaged_changes():
    with TemporaryDirectory() as p:
        with cd(p):
            sh.git.init()
            assert not has_unstaged_changes()
            # add a file
            fname = './file.txt'
            Path(fname).touch()
            assert has_unstaged_changes()
            sh.git.add(fname)
            assert not has_unstaged_changes()
            sh.git.commit('-m', 'first commit')
            assert not has_unstaged_changes()
            # add a directory
            dname = 'adir'
            Path(dname).mkdir()
            assert not has_unstaged_changes()
            # add a file under that directory
            dfile = dname + '/another.txt'
            Path(dfile).touch()
            assert has_unstaged_changes()
            Path(dfile).unlink()
            assert not has_unstaged_changes()
            Path(dname).rmdir()
            assert not has_unstaged_changes()
            # modify the original file
            Path(fname).write_text('adsf')
            assert has_unstaged_changes()
