from app import db

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement='auto')
    name = db.Column(db.String(128), unique=True)
    score = db.Column(db.Integer, default=0)

    def __init__(self, name, score=0):
        self.name = name
        self.score = score

    def __repr__(self):
        return f'<Team name="{self.name}" score={self.score}>'