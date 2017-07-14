from flask import Blueprint, jsonify
from ..mod_auth import require_auth
from ..mod_db import db
from .models import Service

mod_service = Blueprint('service', __name__, url_prefix='/api/data/service')


@mod_service.route('/create', methods=['POST'])
@require_auth
def create_service():
    s = Service(name='MySQL', host='127.0.0.1', port=3306, service_type='MySQL')
    db.session.add(s)

    return str(s)


@mod_service.route('/list', methods=['GET', 'POST'])
@require_auth
def list_services():
    services = Service.query.all()
    return jsonify({
        'services': [{
            'name': s.name,
            'host': s.host,
            'port': s.port,
            'type': s.serviceType
        } for s in services]
    })
