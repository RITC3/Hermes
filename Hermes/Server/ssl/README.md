To generate self-signed certs for testing:
openssl req -x509 -newkey rsa:2048 -keyout server.key -out server.crt -days 365 -nodes
