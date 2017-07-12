from flask import json
from app.mod_data import mod_data
from app.mod_data.service.models import Service
from app import db


@mod_data.route('/service/create', methods=['POST'])
def createService():
    s = Service(name='MySQL', host='127.0.0.1', port=3306, serviceType='MySQL')
    db.session.add(s)
    db.session.commit()

    return str(s)



@mod_data.route('/service/list', methods=['GET', 'POST'])
def listServices():
    services = Service.query.all()
    return json.dumps({
        'services': [
            {
                'name': s.name,
                'host': s.host,
                'port': s.port,
                'type': s.serviceType
            } for s in services
        ]
    })