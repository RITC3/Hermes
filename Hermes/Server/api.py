from flask import Blueprint
from . import endpoints

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/')
def welcome():
    return 'Welcome to the Hermes Scoring server'

#Bot API endpoint list
@api.route('/bot/session/open')
def FlaskBotSessionOpen():
    return endpoints.BotSessionOpen()

@api.route('/bot/session/close')
def FlaskBotSessionClose():
    return endpoints.BotSessionClose()

@api.route('/bot/session/update')
def FlaskBotSessionUpdate():
    return endpoints.BotSessionUpdate()

@api.route('/bot/jobs/list')
def FlaskBotJobsList():
    return endpoints.BotJobsList()

@api.route('/bot/jobs/check-in')
def FlaskBotJobsCheckin():
    return endpoints.BotJobsCheckin()

@api.route('/bot/jobs/request')
def FlaskBotJobsRequest():
    return endpoints.BotJobsRequest()

@api.route('/bot/jobs/abort')
def FlaskBotJobsAbort():
    return endpoints.BotJobsAbort()

#TODO Finish prototyping server API endpoints
#TODO Add requirements for server API endpoints
"""
NOTE: The following API endpoints will expect JSON.
If it is referencing a host on a team, it will need
to send a JSON object specifying those parameters
"""
@api.route('/web-gui/session/open')
def FlaskWebServerSessionOpen():
    return endpoints.WebServerSessionOpen()

@api.route('/web-gui/session/close')
def FlaskWebServerSessionClose():
    return endpoints.WebServerSessionClose()

@api.route('/web-gui/team/list')
def FlaskWebServerTeamList():
    return endpoints.WebServerTeamList()

@api.route('/web-gui/team/create')
def FlaskWebServerTeamCreate():
    return endpoints.WebServerTeamCreate()

@api.route('/web-gui/team/delete')
def FlaskWebServerTeamDelete():
    return endpoints.WebServerTeamDelete()

@api.route('/web-gui/host/list')
def FlaskWebServerHostList():
    return endpoints.WebServerHostList()

@api.route('/web-gui/host/create')
def FlaskWebServerHostCreate():
    return endpoints.WebServerTeamCreate()

@api.route('/web-gui/host/delete')
def FlaskWebServerHostDelete():
    return endpoints.WebServerHostDelete()

@api.route('/web-gui/service/list')
def FlaskWebServersServiceList():
    return endpoints.WebServersServiceList()

@api.route('/web-gui/service/create')
def FlaskWebServerServiceCreate():
    return endpoints.WebServerServiceCreate()

@api.route('/web-gui/service/delete')
def FlaskWebServerServiceDelete():
    return endpoints.WebServerServiceDelete()

@api.route('/web-gui/check/enable')
def FlaskWebServerCheckEnable():
    return endpoints.FlaskWebServerCheckEnable()

@api.route('/web-gui/check/disable')
def FlaskWebServerCheckDisable():
    return endpoints.WebServerCheckDisable()

@api.route('/web-gui/check/interval/list')
def FlaskWebServerCheckIntervalList():
    return endpoints.WebServerCheckIntervalList()

@api.route('/web-gui/check/interval/set')
def FlaskWebServerCheckIntervalSet():
    return endpoints.WebServerCheckIntervalSet()

@api.route('/web-gui/check/interval/default')
def FlaskWebServerCheckIntervalDefault():
    return endpoints.WebServerCheckIntervalDefault()
