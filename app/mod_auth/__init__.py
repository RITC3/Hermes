from functools import wraps
from flask import request, abort

from app.mod_auth.models import Auth

def require_auth(api_method):
    @wraps(api_method)

    def check_api_key(*args, **kwargs):
        apiKey = request.headers.get('X-Hermes-Auth')
        if apiKey:
            keyResult = Auth.query.filter(Auth.api_key == apiKey).all()
            if len(keyResult) != 0:
                return api_method(*args, **kwargs)

        abort(403)

    return check_api_key