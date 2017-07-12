from flask import json
from app.mod_data import mod_data
from app.mod_data.team.models import Team
from app import db

@mod_data.route('/team/create', methods=['POST'])
def createTeam():
    t = Team(name='Test Team 1')
    db.session.add(t)
    db.session.commit()

    return str(t)


@mod_data.route('/team/list', methods=['GET', 'POST'])
def getTeams():
    teams = Team.query.all()
    return json.dumps({'teams': [t.name for t in teams]})