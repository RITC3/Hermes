from ..mod_check import app
from smtplib import SMTP, SMTPException
from logging import getLogger
from os import urandom
from binascii import hexlify

logger = getLogger('mod_check.SMTP')


def rand_hex_str(length):
    return hexlify(urandom(length)).decode('utf8')


@app.task
def check(host, port, username, domain, password, use_ssl=False):
    result = False

    try:
        with SMTP(host=host, port=port, timeout=10) as smtp:
            # if SSL is to be used
            if use_ssl:
                smtp.starttls()

            # send EHLO
            smtp.ehlo(domain)

            # login
            smtp.login(user=username, password=password)

            # generate the subject line and send the email
            subject = f'ScoringCheck-{rand_hex_str(8)}'
            smtp.sendmail(from_addr=username,
                          to_addrs=f'scoring@{domain}',
                          msg=f'Subject: {subject}\n\n{rand_hex_str(32)}')

            # if successful, return subject
            result = subject

    except SMTPException as e:
        logger.exception(e)

    return result
