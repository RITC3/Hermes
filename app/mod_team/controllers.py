from flask import Blueprint, jsonify, request
from sqlalchemy.exc import SQLAlchemyError
from ..mod_auth import require_auth
from ..mod_db import db
from .models import Team

mod_team = Blueprint('team', __name__, url_prefix='/api/data/team')


@mod_team.route('/create', methods=['POST'])
@require_auth
def create_team():
    # get the 'name' field from the POST form data
    name = request.form.get('name')
    if name:
        # if the name was sent
        try:
            team = Team(name=name)
            db.session.add(team)
            db.session.commit()

            return jsonify({'success': True, 'id': team.id})
        except SQLAlchemyError:
            db.session.rollback()

    return jsonify({'success': False}), 400


@mod_team.route('/remove', methods=['GET', 'POST'])
@require_auth
def remove_team():
    team_id = request.form.get('id')
    if id:
        try:
            team = Team.query()

@mod_team.route('/list', methods=['GET', 'POST'])
@require_auth
def get_teams():
    teams = Team.query.all()
    return jsonify({
        'teams': [{
            'id': t.id,
            'name': t.name,
            'score': t.score
        } for t in teams]
    })
