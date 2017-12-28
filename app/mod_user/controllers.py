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
    if user_id is not None:
        try:
            user = User.query.filter(User.id == user_id).first()
            if user is not None:
                db.session.delete(user)
                db.session.commit()

                return jsonify({'success': True}), 200
        except SQLAlchemyError:
            db.session.rollback()

    return jsonify({'success': False}), 400


@mod_user.route('/update', methods=['POST'])
@require_auth
def update_user():
    # check if user ID and possible properties were given
    user_id = request.form.get('id')
    available_keys = [request.form.get(k) for k in ['name', 'email']]
    if user_id is not None and any(available_keys):
        name, email = available_keys

        # check that the user exists
        user = User.query.filter(User.id == user_id).first()
        if user is not None:
            # update name if provided
            if name is not None:
                # ensure that the name is not already in use
                if User.query.filter(User.name == name).count() == 0:
                    user.name = name

            # update email if provided
            if email is not None:
                # ensure that the email is not already in use
                if User.query.filter(User.email == email).count() == 0:
                    user.email = email

            db.session.commit()
            return jsonify({'success': True}), 200

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
