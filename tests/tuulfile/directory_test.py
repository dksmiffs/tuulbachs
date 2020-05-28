"""pytest unit tests for the tuulfile.directory module"""

from os import path
from shutil import rmtree
from tuulfile.directory import create_tmp_dir


def test_create_tmp_dir():
    """unit test create_tmp_dir"""
    tmp = create_tmp_dir()
    assert path.exists(tmp) 
    rmtree(tmp)
    assert not path.exists(tmp)
