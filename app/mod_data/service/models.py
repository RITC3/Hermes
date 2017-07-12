from app import db

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement='auto')
    name = db.Column(db.String(128))
    host = db.Column(db.String(128))
    port = db.Column(db.Integer)
    serviceType = db.Column(db.String(128))

    def __init__(self, name, host, port, serviceType):
        self.name = name
        self.host = host
        self.port = port
        self.serviceType = serviceType

    def __repr__(self):
        return f'<Service name="{self.name}">'