from tuulbachs.exception import TuulError


def test_TuulError():
    a = TuulError()
    b = TuulError('with a message')
    assert True;
