import nacl.secret
import nacl.utils


box = nacl.secret.SecretBox(api.secret_key)

def open():
    """
    Creates a session for a scoring bot
    """
    #Get the key from the json blob
    b64_key = request.json.get('key')
    print("b64_key: %s" %(b64_key))

    #Decrypt the key using NaCl
    encrypted_key = base64.b64decode(b64_key)
    key = box.decrypt(encrypted_key)

    #If they have the key
    if key == api.secret_key:
        print("They're equal")
        #TODO Create a BotID and an API key and store it in a session object
        #If duplicate, try again
        while True:
            print("Made it into the loop")
            botID = random.randint(0, 999)
            print(botID)
            #If we found a unique botID then use that one
            print("Session", session)
            if botID not in session:
                print("ID found")
                print("ID assigned")
                break

        print(botID)
        botApiKey = str(base64.b64encode(os.urandom(32)))
        print("botApiKey", botApiKey)
        session.new
        session[botID] = botApiKey
        print(session[botID])
    #if they don't have the key
        #return a 401 Unauthorized
        #TODO Return the botID and the API Key encrypted with the shared secret
        #Do this as a JSON object that has an encrypted (AES 256) JSON blob in it with the ID and Key
        resp = Response(flask.json.jsonify(BotID=botID, Key=botApiKey), status=200, mimetype='application/json')
        print(resp)
        return resp
    else:
        abort(401) #Unauthorized
    #return endpoints.BotSessionOpen(request)
    pass


    pass

def close():
    """
    Requires an active bot session
    Requires a valid bot session cookie
    This will deactivate the session for that bot
    """
    pass

def update()
    #TODO Will the bot supply other data as well
    """
    Requires an active bot session
    Requires a valid bot session cookie
    The scoring bot will provide the number of available subprocesses
        available for checks
    The scoring bot will provide the maximum number of checks it supports
    """
    pass



