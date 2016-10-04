from flask import Blueprint, request, json, abort, session, sessions
from flask_api import status
from . import endpoints
import os
import base64
import random
import nacl.secret
import nacl.utils
from . import app

#TODO Implement authentcation
"""
Current thoughts for authentication and authorization
There is a shared secret that is generated on the server at initial runtime
The first step that a bot must take to authenticate with the server is to provide that shared secret encrypted with itself
    This ensures that the secret cannot be sniffed from the network
    When decrypted, it will be the shared secret
The server responds with a BotID and an API key (using the session module in Flask)
The bot will then send with each POST to the server the following two things in addition to other requirements for the endpoint
    The BotID being used
        or the hash of the BotID
    The ciphertext from encrypting the BotID with the API key
        The bot will not send the API KE
The server will then decrypt the ciphertext, and if the resultant plaintext matches the BotID, then the client must have the API key
"""

api = Blueprint('api', __name__, url_prefix='/api')

#Use the library NaCl to generate a secret key and base64 encode it for easy copying
api.secret_key = nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)
app.secret_key = api.secret_key
print("Connection Key: %s"  %(base64.b64encode(api.secret_key)))
box = nacl.secret.SecretBox(api.secret_key)

#Set the session type
#api.config['SESSION_TYPE'] = 'filesystem'

#login_manager = LoginManager()
#login_manager.setup_app(api)

#TODO Do I need to delete this?
#seed a random number generator with our newly generated secret key
random.seed(api.secret_key)

#TODO Create decorator for the API Key authentication, then just use that at ever endpoint that needs it.


@api.route('/', methods=['GET','POST'])
def welcome():
    return 'Welcome to the Hermes Scoring server'

#Bot API endpoint list
@api.route('/bot/session/open', methods=['POST'])
def FlaskBotSessionOpen():
    #Get the key from the json blob
    b64_key = request.json.get('key')
    print("b64_key: %s" %(b64_key))

    #Decrypt the key using NaCl
    encrytped_key = base64.b64decode(b64_key)
    key = box.decrypt(encrytped_key)

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
        return resp, status.HTTP_200_OK
    else:
        abort(401) #Unauthorized
    #return endpoints.BotSessionOpen(request)
    pass

@api.route('/bot/session/close', methods=['POST'])
def FlaskBotSessionClose():
    return endpoints.session.close()

#TODO: Why is this here?
@api.route('/bot/session/update', methods=['POST'])
def FlaskBotSessionUpdate():
    return endpoints.session.update()

#TODO Should this be a GET
@api.route('/bot/jobs/list', methods=['POST'])
def FlaskBotJobsList():
    return endpoints.jobs.list()

@api.route('/bot/jobs/check-in', methods=['POST'])
def FlaskBotJobsCheckin():
    return endpoints.jobs.check_in()

@api.route('/bot/jobs/request', methods=['POST'])
def FlaskBotJobsRequest():
    return endpoints.jobs.request()

@api.route('/bot/jobs/abort', methods=['POST'])
def FlaskBotJobsAbort():
    return endpoints.jobs.abort()

#TODO Finish prototyping server API endpoints
#TODO Add requirements for server API endpoints
"""
NOTE: The following API endpoints will expect JSON.
If it is referencing a host on a team, it will need
to send a JSON object specifying those parameters
"""
@api.route('/data/session/open', methods=['POST'])
def FlaskWebServerSessionOpen():
    return endpoints.data.session.open()

@api.route('/data/session/close', methods=['POST'])
def FlaskWebServerSessionClose():
    return endpoints.data.session.close()

#TODO Should this be a GET
@api.route('/data/team/list', methods=['POST'])
def FlaskWebServerTeamList():
    return endpoints.data.team.list()

@api.route('/data/team/create', methods=['POST'])
def FlaskWebServerTeamCreate():
    return endpoints.data.team.create()

@api.route('/data/team/delete', methods=['POST'])
def FlaskWebServerTeamDelete():
    return endpoints.data.team.delete()

@api.route('/data/host/list', methods=['POST'])
def FlaskWebServerHostList():
    return endpoints.data.host.list()

@api.route('/data/host/create', methods=['POST'])
def FlaskWebServerHostCreate():
    return endpoints.data.host.create()

@api.route('/data/host/delete', methods=['POST'])
def FlaskWebServerHostDelete():
    return endpoints.data.host.delete()

@api.route('/data/service/list', methods=['POST'])
def FlaskWebServersServiceList():
    return endpoints.data.service.list()

@api.route('/data/service/create', methods=['POST'])
def FlaskWebServerServiceCreate():
    return endpoints.data.service.create()

@api.route('/data/service/delete', methods=['POST'])
def FlaskWebServerServiceDelete():
    return endpoints.data.service.delete()

@api.route('/data/check/enable', methods=['POST'])
def FlaskWebServerCheckEnable():
    return endpoints.data.check.enable()

@api.route('/data/check/disable', methods=['POST'])
def FlaskWebServerCheckDisable():
    return endpoints.data.check.disable()

@api.route('/data/check/interval/list', methods=['POST'])
def FlaskWebServerCheckIntervalList():
    return endpoints.data.check.interval.list()

@api.route('/data/check/interval/set', methods=['POST'])
def FlaskWebServerCheckIntervalSet():
    return endpoints.data.check.interval.set()

@api.route('/data/check/interval/default', methods=['POST'])
def FlaskWebServerCheckIntervalDefault():
    return endpoints.check.interval.default()
