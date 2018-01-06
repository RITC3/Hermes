from celery import Celery

app = Celery('hermes',
             backend='rpc://',
             broker='amqp://guest@localhost//',
             include=[
                 'app.mod_check.MySQL',
                 'app.mod_check.FTP',
                 'app.mod_check.SSH',
                 'app.mod_check.IMAP',
                 'app.mod_check.SMTP',
                 'app.mod_check.SMB'
             ])

if __name__ == '__start__':
    app.start()
