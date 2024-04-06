import os

class Config(object):
    APP_NAME = os.getenv('APP_NAME')
    AUTHOR = os.getenv('AUTHOR')