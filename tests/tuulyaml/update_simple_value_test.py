import os
from tuulyaml.parse import parse_yaml
from tuulyaml.update_simple_value import update_value


def test_update_value():
    """unit test update_value"""
    fname = '/tmp/update_value_test123.yaml'
    out = open(fname, 'w')
    print('foo: bar', file = out)
    out.close()
    update_value(fname, 'foo', '123')
    data = parse_yaml(fname)
    assert data['foo'] == '123'
    os.remove(fname)
