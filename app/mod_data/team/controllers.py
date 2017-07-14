from flask import jsonify, request
from sqlalchemy.exc import SQLAlchemyError
from app.mod_data import mod_data
from app.mod_data.team.models import Team
from app import db
from app.mod_auth import require_auth

@mod_data.route('/team/create', methods=['POST'])
@require_auth
def createTeam():
    name = request.form.get('name')
    if name:
        try:
            team = Team(name=name)
            db.session.add(team)
            db.session.commit()

            return jsonify({'success': True, 'id': team.id})
        except SQLAlchemyError:
            db.session.rollback()

    return jsonify({'success': False}), 400

@mod_data.route('/team/list', methods=['GET', 'POST'])
@require_auth
def getTeams():
    teams = Team.query.all()
    return jsonify({
        'teams': [{
            'id': t.id,
            'name': t.name,
            'score': t.score
        } for t in teams]
    })