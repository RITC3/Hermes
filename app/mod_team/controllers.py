from flask import Blueprint, jsonify, request, session
from sqlalchemy.exc import SQLAlchemyError
from logging import getLogger
from ..mod_auth import require_auth
from ..mod_db import db
from .models import Team

mod_team = Blueprint('team', __name__, url_prefix='/api/data/team')
logger = getLogger(__name__)


# TODO: username validation on this endpoint
@mod_team.route('/create', methods=['POST'])
@require_auth
def create_team():
    if session.get('_admin', False):
        # if the team name was provided
        body_params = [request.form.get(f) for f in ['username', 'password']]
        if all(body_params):
            username, password = body_params

            try:
                team = Team(username=username, password=password)
                db.session.add(team)
                db.session.commit()

                return jsonify({'success': True, 'id': team.id})
            except SQLAlchemyError:
                db.session.rollback()

        return jsonify({'success': False}), 400

    return jsonify({'success': False}), 401


@mod_team.route('/remove', methods=['POST'])
@require_auth
def remove_team():
    # unauthorized if not an admin
    return_code = 401

    # only an admin can remove teams
    if session.get('_admin', False):
        # if the team ID was provided
        team_id = request.form.get('id')
        if team_id is not None:
            try:
                team = Team.query.filter(Team.id == team_id).first()
                if team is not None:
                    db.session.delete(team)
                    db.session.commit()

                    return jsonify({'success': True}), 200
            except SQLAlchemyError as e:
                # log the exception
                logger.exception(e)
                db.session.rollback()

        # bad request if something went wrong
        return_code = 400

    return jsonify({'success': False}), return_code


@mod_team.route('/update', methods=['POST'])
@require_auth
def update_team():
    team_id = None
    is_admin = session.get('_admin', False)

    # check that the team ID is available from args or the session data
    if is_admin:
        team_id = request.form.get('team_id')
    elif '_team' in session:
        team_id = session['_team']

    # check if team ID and possible properties were given
    avail_args = [request.form.get(k) for k in ['username', 'old_password', 'new_password']]
    if team_id is not None and any(avail_args):
        username, old_password, new_password = avail_args

        # check that the team exists
        team = Team.query.filter(Team.id == team_id).first()
        if team is not None:
            # update the username if provided
            if username is not None:
                team.username = username

            # update the password if provided
            if new_password is not None:
                # check that the old password has been provided and matches the current pass
                # or that the caller is an admin
                if is_admin or (old_password is not None and team.check_password(old_password)):
                    team.password = Team.hash_password(new_password)
                    # remove the team ID session to force the user to log back in after a password change
                    session.pop('_team', None)
                else:
                    logger.error('Old password did not match and caller is not an admin!')
                    db.session.rollback()
                    return jsonify({'success': False}), 400

            db.session.commit()
            return jsonify({'success': True}), 200

    return jsonify({'success': False}), 400


@mod_team.route('/list', methods=['GET', 'POST'])
@require_auth
def get_teams():
    # check if requester is an admin
    if session.get('_admin', False):
        teams = Team.query.all()
        return jsonify({
            'teams': [{
                'id': t.id,
                'username': t.username
            } for t in teams]
        })

    return jsonify({'success': False}), 401


@mod_team.route('/login', methods=['POST'])
def team_login():
    return_code = 400

    # check all params
    body_params = [request.form.get(k) for k in ['username', 'password']]
    if all(body_params):
        # expand
        username, password = body_params

        # get the team with the matching username
        team = Team.query.filter(Team.username == username).first()
        if team.check_password(password):
            session['_team'] = team.id
            return jsonify({'success': True})
        else:
            logger.error('Invalid password for team %s', team.username)
            return_code = 401

    return jsonify({'success': False}), return_code
