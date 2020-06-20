from tuuldevops.pipeline_steps import major_step


def test_major_step():
    major_step('a title', 'a description')
    assert True
