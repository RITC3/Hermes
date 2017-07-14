from ..mod_db import db


class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128))
    host = db.Column(db.String(128))
    port = db.Column(db.Integer)
    service_type = db.Column(db.String(128))

    def __init__(self, name, host, port, service_type):
        self.name = name
        self.host = host
        self.port = port
        self.service_type = service_type

    def __repr__(self):
        return f'<Service name="{self.name}" host="{self.host}" port={self.port} service_type="{self.service_type}">'
