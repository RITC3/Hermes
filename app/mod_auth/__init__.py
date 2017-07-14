from functools import wraps
from sqlalchemy.exc import SQLAlchemyError
from flask import request, jsonify

from .models import Auth


# This decorator can be placed on any route handler to require API-key authentication
def require_auth(api_method):
    @wraps(api_method)
    # the actual function that does the authentication
    def check_api_key(*args, **kwargs):
        # get the API key from the headers
        api_key = request.headers.get('X-Hermes-Auth')
        if api_key:
            key_result = None
            # make sure to account for any SQLAlchemy exceptions that may occur
            try:
                # if one has been provided, check if there's an entry for it in the auth table
                key_result = Auth.query.filter(Auth.api_key == api_key).all()
            except SQLAlchemyError:
                pass

            if key_result:
                # if a row was returned matching the API key, proceed
                if len(key_result) != 0:
                    return api_method(*args, **kwargs)

        # catch-all 401 error
        return jsonify({'error': 'invalid_key'}), 401

    return check_api_key
