import configparser
import sys

config_file = sys.path[1] + "/tests/config/qa.ini"

config = configparser.ConfigParser()
config.read(config_file)


def get_gmail_url():
    return config['gmail']['url']


def get_gmail_user():
    return config['gmail']['user']


def get_gmail_pass():
    return config['gmail']['pass']

print(config_file)
print(get_gmail_user())
