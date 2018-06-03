from ..mod_check import app
import ldap
from logging import getLogger

logger = getLogger('mod_check.IMAP')

@app.task
def check(host, username, password, domain, port=None):
    """Perform LDAP check against a target

    Perform LDAP check by default. Ensure successful authentication using ldap_bind. 

    Args:
        host       (str): Service IP address or DNS name of target
        port       (str): Service port
        username   (str): Username of LDAP user
        password   (str): Password of LDAP user
        domain     (str): FQDN of domain

    Returns:
        result (bool): Boolean value noting check success or failure:

    """
    con = ldap.initialize('ldap://{}:{}'.format(host, port)) # checks ldap (389), not ldaps (636)
    sld, tld = domain.split('.') # Splits only on a domain with two levels
    if con.simple_bind_s("cn={},dc={},dc={}".format(username, sld, tld), password): # Try to bind 
        return "Successful bind"
    else:
        return False
