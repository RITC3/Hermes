from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import app.config as config

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)

@app.errorhandler(404)
def page_not_found(error):
    """Return generic 404 page"""
    return 'Requested page does not exist', 404


# blueprints
from app.mod_data import mod_data as data_module
app.register_blueprint(data_module)

db.create_all()