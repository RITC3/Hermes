from ..mod_db import db
import hashlib


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), unique=True)
    username = db.Column(db.String(32), unique=True)
    password_hash = db.Column(db.String(64))
    email = db.Column(db.String(64), unique=True)

    def __init__(self, name, username, password, email):
        self.name = name
        self.username = username
        self.password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
        self.email = email

    def __repr__(self):
        return f'<Team name="{self.name}" score={self.score}>'
