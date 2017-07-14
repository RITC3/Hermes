from app import db
from os import urandom
from binascii import hexlify

class Auth(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement='auto')
    name = db.Column(db.String(128), unique=True, nullable=False)
    api_key = db.Column(db.String(32), unique=True, nullable=False)

    def __init__(self, name, apiKey=None):
        self.name = name
        self.api_key = apiKey if apiKey is not None else hexlify(urandom(32))

    def __repr__(self):
        return f'<Auth name="{self.name}" api_key="{self.api_key}">'