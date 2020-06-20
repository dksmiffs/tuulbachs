from pathlib import Path
import pytest
import sh
from tempfile import TemporaryDirectory
from tuulbachs.exception import TuulError
from tuulfile.directory import cd
import tuulgit.tag_commit


def test_tag_current():
    with TemporaryDirectory() as p:
        with cd(p):
            sh.git.init()
            atag = 'sometag'
            with pytest.raises(TuulError) as e_info:
                # tagging w/ no HEAD will raise
                tuulgit.tag_commit.tag_current(atag)
            # add a file
            fname = './file.txt'
            Path(fname).touch()
            with pytest.raises(TuulError) as e_info:
                # there's still no HEAD yet
                tuulgit.tag_commit.tag_current(atag)
            sh.git.add(fname)
            sh.git.commit('-m', 'first commit')
            tuulgit.tag_commit.tag_current(atag)  # finally, there's a HEAD
            # try to use the same tag again
            with pytest.raises(TuulError) as e_info:
                tuulgit.tag_commit.tag_current(atag)  # can't use same tag twice


def test_tag_current_signed(mocker):
    with TemporaryDirectory() as p:
        with cd(p):
            mocker.patch('tuulgit.tag_commit.__tag_current_helper')
            atag = 'sometag'
            tuulgit.tag_commit.tag_current_signed(atag)
            tuulgit.tag_commit.__tag_current_helper.assert_called_once_with(
              atag, '--sign')


def test_tag_delete_local():
    with TemporaryDirectory() as p:
        with cd(p):
            sh.git.init()
            atag = 'sometag'
            fname = './file.txt'
            Path(fname).touch()
            sh.git.add(fname)
            sh.git.commit('-m', 'first commit')
            tuulgit.tag_commit.tag_current(atag)
            # Delete the tag
            tuulgit.tag_commit.tag_delete_local(atag)
            # Try to delete the (now non-existent) same tag name
            with pytest.raises(TuulError) as e_info:
                tuulgit.tag_commit.tag_delete_local(atag)
