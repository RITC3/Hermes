from flask import Blueprint, jsonify, request
from sqlalchemy.exc import SQLAlchemyError
from ..mod_auth import require_auth
from ..mod_db import db
from .models import Team

mod_team = Blueprint('team', __name__, url_prefix='/api/data/team')


@mod_team.route('/create', methods=['POST'])
@require_auth
def create_team():
    # if the team name was provided
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


@mod_team.route('/remove', methods=['POST'])
@require_auth
def remove_team():
    # if the team ID was provided
    team_id = request.form.get('id')
    if team_id is not None:
        try:
            team = Team.query.filter(Team.id == team_id).first()
            if team is not None:
                db.session.delete(team)
                db.session.commit()

                return jsonify({'success': True}), 200
        except SQLAlchemyError:
            db.session.rollback()

    return jsonify({'success': False}), 400


@mod_team.route('/update', methods=['POST'])
@require_auth
def update_team():
    # check if team ID and possible properties were given
    team_id = request.form.get('id')
    available_keys = [request.form.get(k) for k in ['name', 'score']]
    if team_id is not None and any(available_keys):
        name, score = available_keys

        # check that the team exists
        team = Team.query.filter(Team.id == team_id).first()
        if team is not None:
            # update the team name if provided
            if name is not None:
                team.name = name

            # update the score if provided
            if score is not None:
                # catch the exception for is score isn't a valid int
                try:
                    team.score = int(score)
                except ValueError:
                    pass

            db.session.commit()
            return jsonify({'success': True}), 200

    return jsonify({'success': False}), 400


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
