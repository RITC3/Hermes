from flask import Blueprint, jsonify, request
from sqlalchemy.exc import SQLAlchemyError
from ..mod_auth import require_auth
from ..mod_db import db
from .models import User

mod_user = Blueprint('user', __name__, url_prefix='/api/data/user')


@mod_user.route('/create', methods=['POST'])
@require_auth
def create_user():
    service_params = [request.form.get(k) for k in ['name', 'username', 'password', 'email']]

    # check that all the necessary params have been provided and contain a value
    if all(service_params):
        # expand out into variables
        name, username, password, email = service_params

        # try to add it into the DB
        try:
            user = User(name=name, username=username, password=password, email=email)
            db.session.add(user)
            db.session.commit()

            return jsonify({'success': True, 'id': user.id})
        except SQLAlchemyError:
            db.session.rollback()
            pass

    return jsonify({'success': False}), 400


@mod_user.route('/remove', methods=['POST'])
@require_auth
def remove_user():
    # if the user ID was provided
    user_id = request.form.get('id')
    if user_id:
        try:
            user = User.query.filter(User.id == user_id).first()
            if user is not None:
                db.session.delete(user)
                db.session.commit()

                return jsonify({'success': True}), 200
        except SQLAlchemyError:
            db.session.rollback()

    return jsonify({'success': False}), 400


@mod_user.route('/list', methods=['GET', 'POST'])
@require_auth
def list_users():
    users = User.query.all()
    return jsonify({
        'users': [{
            'id': u.id,
            'name': u.name,
            'username': u.username,
            'email': u.email
        } for u in users]
    })
