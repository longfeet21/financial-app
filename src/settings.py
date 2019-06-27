import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\x97\xfc\x10\x021xLCX\x92\x16\xa4\xb47D\xa2'
DEBUG = True
