from flask import Blueprint, render_template
from ..mod_socket import socketio
from logging import getLogger, DEBUG

mod_socket = Blueprint('socket', __name__, url_prefix='/socket')
logger = getLogger(__name__)
logger.setLevel(DEBUG)


@mod_socket.route('/')
def index():
    return render_template('socket_test.html')


@socketio.on('message')
def handle_message(message):
    logger.warning(f'[CLIENT] {message}')
    socketio.send('welcome!')
