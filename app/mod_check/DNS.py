from ..mod_check import app
from logging import getLogger
from dns.exception import DNSException
import dns.resolver

logger = getLogger('mod_check.DNS')

@app.task
def check():
    result = None
    try:
        resolver = dns.resolver.Resolver()  # create a new instance named 'myResolver'
        answers = resolver.query("google.com", "A")  # Lookup the 'A' record(s) for google.com
        return answers

    except DNSException as e:
        print(e)
        result = False
    return result

