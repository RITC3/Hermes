from flask import Blueprint, jsonify, request
from sqlalchemy.exc import SQLAlchemyError
from ..mod_auth import require_auth
from ..mod_db import db
from .models import Service

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
    if service_id:
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
    if service_id and any(available_keys):
        name, host, port, service_type = available_keys

        # check that the team exists
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
