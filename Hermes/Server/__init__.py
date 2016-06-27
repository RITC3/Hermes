from flask import Flask
import ssl
import os
from .api import api

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

@app.errorhandler(404)
def page_not_found(error):
    """Return generic 404 page"""
    return 'Requested page does not exist', 404

app.register_blueprint(api)

try:
    ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ctx.load_cert_chain(os.path.join(basedir, 'ssl', 'server.crt'),
                        os.path.join(basedir, 'ssl', 'server.key'))
    app.run(ssl_context=ctx)
except:
    app.run()
