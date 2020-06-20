from pathlib import Path
from pytest import raises
import sh
from tempfile import TemporaryDirectory
from tuulbachs.exception import TuulError
from tuulfile.directory import cd
from tuulgit.check_status import has_staged_uncommitted, \
                                 has_unstaged_changes, \
                                 has_untracked_unignored_files, \
                                 is_clean_working_tree, \
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
            sh.git.add(fname)
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
            # modify the original file
            Path(fname).write_text('adsf')
            assert has_unstaged_changes()


def test_has_untracked_unignored_files():
    with TemporaryDirectory() as p:
        with cd(p):
            sh.git.init()
            assert not has_untracked_unignored_files()
            # add a file
            fname = './file.txt'
            Path(fname).touch()
            assert has_untracked_unignored_files()
            sh.git.add(fname)
            assert not has_untracked_unignored_files()
            # add a directory
            dname = 'adir'
            Path(dname).mkdir()
            assert not has_untracked_unignored_files()
            # add a file under that directory
            dfile = dname + '/another.txt'
            Path(dfile).touch()
            assert has_untracked_unignored_files()
            Path(dfile).unlink()
            assert not has_untracked_unignored_files()
            # add an ignored file
            sh.git.rm('--cached', fname)
            assert has_untracked_unignored_files()
            ignorename = './.gitignore'
            Path(ignorename).touch()
            Path(ignorename).write_text('file.txt')
            sh.git.add(ignorename)
            assert not has_untracked_unignored_files()


def test_is_clean_working_tree():
    with TemporaryDirectory() as p:
        with cd(p):
            sh.git.init()
            assert is_clean_working_tree()
            # add a file
            fname = './file.txt'
            Path(fname).touch()
            assert not is_clean_working_tree()
            sh.git.add(fname)
            assert not is_clean_working_tree()
            sh.git.commit('-m', 'dummy commit msg')
            assert is_clean_working_tree()
            # add a directory
            dname = 'adir'
            Path(dname).mkdir()
            assert is_clean_working_tree()
            # add a file under that directory
            dfile = dname + '/another.txt'
            Path(dfile).touch()
            assert not is_clean_working_tree()
