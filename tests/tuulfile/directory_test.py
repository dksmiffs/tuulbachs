"""pytest unit tests"""

from pathlib import Path
from shutil import rmtree
from tuulfile.directory import cd, create_tmp_dir


def test_cd():
    old = Path.cwd()
    with cd('/tmp'):
        assert Path.cwd != old
        p = Path('./hellew.txt')
        p.touch()
        assert p.exists()
        p.unlink()
        assert not p.exists()
    assert Path.cwd() == old


def test_create_tmp_dir():
    """unit test create_tmp_dir"""
    tmp = create_tmp_dir()
    p = Path(tmp)
    assert p.exists()
    rmtree(tmp)
    assert not p.exists()
