from pathlib import Path
from tuulfile.directory import cd


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
