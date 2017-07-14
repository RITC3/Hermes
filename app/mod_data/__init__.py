from flask import Blueprint

# create the blueprint before anything else
mod_data = Blueprint('data', __name__, url_prefix='/api/data')

# auth
import app.mod_auth as auth



# team MVC
from app.mod_data import team

# service MVC
from app.mod_data import service