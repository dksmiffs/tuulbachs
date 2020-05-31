from pathlib import Path
from tempfile import TemporaryDirectory
from tuulfile.directory import cd
from tuulver.version import bump_build, \
                            bump_major, \
                            bump_minor, \
                            bump_patch, \
                            bump_pre, \
                            create_version_file, \
                            emit_product_name, \
                            emit_version


def test_create_version_file():
    with TemporaryDirectory() as p:
        with cd(p):
            fname = 'version.yaml'
            create_version_file(fname, 'justtestin')
            f = Path(fname)
            assert f.exists()


def test_emit_product_name():
    with TemporaryDirectory() as p:
        with cd(p):
            fname = 'version.yaml'
            prod = 'productname'
            create_version_file(fname, prod)
            assert emit_product_name(fname) == prod


def test_emit_version():
    with TemporaryDirectory() as p:
        with cd(p):
            fname = 'version.yaml'
            create_version_file(fname, 'whatever')
            assert emit_version(fname) == '0.0.0'


def test_bump_major():
    with TemporaryDirectory() as p:
        with cd(p):
            fname = 'version.yaml'
            create_version_file(fname, 'yup')
            bump_major(fname)
            assert emit_version(fname) == '1.0.0'


def test_bump_minor():
    with TemporaryDirectory() as p:
        with cd(p):
            fname = 'version.yaml'
            create_version_file(fname, 'yup')
            bump_minor(fname)
            assert emit_version(fname) == '0.1.0'


def test_bump_patch():
    with TemporaryDirectory() as p:
        with cd(p):
            fname = 'version.yaml'
            create_version_file(fname, 'yup')
            bump_patch(fname)
            assert emit_version(fname) == '0.0.1'


def test_bump_pre():
    with TemporaryDirectory() as p:
        with cd(p):
            fname = 'version.yaml'
            create_version_file(fname, 'yup')
            bump_pre(fname)
            assert emit_version(fname) == '0.0.0-pre.1'


def test_bump_build():
    with TemporaryDirectory() as p:
        with cd(p):
            fname = 'version.yaml'
            create_version_file(fname, 'yup')
            bump_pre(fname)
            bump_build(fname)
            assert emit_version(fname) == '0.0.0-pre.1+build.1'
            bump_pre(fname)
            bump_build(fname)
            assert emit_version(fname) == '0.0.0-pre.2+build.1'
