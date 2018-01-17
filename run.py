#!/usr/bin/env python3

from app import app
from app.mod_socket import socketio
from app.config import BASE_DIR
from argparse import ArgumentParser
from os import path
import ssl


def main():
    ssl_base_dir = path.join(BASE_DIR, 'ssl')

    parser = ArgumentParser()
    parser.add_argument('--bind', '-b', action='store', help='the address to bind to', default='127.0.0.1')
    parser.add_argument('--port', '-p', action='store', type=int, help='the port to listen on', default=12321)
    parser.add_argument('--debug', '-d', action='store_true', help='enable debugging (use with caution)', default=False)
    parser.add_argument('--ssl', '-s', action='store_true', help='enable ssl', default=False)

    socketio.init_app(app)

    args = parser.parse_args()
    if args.ssl:
        ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        ctx.load_cert_chain(path.join(ssl_base_dir, 'server.crt'), path.join(ssl_base_dir, 'server.key'))

        socketio.run(app, host=args.bind, port=args.port, debug=args.debug, ssl_context=ctx)
    else:
        socketio.run(app, host=args.bind, port=args.port, debug=args.debug)


if __name__ == '__main__':
    main()
