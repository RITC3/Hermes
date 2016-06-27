from flask import Flask
from .api import api

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    """Return generic 404 page"""
    return 'Requested page does not exist', 404

app.register_blueprint(api)
