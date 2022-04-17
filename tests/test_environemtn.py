def test_env_is_qa(app_config):
    assert app_config.base_url == "http://qa-env.com"


def test_env_is_dev(app_config):
    assert app_config.base_url == "http://dev-env.com"
