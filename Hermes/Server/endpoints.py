from flask import session
def page_not_found(error):
    """Return generic 404 page"""
    return 'Requested page does not exist', 404

#Bot API endpoint list
def BotSessionOpen():
    """
    Creates a session for a scoring bot
    """
    pass

def BotSessionClose():
    """
    Requires an active bot session
    Requires a valid bot session cookie
    This will deactivate the session for that bot
    """
    pass

def BotSessionUpdate():
    #TODO Will the bot supply other data as well
    """
    Requires an active bot session
    Requires a valid bot session cookie
    The scoring bot will provide the number of available subprocesses
        available for checks
    The scoring bot will provide the maximum number of checks it supports
    """
    pass

def BotJobsList():
    """
    Requires an active bot session
    Requires a valid bot session cookie
    Lists all of the checks that are queued
    """
    pass

def BotJobsCheckin():
    """
    Requires an active bot session
    Requires a valid bot session cookie
    Bot will send the status of each currently active job
    Bot will send the status of all recently completed job
    Will notify the bot if the job has been deleted
    """
    pass

def BotJobsRequest():
    """
    Requires an active bot session
    Requires a valid bot session cookie
    Bot requests one job to take on
    Server responds with a job for the bot to execute
    Server places that job into an "Active" list
    """
    pass

def BotJobsAbort():
    """
    Requires an active bot session
    Requires a valid bot session cookie
    Bot notifies the server that the job has been aborted
    Server places that job back into the available pool
    """
    pass

#TODO BotJobsComplete()

#TODO Finish prototyping server API endpoints
#TODO Add requirements for server API endpoints
"""
NOTE: The following API endpoints will expect JSON.
If it is referencing a host on a team, it will need
to send a JSON object specifying those parameters
"""
def WebServerSessionOpen():
    """
    Creates a session for the web server instance
    """
    pass

def WebServerSessionClose():
    """
    Requires an active web server session
    Requires a valid web server session cookie
    Close session for the web server
    Invalidate the session cookie for that server
    """
    pass

def WebServerTeamList():
    """
    Requires an active web server session
    Requires a valid web server session cookie
    Lists the teams currently created
    Lists the teams' ID numbers
    Lists the teams' names
    """
    pass

def WebServerTeamCreate():
    """
    Requires an active web server session
    Requires a valid web server session cookie
    Creates a team
    Accepts a Team ID
        If the ID that is passed is invalid or conflicts with another team ID,
        then the ID will be assigned accordingly
    Team name can be passed manually
        Default team name will be "Team <Team ID>"
        This is to facilitate special team names, or machine groupings if you
        are using this project as a network monitoring system
    """
    pass

def WebServerTeamDelete():
    """
    Requires an active web server session
    Requires a vali web server session cookie
    Requires the team ID number to be sent
    This action will call 
    """
    pass

def WebServerHostList():
    """
    Requires an active web server session
    Requires a valid web server session cookie
    Requires a valid team ID
    """
    pass

def WebServerHostCreate():
    """
    Requires an active web server session
    Requires a valid web server session cookie
    Requires a valid ID
    Accepts a Host ID
        If the Host ID is not supplied, or the supplied Host ID is invalid,
        then the Host ID will be assigned accordingly
    """
    pass

def WebServerHostDelete():
    """
    Requires an active web server session
    Requires a valid web server session cookie
    Requires a team ID
    Requires a Host ID
    This function will call WebServerServiceDelete() on all services on this host
    """
    pass

def WebServersServiceList():
    """
    Requires an active web server session
    Requires a valid web server session cookie
    Requires a valid Team ID
    Requires a valid Host ID
    Lists all of the services on this host
    """
    pass

def WebServerServiceCreate():
    """
    Requires an active web server session
    Requires a valid web server session cookie
    Requires a valid Team ID
    Requires a valid Host ID
    Requires a valid Service Name
        This will serve as the protocol
        If the Service Name is TCP/UDP based
            Requires a port number
        If the Service Name is an IP protocol
            Requires only IP address
    Requires IP address
    This will call WebServerCheckEnable() on the service
    """
    pass

def WebServerServiceDelete():
    """
    Requires an active web server session
    Requires a valid web server session cookie
    Requires a valid Team ID
    Requires a valid Host ID
    Removes the service from any active checks
        This will send an abort to the Bot????
    """
    pass

def WebServerCheckEnable():
    """
    requires an active web server session
    requires a valid web server session cookie
    requires a valid team id
    requires a valid host id
    Will set the check as enabled for the next round and all subsequent checks
    """
    pass

def WebServerCheckDisable():
    """
    requires an active web server session
    requires a valid web server session cookie
    requires a valid team id
    requires a valid host id
    Will set the check as disabled for the next round and all subsequent checks
    """
    pass

def WebServerCheckIntervalList():
    """
    Requires an active web server session
    Requires a valid web server session cookie
    Returns the interval between check rounds
    """
    pass

def WebServerCheckIntervalSet():
    """
    Requires an active web server session
    Requires a valid web server session cookie
    Sets the interval between check rounds
        If the supplied time value is invalid, then the time will be set to
        the default with WebServerCheckIntervalDefault()
    """
    pass

def WebServerCheckIntervalDefault():
    """
    Requires an active web server session
    Requires a valid web server session cookie
    Sets the check interval to the default time
    """
    pass
