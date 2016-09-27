def list():
    """
    Requires an active bot session
    Requires a valid bot session cookie
    Lists all of the checks that are queued
    """
    pass

def check_in():
    """
    Requires an active bot session
    Requires a valid bot session cookie
    Bot will send the status of each currently active job
    Bot will send the status of all recently completed job
    Will notify the bot if the job has been deleted
    """
    pass

def request():
    """
    Requires an active bot session
    Requires a valid bot session cookie
    Bot requests one job to take on
    Server responds with a job for the bot to execute
    Server places that job into an "Active" list
    """
    pass

def abort():
    """
    Requires an active bot session
    Requires a valid bot session cookie
    Bot notifies the server that the job has been aborted
    Server places that job back into the available pool
    """
    pass

