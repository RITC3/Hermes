from ..mod_check import app
from smb.SMBConnection import SMBConnection
from celery.utils.log import get_task_logger


@app.task
def check(host, port, username, password):
    logger = get_task_logger(__name__)
    try:
        conn = SMBConnection(username=username, password=password, my_name='Hermes', remote_name='HERMES')
        conn.connect(host, port, timeout=10)

        shares = conn.listShares(timeout=10)
        for share in shares:
            logger.info(share.name)
    except Exception as e:
        logger.exception(e)
