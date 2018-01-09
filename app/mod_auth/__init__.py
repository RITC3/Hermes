from flask import request, session, jsonify
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
            key_count = Auth.query.filter(Auth.api_key == api_key).first()

            if key_count:
                if '_admin' not in session or not session['_admin']:
                    session['_admin'] = True

                # proceed if the API key exists
                return api_method(*args, **kwargs)
        else:
            # check if _admin is set but no API key provided
            if session.get('_admin', False):
                session.pop('_admin', None)

        # check for _team session cookie
        if '_team' in session:
            return api_method(*args, **kwargs)

        # catch-all 401 error
        return jsonify({'error': 'invalid_key'}), 401

    return check_api_key
