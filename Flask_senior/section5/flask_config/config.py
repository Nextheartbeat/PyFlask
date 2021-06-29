# TODO: 从对象中加载配置
from datetime import timedelta


class BaseConfig():
    SECRET_KEY = 'test'
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)


class Development(BaseConfig):
    """开发环境"""
    ENV = 'development'


class Production(BaseConfig):
    """开发环境"""
    ENV = 'production'
