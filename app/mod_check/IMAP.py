from ..mod_check import app
import imaplib
import email
import logging

logger = logging.getLogger('mod_check.IMAP')


def get_first_text_block(email_message_instance):
    maintype = email_message_instance.get_content_maintype()
    if maintype == 'multipart':
        for part in email_message_instance.get_payload():
            if part.get_content_maintype() == 'text':
                return part.get_payload()
    elif maintype == 'text':
        return email_message_instance.get_payload()


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
            mail.select('INBOX')

            result, data = mail.uid('search', None, 'ALL')
            latest_email_uid = data[0].split()[-1]

            result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
            raw_email = data[0][1]
            email_message = email.message_from_bytes(raw_email)
            result = get_first_text_block(email_message)

    except (imaplib.IMAP4_SSL.error, imaplib.IMAP4.error) as e:
        logger.exception(e)

    return result
