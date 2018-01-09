from os import path

# Base directory
BASE_DIR = path.abspath(path.dirname(__file__))


class Config:
    # Application threads
    THREADS_PER_PAGE = 2

    # Secret key for application
    SECRET_KEY = b'\x9c\xbb\xaa\xe5\x8f\xa3\xf0\x94\xb9\xf8\xea\x96&7\xbb\xa4\xa9\x85i\xf5\xb4\x9f\xd8\xaf\xef\xbc\xd0E\xe66\x98\xad'

    # No need for modification tracking events
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Debug(Config):
    # Enable debugging features
    DEBUG = True

    SQLITE_FILE = 'hermes.db'
    SQLITE_PATH = path.join(BASE_DIR, SQLITE_FILE)

    # SQLAlchemy config
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{SQLITE_PATH}'


class Production(Config):
    # SQLAlchemy config
    SQL_USER = 'user'
    SQL_PASS = 'password'
    SQL_HOST = 'hostname'
    SQL_PORT = '3306'
    SQL_DB   = 'db_name'

    SQLALCHEMY_DATABASE_URI = f'mysql://{SQL_USER}:{SQL_PASS}@{SQL_HOST}:{SQL_PORT}/{SQL_DB}'
