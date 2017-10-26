from celery import Celery

app = Celery('hermes',
             backend='rpc://',
             broker='amqp://guest@localhost//',
             include=['app.mod_check.MySQL'])

if __name__ == '__start__':
    app.start()
