from flask import Blueprint, jsonify, request
from sqlalchemy.exc import SQLAlchemyError
from ..mod_auth import require_auth
from ..mod_db import db
from .models import Service
from ..mod_check import MySQL, FTP

mod_service = Blueprint('service', __name__, url_prefix='/api/data/service')


@mod_service.route('/create', methods=['POST'])
@require_auth
def create_service():
    service_params = [request.form.get(k) for k in ['name', 'host', 'port', 'type']]

    # check that all the necessary params have been provided and contain a value
    if all(service_params):
        # expand out into variables
        name, host, port, service_type = service_params

        # try to add it into the DB
        try:
            service = Service(name=name, host=host, port=int(port), service_type=service_type)
            db.session.add(service)
            db.session.commit()

            return jsonify({'success': True, 'id': service.id})
        except (SQLAlchemyError, TypeError):
            # catch TypeError in case the int conversion fails
            db.session.rollback()
            pass

    return jsonify({'success': False}), 400


@mod_service.route('/remove', methods=['POST'])
@require_auth
def remove_service():
    # if the service ID was provided
    service_id = request.form.get('id')
    if service_id is not None:
        try:
            service = Service.query.filter(Service.id == service_id).first()
            if service is not None:
                db.session.delete(service)
                db.session.commit()

                return jsonify({'success': True}), 200
        except SQLAlchemyError:
            db.session.rollback()

    return jsonify({'success': False}), 400


@mod_service.route('/update', methods=['POST'])
@require_auth
def update_service():
    # check if service ID and possible properties were given
    service_id = request.form.get('id')
    available_keys = [request.form.get(k) for k in ['name', 'host', 'port', 'type']]
    if service_id is not None and any(available_keys):
        name, host, port, service_type = available_keys

        # check that the service exists
        service = Service.query.filter(Service.id == service_id).first()
        if service is not None:
            # update the name if provided
            if name is not None:
                service.name = name

            # update the host if provided
            if host is not None:
                service.host = host

            # update the port if provided
            if port is not None:
                # catch exception if port is not a valid int
                try:
                    service.port = int(port)
                except ValueError:
                    pass

            # update the service type if provided
            if service_type is not None:
                service.service_type = service_type

            db.session.commit()
            return jsonify({'success': True}), 200

    return jsonify({'success': False}), 400


@mod_service.route('/list', methods=['GET', 'POST'])
@require_auth
def list_services():
    services = Service.query.all()
    return jsonify({
        'services': [{
            'name': s.name,
            'host': s.host,
            'port': s.port,
            'type': s.service_type
        } for s in services]
    })


@mod_service.route('/check', methods=['POST'])
@require_auth
def check_service():
    # get service ID if provided
    service_id = request.form.get('id')
    if service_id is not None:

        # get the service from the DB
        service = Service.query.filter(Service.id == service_id).first()
        if service is not None:
            service_type = service.service_type

            # MySQL
            if service_type == 'MySQL':
                body_args = [request.form.get(k) for k in ['username', 'password', 'db']]

                # check that all parameters were provided
                if all(body_args):
                    # expand arguments into variables
                    username, password, db_name = body_args

                    # check the service
                    res = MySQL.check.delay(host=service.host,
                                            port=service.port,
                                            username=username,
                                            password=password,
                                            db=db_name)

                    # return the check result
                    return jsonify({'success': True, 'result': res.get(timeout=1)}), 200

            # FTP
            elif service_type == 'FTP':
                body_args = [request.form.get(k) for k in ['username', 'password']]

                # check that all the body parameters has been provided
                if all(body_args):
                    # expand arguments into variables
                    username, password = body_args

                    # check the service
                    res = FTP.check.delay(host=service.host,
                                          port=service.port,
                                          username=username,
                                          password=password)

                    # return the check result
                    return jsonify({'success': True, 'result': res.get(timeout=5)}), 200
            else:
                return jsonify({'success': False, 'error': 'service_not_implemented'}), 400

    return jsonify({'success': False}), 400
