from flask import Flask
from .mod_db import db

# blueprints
from .mod_service.controllers import mod_service
from .mod_team.controllers import mod_team

app = Flask(__name__)
app.config.from_object('app.config.Debug')

# register blueprints
app.register_blueprint(mod_service)
app.register_blueprint(mod_team)


@app.errorhandler(404)
def page_not_found(error):
    """Return generic 404 page"""
    return 'Requested page does not exist', 404


db.init_app(app)
with app.app_context():
    db.create_all()
