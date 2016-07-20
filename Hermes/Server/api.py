from flask import Blueprint, request, json, abort
from . import endpoints
import os
import base64
import random

#TODO Implement authentcation
"""
Current thoughts for authentication and authorization
There is a shared secret that is generated on the server at initial runtime
The first step that a bot must take to authenticate with the server is to provide that shared secret
The server responds with a BotID and an API key (using the session module in Flask)
The bot will then send with each POST to the server the following two things in addition to other requirements for the endpoint
    The BotID being used
        or the hash of the BotID
    The ciphertext from encrypting the BotID with the API key
        The bot will not send the API KE
The server will then decrypt the ciphertext, and if the resultant plaintext matches the BotID, then the client must have the API key
"""

"""
OAuth may accomplish the above thing, as well.
We could be our own OAuth provider
    or we could offload it onto Google OAuth
I don't think that this works for our current use case
"""

#TODO Create decorator for the API Key authentication, then just use that at ever endpoint that needs it.

api = Blueprint('api', __name__, url_prefix='/api')

#Set the secret key on startup.  This will require you to have control of the server in order to register a Bot
api.secret_key = str(base64.b64encode(os.urandom(32)))
print "Connection Key:", api.secret_key

#seed a random number generator with our newly generated secret key
random.seed(api.secret_key)

@api.route('/', methods=['GET','POST'])
def welcome():
    return 'Welcome to the Hermes Scoring server'

#Bot API endpoint list
@api.route('/bot/session/open', methods=['POST'])
def FlaskBotSessionOpen():
    #Get the key from the json blob
    #If they have the key
        #Do the rest to authenticate them
    #if they don't have the key
        #return a 401 Unauthorized
    key = request.json.get('key')
    if key == api.secret_key:
        #Generate a unique ID for them
        #Get a session cookie for them

        return "success"
    else:
        abort(401) #Unauthorized
    #return endpoints.BotSessionOpen(request)
    pass

@api.route('/bot/session/close', methods=['POST'])
def FlaskBotSessionClose():
    return endpoints.BotSessionClose()

@api.route('/bot/session/update', methods=['POST'])
def FlaskBotSessionUpdate():
    return endpoints.BotSessionUpdate()

#TODO Should this be a GET
@api.route('/bot/jobs/list', methods=['POST'])
def FlaskBotJobsList():
    return endpoints.BotJobsList()

@api.route('/bot/jobs/check-in', methods=['POST'])
def FlaskBotJobsCheckin():
    return endpoints.BotJobsCheckin()

@api.route('/bot/jobs/request', methods=['POST'])
def FlaskBotJobsRequest():
    return endpoints.BotJobsRequest()

@api.route('/bot/jobs/abort', methods=['POST'])
def FlaskBotJobsAbort():
    return endpoints.BotJobsAbort()

#TODO Finish prototyping server API endpoints
#TODO Add requirements for server API endpoints
"""
NOTE: The following API endpoints will expect JSON.
If it is referencing a host on a team, it will need
to send a JSON object specifying those parameters
"""
@api.route('/web-gui/session/open', methods=['POST'])
def FlaskWebServerSessionOpen():
    return endpoints.WebServerSessionOpen()

@api.route('/web-gui/session/close', methods=['POST'])
def FlaskWebServerSessionClose():
    return endpoints.WebServerSessionClose()

#TODO Should this be a GET
@api.route('/web-gui/team/list', methods=['POST'])
def FlaskWebServerTeamList():
    return endpoints.WebServerTeamList()

@api.route('/web-gui/team/create', methods=['POST'])
def FlaskWebServerTeamCreate():
    return endpoints.WebServerTeamCreate()

@api.route('/web-gui/team/delete', methods=['POST'])
def FlaskWebServerTeamDelete():
    return endpoints.WebServerTeamDelete()

@api.route('/web-gui/host/list', methods=['POST'])
def FlaskWebServerHostList():
    return endpoints.WebServerHostList()

@api.route('/web-gui/host/create', methods=['POST'])
def FlaskWebServerHostCreate():
    return endpoints.WebServerTeamCreate()

@api.route('/web-gui/host/delete', methods=['POST'])
def FlaskWebServerHostDelete():
    return endpoints.WebServerHostDelete()

@api.route('/web-gui/service/list', methods=['POST'])
def FlaskWebServersServiceList():
    return endpoints.WebServersServiceList()

@api.route('/web-gui/service/create', methods=['POST'])
def FlaskWebServerServiceCreate():
    return endpoints.WebServerServiceCreate()

@api.route('/web-gui/service/delete', methods=['POST'])
def FlaskWebServerServiceDelete():
    return endpoints.WebServerServiceDelete()

@api.route('/web-gui/check/enable', methods=['POST'])
def FlaskWebServerCheckEnable():
    return endpoints.FlaskWebServerCheckEnable()

@api.route('/web-gui/check/disable', methods=['POST'])
def FlaskWebServerCheckDisable():
    return endpoints.WebServerCheckDisable()

@api.route('/web-gui/check/interval/list', methods=['POST'])
def FlaskWebServerCheckIntervalList():
    return endpoints.WebServerCheckIntervalList()

@api.route('/web-gui/check/interval/set', methods=['POST'])
def FlaskWebServerCheckIntervalSet():
    return endpoints.WebServerCheckIntervalSet()

@api.route('/web-gui/check/interval/default', methods=['POST'])
def FlaskWebServerCheckIntervalDefault():
    return endpoints.WebServerCheckIntervalDefault()
