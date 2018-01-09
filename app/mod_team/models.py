from ..mod_db import db
from passlib.hash import argon2


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(32), unique=True)
    password = db.Column(db.String(128))

    def __init__(self, username, password):
        self.username = username
        self.password = Team.hash_password(password)

    def __repr__(self):
        return f'<Team name="{self.name}" score={self.score}>'

    @staticmethod
    def hash_password(password):
        return argon2.using(time_cost=160, memory_cost=10240, parallelism=8).hash(password)

    # compare the given password to the stored hash
    def check_password(self, password):
        return argon2.verify(password, self.password)
