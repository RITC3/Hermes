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

        with connection as mail:
            mail.login(user=username, password=password)
            res, _ = mail.select('Scoring')
            if res == 'OK':
                result, data = mail.uid('search', None, 'ALL')
                latest_email_uid = data[0].split()[-1]

                result, data = mail.uid('fetch', latest_email_uid, '(RFC822.TEXT)')
                result = data[0][1].decode('utf8')
            else:
                result = False
    except (imaplib.IMAP4_SSL.error, imaplib.IMAP4.error) as e:
        logger.exception(e)

    return result
