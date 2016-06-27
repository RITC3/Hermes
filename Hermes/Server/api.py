from flask import Blueprint, jsonify

api = Blueprint('api', __name__, '/api')

@api.route('/')
def welcome():
    return 'Welcome to the Hermes Scoring server'

#Bot API endpoint list
@api.route('/bot/session/open')
def FlaskBotSessionOpen():
    endpoints.BotSessionOpen()

@api.route('/bot/session/close')
def FlaskBotSessionClose():
    endpoints.BotSessionClose()

@api.route('/bot/session/update')
def FlaskBotSessionUpdate():
    endpoints.BotSessionUpdate()

@api.route('/bot/jobs/list')
def FlaskBotJobsList():
    endpoints.BotJobsList()

@api.route('/bot/jobs/check-in')
def FlaskBotJobsCheckin():
    endpoints.BotJobsCheckin()

@api.route('/bot/jobs/request')
def FlaskBotJobsRequest():
    endpoints.BotJobsRequest()

@api.route('/bot/jobs/abort')
def FlaskBotJobsAbort():
    endpoints.BotJobsAbort()

#TODO Finish prototyping server API endpoints
#TODO Add requirements for server API endpoints
"""
NOTE: The following API endpoints will expect JSON.
If it is referencing a host on a team, it will need
to send a JSON object specifying those parameters
"""
@api.route('/web-gui/session/open')
def FlaskWebServerSessionOpen():
    endpoints.WebServerSessionOpen()

@api.route('/web-gui/session/close')
def FlaskWebServerSessionClose():
    endpoints.WebServerSessionClose()

@api.route('/web-gui/team/list')
def FlaskWebServerTeamList():
    endpoints.WebServerTeamList()

@api.route('/web-gui/team/create')
def FlaskWebServerTeamCreate():
    endpoints.WebServerTeamCreate()

@api.route('/web-gui/team/delete')
def FlaskWebServerTeamDelete():
    endpoints.WebServerTeamDelete()

@api.route('/web-gui/host/list')
def FlaskWebServerHostList():
    endpoints.WebServerHostList()

@api.route('/web-gui/host/create')
def FlaskWebServerHostCreate():
    endpoints.WebServerTeamCreate()

@api.route('/web-gui/host/delete')
def FlaskWebServerHostDelete():
    endpoints.WebServerHostDelete()

@api.route('/web-gui/service/list')
def FlaskWebServersServiceList():
    endpoints.WebServersServiceList()

@api.route('/web-gui/service/create')
def FlaskWebServerServiceCreate():
    endpoints.WebServerServiceCreate()

@api.route('/web-gui/service/delete')
def FlaskWebServerServiceDelete():
    endpoints.WebServerServiceDelete()

@api.route('/web-gui/check/enable')
def FlaskWebServerCheckEnable():
    endpoints.FlaskWebServerCheckEnable()

@api.route('/web-gui/check/disable')
def FlaskWebServerCheckDisable():
    endpoints.WebServerCheckDisable()

@api.route('/web-gui/check/interval/list')
def FlaskWebServerCheckIntervalList():
    endpoints.WebServerCheckIntervalList()

@api.route('/web-gui/check/interval/set')
def FlaskWebServerCheckIntervalSet():
    endpoints.WebServerCheckIntervalSet()

@api.route('/web-gui/check/interval/default')
def FlaskWebServerCheckIntervalDefault():
    endpoints.WebServerCheckIntervalDefault()
