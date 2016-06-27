from flask import Flask, jsonify

#TODO Implement TLS

app = Flask(__name__)
app.run()

@app.errorhandler(404)
def page_not_found(error):
    """Return generic 404 page"""
    return 'Requested page does not exist', 404

@app.route('/')
def welcome():
    return 'Welcome to the Hermes Scoring server'

#Bot API endpoint list
@app.route('/bot/session/open')
def FlaskBotSessionOpen():
    endpoints.BotSessionOpen()

@app.route('/bot/session/close')
def FlaskBotSessionClose():
    endpoints.BotSessionClose()

@app.route('/bot/session/update')
def FlaskBotSessionUpdate():
    endpoints.BotSessionUpdate()

@app.route('/bot/jobs/list')
def FlaskBotJobsList():
    endpoints.BotJobsList()

@app.route('/bot/jobs/check-in')
def FlaskBotJobsCheckin():
    endpoints.BotJobsCheckin()

@app.route('/bot/jobs/request')
def FlaskBotJobsRequest():
    endpoints.BotJobsRequest()

@app.route('/bot/jobs/abort')
def FlaskBotJobsAbort():
    endpoints.BotJobsAbort()

#TODO Finish prototyping server API endpoints
#TODO Add requirements for server API endpoints
"""
NOTE: The following API endpoints will expect JSON.
If it is referencing a host on a team, it will need
to send a JSON object specifying those parameters
"""
@app.route('/web-gui/session/open')
def FlaskWebServerSessionOpen():
    endpoints.WebServerSessionOpen()

@app.route('/web-gui/session/close')
def FlaskWebServerSessionClose():
    endpoints.WebServerSessionClose()

@app.route('/web-gui/team/list')
def FlaskWebServerTeamList():
    endpoints.WebServerTeamList()

@app.route('/web-gui/team/create')
def FlaskWebServerTeamCreate():
    endpoints.WebServerTeamCreate()

@app.route('/web-gui/team/delete')
def FlaskWebServerTeamDelete():
    endpoints.WebServerTeamDelete()

@app.route('/web-gui/host/list')
def FlaskWebServerHostList():
    endpoints.WebServerHostList()

@app.route('/web-gui/host/create')
def FlaskWebServerHostCreate():
    endpoints.WebServerTeamCreate()

@app.route('/web-gui/host/delete')
def FlaskWebServerHostDelete():
    endpoints.WebServerHostDelete()

@app.route('/web-gui/service/list')
def FlaskWebServersServiceList():
    endpoints.WebServersServiceList()

@app.route('/web-gui/service/create')
def FlaskWebServerServiceCreate():
    endpoints.WebServerServiceCreate()

@app.route('/web-gui/service/delete')
def FlaskWebServerServiceDelete():
    endpoints.WebServerServiceDelete()

@app.route('/web-gui/check/enable')
def FlaskWebServerCheckEnable():
    endpoints.FlaskWebServerCheckEnable()

@app.route('/web-gui/check/disable')
def FlaskWebServerCheckDisable():
    endpoints.WebServerCheckDisable()

@app.route('/web-gui/check/interval/list')
def FlaskWebServerCheckIntervalList():
    endpoints.WebServerCheckIntervalList()

@app.route('/web-gui/check/interval/set')
def FlaskWebServerCheckIntervalSet():
    endpoints.WebServerCheckIntervalSet()

@app.route('/web-gui/check/interval/default')
def FlaskWebServerCheckIntervalDefault():
    endpoints.WebServerCheckIntervalDefault()
