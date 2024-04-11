import os

class Config(object):
    APP_NAME = os.getenv('APP_NAME')
    AUTHOR = os.getenv('AUTHOR')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # Connect to the MYSQL database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')