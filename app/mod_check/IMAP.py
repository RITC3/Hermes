from ..mod_check import app
import imaplib
from logging import getLogger

logger = getLogger('mod_check.IMAP')


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

            scoring_exists = False
            # check if the scoring mailbox exists
            mb_res, _ = mail.select('Scoring')
            if mb_res == 'OK':
                # if it does, mark it for later use
                scoring_exists = True
            else:
                # if the scoring mailbox doesn't exist, select the inbox
                mb_res, _ = mail.select('INBOX')

            # if the result was OK (for either scoring or inbox)
            if mb_res == 'OK':
                # retrieve the ScoringCheck email
                search_res, search_data = mail.uid('search', None, 'SUBJECT', 'ScoringCheck-')
                if search_res == 'OK' and len(search_data) > 0:
                    # split the email UIDs and check for the
                    email_uids = search_data[0].split()
                    if len(email_uids) > 0:
                        latest_email_uid = email_uids[-1]

                        result, data = mail.uid('fetch', latest_email_uid, '(RFC822.TEXT)')
                        result = data[0][1].decode('utf8')

                        if not scoring_exists:
                            res, _ = mail.create('Scoring')
                            if res == 'OK':
                                res, _ = mail.copy(latest_email_uid, 'Scoring')
                                if res != 'OK':
                                    logger.error('Error copying email to Scoring mailbox')
                            else:
                                logger.error('Error creating Scoring mailbox')
                    else:
                        logger.error('No messages fetched')
                else:
                    logger.error('Error getting all messages')
            else:
                logger.error('Scoring mailbox does not exist')

    except (imaplib.IMAP4_SSL.error, imaplib.IMAP4.error) as e:
        logger.exception(e)
        result = False

    return result
