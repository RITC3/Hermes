from ..mod_db import db
from passlib.hash import argon2


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), unique=True)
    username = db.Column(db.String(32), unique=True)
    password = db.Column(db.String(128))

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = argon2.using(time_cost=160, memory_cost=10240, parallelism=8).hash(password)

    def __repr__(self):
        return f'<User name="{self.name}" username="{self.username}">'
