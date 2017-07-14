from flask import jsonify
from app.mod_data import mod_data
from app.mod_data.service.models import Service
from app.mod_auth import require_auth
from app import db


@mod_data.route('/service/create', methods=['POST'])
@require_auth
def createService():
    s = Service(name='MySQL', host='127.0.0.1', port=3306, serviceType='MySQL')
    db.session.add(s)

    return str(s)


@mod_data.route('/service/list', methods=['GET', 'POST'])
@require_auth
def listServices():
    services = Service.query.all()
    return jsonify({
        'services': [{
            'name': s.name,
            'host': s.host,
            'port': s.port,
            'type': s.serviceType
        } for s in services]
    })