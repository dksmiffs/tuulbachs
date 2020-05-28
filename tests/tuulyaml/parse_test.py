"""pytest unit tests for the tuulyaml.parse module"""

from tuulyaml.parse import parse_yaml


def test_parse_yaml():
    """unit test parse_yaml"""
    cfg = parse_yaml('version.yaml')
    assert cfg['product_name'] == 'tuulbachs'
