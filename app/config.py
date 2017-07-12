from os import path

# Enable debugging features
DEBUG = True

# Base directory
BASE_DIR = path.abspath(path.dirname(__file__))


# SQLAlchemy config
SQLALCHEMY_DATABASE_URI = f'sqlite:///{path.join(BASE_DIR, "hermes.db")}'
SQLALCHEMY_TRACK_MODIFICATIONS = False
DATABASE_CONNECT_OPTIONS = {}


# Application threads
THREADS_PER_PAGE = 2


# Secret key for application
SECRET_KEY = b'\x9c\xbb\xaa\xe5\x8f\xa3\xf0\x94\xb9\xf8\xea\x96&7\xbb\xa4\xa9\x85i\xf5\xb4\x9f\xd8\xaf\xef\xbc\xd0E\xe66\x98\xad'