from pytest import mark


def test_env_is_qa(app_config):
    assert app_config.base_url == "http://qa-env.com"
    assert app_config.app_port == 80


@mark.skip(reason="broken test")
def test_env_is_dev(app_config):
    assert app_config.base_url == "http://dev-env.com"
    assert app_config.app_port == 8080
