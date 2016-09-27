def list():
    """
    Requires an active web server session
    Requires a valid web server session cookie
    Requires a valid Team ID
    Requires a valid Host ID
    Lists all of the services on this host
    """
    pass

def create():
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

def delete():
    """
    Requires an active web server session
    Requires a valid web server session cookie
    Requires a valid Team ID
    Requires a valid Host ID
    Removes the service from any active checks
        This will send an abort to the Bot????
    """
    pass

