import configparser
import sys


class ConfigFileParser():
    cfg_file = 'qa.ini'
    cfg_path = sys.path[1] + "/tests/config/"
    config = configparser.ConfigParser()

    def __init__(self, cfg=cfg_path):
        self.cfg_file = cfg
        self.config.read(self.cfg_path + self.cfg_file)

    def get_gmail_url(self):
        return self.config['gmail']['url']

    def get_gmail_user(self):
        return self.config['gmail']['user']

    def get_gmail_pass(self):
        return self.config['gmail']['pass']


if __name__ == '__main__':
    config = ConfigFileParser('qa.ini')
    print(config.get_gmail_user())
