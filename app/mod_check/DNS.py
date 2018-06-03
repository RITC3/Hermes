from ..mod_check import app
from logging import getLogger
from dns.exception import DNSException
from dns import resolver, reversename

logger = getLogger('mod_check.DNS')

@app.task
def check(host, record_type, query, dns_response, port=None):
    resolver.default_resolver = resolver.Resolver(configure=False)
    resolver.default_resolver.nameservers = [host]
    
    try:
        if record_type == 'PTR':
            query = reversename.from_address(query)
        answers = resolver.query(query, record_type.upper())

    except DNSException as e:
        logger.exception(e)
        return False

    answer = answers[0].to_text()
    if answer == dns_response:
        return answer
    return False
