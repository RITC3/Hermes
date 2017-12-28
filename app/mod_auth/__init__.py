from flask import request, jsonify
from functools import wraps

from .models import Auth


# This decorator can be placed on any route handler to require API-key authentication
def require_auth(api_method):
    # the actual function that does the authentication
    @wraps(api_method)
    def check_api_key(*args, **kwargs):
        # get the API key from the headers
        api_key = request.headers.get('X-Hermes-Auth')
        if api_key:
            # if one has been provided, check if there's an entry for it in the auth table
            key_count = Auth.query.filter(Auth.api_key == api_key).count()

            if key_count > 0:
                # proceed if the API key exists
                return api_method(*args, **kwargs)

        # catch-all 401 error
        return jsonify({'error': 'invalid_key'}), 401

    return check_api_key
