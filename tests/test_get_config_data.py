from utils.ConfigFileParser import ConfigFileParser

config = ConfigFileParser('qa.ini')


def test_get_gmail_url():
    print(config.get_gmail_url())
