from flask import Flask
from .api import api
from .db import create_db

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    """Return generic 404 page"""
    return 'Requested page does not exist', 404

app.register_blueprint(api)
app.secret_key = api.secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///server.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
create_db(app)