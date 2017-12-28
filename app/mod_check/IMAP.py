from ..mod_check import app
import imaplib
import logging

logger = logging.getLogger('mod_check.IMAP')

@app.task
def check(host, port, username, password, use_ssl=False):
    # initialize result to None
    result = None

    try:
        # create the IMAP connection object
        if use_ssl:
            connection = imaplib.IMAP4_SSL(host=host, port=port)
        else:
            connection = imaplib.IMAP4(host=host, port=port)
            logger.debug('connection', connection)

        with connection as conn:
            conn.login(user=username, password=password)
            print(conn.list())
            print(conn.capability())
            print(conn.select('INBOX'))

    except (imaplib.IMAP4_SSL.error, imaplib.IMAP4.error) as e:
        logger.exception(e)

    return result
