import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'romko'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql://postgres:postgres@localhost:5432/text'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
