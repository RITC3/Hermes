from flask import Blueprint

# create the blueprint before anything else
mod_data = Blueprint('data', __name__, url_prefix='/api/data')


# instantiate the team controllers, models, etc.
from app.mod_data import team

# services
from app.mod_data import service