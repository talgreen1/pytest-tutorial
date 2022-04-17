class Config:
    def __init__(self, env):

        SUPPORTED_ENVS = ['dev', 'qa']

        if env.lower() not in SUPPORTED_ENVS:
            raise Exception(f'{env} is not a supported environment. Supported envs: {SUPPORTED_ENVS}')

        self.base_url = {
            'dev': "http://dev-env.com",
            'qa': "http://qa-env.com",
        }[env]

        self.app_port = {
            'dev': 8080,
            'qa': 80
        }[env]