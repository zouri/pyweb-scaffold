# -*- coding:utf-8 -*-
#
# Created Time: 2020/1/4 11:15 上午
# Be From: ZouRi 
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#


class BaseConfig:
    SECRET_KEY = 'XMncH3QWSBxegQSv5'
    ITEMS_PER_PAGE = 10
    HOST = '127.0.0.1'
    PORT = 8080

    # don't need to login
    URL_WHITE_LIST = [
        '/apps/api/user/login',
        '/apps/api/verify/img',
        '/apps/api/user',
    ]

    URL_BLACK_LIST = []
    IP_BLACK_LIST = []

    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    # mysql
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/website'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # redis
    REDIS_URL = 'redis://:@127.0.0.1:6379/0'
    # 日志
    LOG_NAME = 'server-test.log'
    LOG_DIR = './'
    LOG_LEVEL = 'DEBUG'
    LOG_FORMAT = '[%(asctime)s %(processName)s %(threadName)s %(levelname)s]: %(message)s'

    # 上传文件配置
    UPLOAD_PATH = '/Users/sun/Project/project-template/website-template/background/static/upload_file/'


class TestingConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/website'
    # 日志
    LOG_NAME = 'server-test.log'
    LOG_DIR = './'
    LOG_LEVEL = 'DEBUG'
    LOG_FORMAT = '[%(asctime)s %(processName)s %(threadName)s %(levelname)s]: %(message)s'
    UPLOAD_PATH = '/opt/website/pyweb/background/static/upload_file/'


class ProductionConfig(BaseConfig):
    DEBUG = False
    # mysql
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://staff:dESC3UWFYwPJKyK6P@127.0.0.1:3306/website'
    # redis
    REDIS_URL = 'redis://:@127.0.0.1:6379/0'
    # 日志
    LOG_NAME = 'server-test.log'
    LOG_DIR = './'
    LOG_LEVEL = 'INFO'
    LOG_FORMAT = '[%(asctime)s %(processName)s %(threadName)s %(levelname)s]: %(message)s'
    UPLOAD_PATH = '/opt/website/pyweb/background/static/upload_file/'

    # 上传文件配置
    UPLOAD_PATH = '/Users/sun/Project/project-template/website-template/background/static/upload_file/'

config = {
    'default': DevelopmentConfig,
    'dev': DevelopmentConfig,
    'test': TestingConfig,
    'prod': ProductionConfig
}



