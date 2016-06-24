from flask import Flask, jsonify

#TODO Implement TLS

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    """Return generic 404 page"""
    return 'Requested page does not exist', 404

#TODO Move the function definitions to the another file called api-handlers.py

#Client API endpoint list
@app.route('/client/session/open')
def ClientSessionOpen():
    """
    Creates a session for a scoring bot
    """
    pass

@app.route('/client/session/close')
def ClientSessionClose():
    """
    Requires an active client session
    Requires a valid client session cookie
    This will deactivate the session for that client
    """
    pass

@app.route('/client/session/update')
def ClientSessionUpdate():
    #TODO Will the client supply other data as well
    """
    Requires an active client session
    Requires a valid client session cookie
    The scoring bot will provide the number of available subprocesses
        available for checks
    The scoring bot will provide the maximum number of checks it supports
    """
    pass

@app.route('/client/jobs/list')
def ClientJobsList():
    """
    Requires an active client session
    Requires a valid client session cookie
    Lists all of the checks that are queued
    """
    pass

@app.route('/client/jobs/check-in')
def ClientJobsCheckin():
    """
    Requires an active client session
    Requires a valid client session cookie
    Client will send the status of each currently active job
    Client will send the status of all recently completed job
    """
    pass

@app.route('/client/jobs/request')
def ClientJobsRequest():
    """
    Requires an active client session
    Requires a valid client session cookie
    Client requests one job to take on
    Server responds with a job for the client to execute
    Server places that job into an "Active" list
    """
    pass

@app.route('/client/jobs/abort')
def ClientJobsAbort():
    """
    Requires an active client session
    Requires a valid client session cookie
    Client notifies the server that the job has been aborted
    Server places that job back into the available pool
    """
    pass

#TODO Finish prototyping server API endpoints
#TODO Add requirements for server API endpoints
"""
NOTE: The following API endpoints will expect JSON.
If it is referencing a host on a team, it will need
to send a JSON object specifying those parameters
"""
@app.route('/web-gui/session/open')
def WebGuiSessionOpen():
    pass

@app.route('/web-gui/session/close')
def WebGuiSessionClose():
    pass

@app.route('/web-gui/team/list')
def WebGuiTeamList():
    pass

@app.route('/web-gui/team/create')
def WebGuiTeamCreate():
    pass

@app.route('/web-gui/team/delete')
def WebGuiTeamDelete():
    pass

@app.route('/web-gui/host/list')
def WebGuiHostList():
    pass

@app.route('/web-gui/host/create')
def WebGuiHostCreate():
    pass

@app.route('/web-gui/host/delete')
def WebGuiHostDelete():
    pass

@app.route('/web-gui/service/list')
def WebGuisServiceList():
    pass

@app.route('/web-gui/service/create')
def WebGuiServiceCreate():
    pass

@app.route('/web-gui/service/delete')
def WebGuiServiceDelete():
    pass

@app.route('/web-gui/check/enable')
def WebGuiCheckEnable():
    pass

@app.route('/web-gui/check/disable')
def WebGuiCheckDisable():
    pass

@app.route('/web-gui/check/interval/list')
def WebGuiCheckIntervalList():
    pass

@app.route('/web-gui/check/interval/set')
def WebGuiCheckIntervalSet():
    pass

@app.route('/web-gui/check/interval/default')
def WebGuiCheckIntervalDefault():
    pass
