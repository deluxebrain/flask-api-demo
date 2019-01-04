import logging.config
import os

class Config(object):
    SERVER_NAME = '127.0.0.1:5000'
    LOGGING_CONFIG_FILE = 'logging-config.ini'

    @classmethod
    def init_app(cls, app):
        logging_config_path = os.path.normpath(
            os.path.join(
                os.path.dirname(__file__), cls.LOGGING_CONFIG_FILE))
        logging.config.fileConfig(logging_config_path)

class DevelopmentConfig(Config):
    DEBUG = True

config_map = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}

