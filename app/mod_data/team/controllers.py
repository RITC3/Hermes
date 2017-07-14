from flask import jsonify, request
from app.mod_data import mod_data
from app.mod_data.team.models import Team
from app import db
from app.mod_auth import require_auth

@mod_data.route('/team/create', methods=['POST'])
@require_auth
def createTeam():
    return jsonify(request.data)

@mod_data.route('/team/list', methods=['GET', 'POST'])
@require_auth
def getTeams():
    teams = Team.query.all()
    return jsonify({
        'teams': [t.name for t in teams]
    })