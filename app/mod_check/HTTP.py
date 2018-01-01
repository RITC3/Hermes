from ..mod_check import app
import requests
import hashlib
from logging import getLogger

logger = logging.getLogger('mod_check.HTTP')

@app.task
def check(host, uri, stored_hash, port=None, use_ssl=False):
    """Perform HTTP/HTTPS check against a target

    Perform HTTP check by default. Match SHA-512 hash of the body of the page with a stored hash. If the hashes match, the check succeeds.

    Args:
        host       (str): IP address or DNS name of target
        uri        (str): URI to be accessed on the target
        body_hash  (str): SHA512 hash hexdigest to compare the hash of the new page to
        port       (int): TCP port to access the web server on the target
        use_ssl   (bool): Boolean to use SSL/TLS

    Returns:
        result (bool): Boolean value noting check success or failure:

    """
    #Initialize result to None
    result = None

    try:
        #Assemble URL
        if use_ssl:
            url = "https://"
            if port is None:
                port = 443
                logger.debug("Changing HTTPS port to 443 since no port was supplied")
        else:
            url = "http://"
            if port is None:
                port = 80
                logger.debug("Changing HTTP port to 80 since no port was supplied")

        #Build URL and attempt to download page
        url = url + host + ":" + str(port) + "/" + uri
        resp = requests.get(url)

        #Calculate hash of current page with supplied hash in short form
        new_hash = hashlib.sha512(resp.content).hexdigest()

        #Verify new hash matches stored hash
        if new_hash == stored_hash:
            result = True
        else:
            print("false")
            result = False

    except Exception as e:
        logger.exception(e)
        result = False

    return result
