#!/usr/bin/env python
from Hermes.Server import app
from argparse import ArgumentParser
import ssl
import os


def parse_and_run(args=None):
    basedir = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                           'Hermes', 'Server', 'ssl')
    p = ArgumentParser()
    p.add_argument('--bind', '-b', action='store', help='the address to bind to', default='127.0.0.1')
    p.add_argument('--port', '-p', action='store', type=int, help='the port to listen on', default=8080)
    p.add_argument('--debug', '-d', action='store_true', help='enable debugging (use with caution)', default=False)
    p.add_argument('--ssl', '-s', action='store_true', help='enable ssl', default=False)
    args = p.parse_args(args)
    if args.ssl:
        ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        ctx.load_cert_chain(os.path.join(basedir, 'server.crt'),
                            os.path.join(basedir, 'server.key'))
        app.run(host=args.bind, port=args.port, debug=args.debug, ssl_context=ctx)
    else:
        app.run(host=args.bind, port=args.port, debug=args.debug)

if __name__ == '__main__':
    parse_and_run()
