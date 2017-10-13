from ..mod_db import db
from binascii import hexlify
import scrypt
import os


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), unique=True)
    username = db.Column(db.String(32), unique=True)
    password_hash = db.Column(db.String(128))
    salt = db.Column(db.String(16))
    email = db.Column(db.String(64), unique=True)

    def __init__(self, name, username, password, email):
        self.name = name
        self.username = username
        self.email = email

        salt = os.urandom(8)
        self.salt = hexlify(salt)
        self.password_hash = hexlify(scrypt.hash(password, salt))

    def __repr__(self):
        return f'<Team name="{self.name}" score={self.score}>'
