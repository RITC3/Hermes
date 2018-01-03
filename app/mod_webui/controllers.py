"""
    Controller for handling web ui of Hermes
"""
from flask import Blueprint, request, render_template, make_response, redirect, url_for
#from sqlalchemy.exc import SQLAlchemyError
#from ..mod_auth import require_auth
#from ..mod_db import db

mod_webui = Blueprint('webui', __name__, url_prefix='/', template_folder='templates')

@mod_webui.context_processor
def all_services():
    """
        this allows for the services to be accessed from every template without copy/pasting
    """
    return dict(all_services=[('Web', 'wb_cloudy'), ('IMAP', 'drafts'), ('SMTP', 'email'), \
                             ('LDAP', 'supervisor_account'), ('WinRM', 'contacts')])

@mod_webui.route('/')
def index():
    # show should be 2 if logged in (this logic might be bad)
    return render_template('index.html')

# test route for admin functionality
@mod_webui.route('admin')
def admin():
    # just for testing
    return render_template('index.html', is_admin=True)

# we leave off the leading / since it is declared as the url_prefix
@mod_webui.route('register', methods=['GET', 'POST'])
def register():
    # delete any cookie they may have
    if request.method == 'POST':
        # do things with the stuff, aka create account and redirect
        val = ('not yet', 400)
    else:
        val = render_template('register.html')
    resp = make_response(val)
    resp.set_cookie('username', '', expires=0) 
    return resp

@mod_webui.route('login', methods=['POST'])
def login():
    # check login, set session to logged in
    resp = make_response(redirect(url_for('webui.index')))
    resp.set_cookie('username', 'test123')
    return resp

@mod_webui.route('logout')
def logout():
    resp = make_response(redirect(url_for('webui.index')))
    resp.set_cookie('username', '', expires=0)
    return resp

@mod_webui.route('config/<service>', methods=['GET', 'POST'])
def config(service):
    if request.method == 'POST':
        # configure required service
        return f"soon configure {service}"
    else:
        return render_template('configure.html', service=service)

@mod_webui.route('results')
def results():
    return render_template('results.html')
