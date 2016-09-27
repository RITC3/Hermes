#!/usr/bin/env python
import nacl.secret
import nacl.utils
import json
import urllib2
from sys import argv
import base64

def authenticate(val, url="http://127.0.0.1:8080/api/bot/session/open"):
    """
    Authentication to the server
    base64 decode the value passed in
    initialize a NaCl box
    create a nonce
    encrypt dat shiz
    base64 encode it
    send it over to the server
    """
    key = base64.b64decode(val)
    box = nacl.secret.SecretBox(key)
    nonce = nacl.utils.random(nacl.secret.SecretBox.NONCE_SIZE)
    ciphertext = box.encrypt(key, nonce)
    transmit = base64.b64encode(ciphertext)
    data = json.dumps({"key": transmit})
    print data
    req = urllib2.Request(url, data, {'Content-Type': 'application/json'})
    f = urllib2.urlopen(req)
    response = f.read()
    print response
    f.close()
    #TODO Extract and use the API key that was returned

if __name__ == "__main__":
    authenticate(argv[1])
