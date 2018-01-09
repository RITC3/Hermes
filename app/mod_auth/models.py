from ..mod_db import db
from os import urandom
from binascii import hexlify


class Auth(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    api_key = db.Column(db.String(32), unique=True, nullable=False)

    def __init__(self, name, api_key=None):
        # used for key association
        self.name = name

        # default to a random, 32-character long API key if one is not explicitly provided
        self.api_key = api_key if api_key is not None else hexlify(urandom(32))

    def __repr__(self):
        return f'<Auth name="{self.name}" api_key="{self.api_key}">'
