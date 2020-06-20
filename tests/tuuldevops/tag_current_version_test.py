import tuuldevops.tag_current_version


def test_fnname(mocker):
    mocker.patch('tuuldevops.tag_current_version.tag_current_signed')
    mocker.patch('tuuldevops.tag_current_version.emit_version')
    fname = 'whatevs'
    tuuldevops.tag_current_version.tag_product_version(fname)
    tuuldevops.tag_current_version.emit_version.assert_called_once_with(fname)
    tuuldevops.tag_current_version.tag_current_signed.assert_called_once()
