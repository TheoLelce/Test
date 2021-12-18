import os, binascii

basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):
    SECRET_KEY = binascii.hexlify(os.urandom(24))
    DEBUG = True
    ENV = "development"
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'users.db')
