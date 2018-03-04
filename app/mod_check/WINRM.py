import winrm
import argparse
from celery.utils.log import get_task_logger
from ..mod_check import app
logger = get_task_logger(__name__)
logger.setLevel(DEBUG)

# scoring share name and check file name
scoring_share = 'scoring'
scoring_check_path = '/scoring.txt'

@app.task
def check(host, port, username, password, cmd, domain=None, method=None):
    result = False

    try:
        auth_user = username
        if domain is not None:
            auth_user = '{}@{}'.format(username, domain)
        winrm_session = winrm.Session(host, auth=(auth_user, password))
        result = winrm_session.run_ps(cmd)
        if result.std_err:
            print(result.std_err)
        else:
            result = result.std_out
    except Exception as e:
        logger.exception(e)
        result = False

    return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-H', help='host', dest='host')
    parser.add_argument('-p', help='port', dest='port')
    parser.add_argument('-U', help='username', dest='user')
    parser.add_argument('-P', help='password', dest='passw')
    parser.add_argument('-D', help='domain', dest='domain', default=None)
    parser.add_argument('-m', help='method of auth', dest='method')
    parser.add_argument('-c', help='cmd to run', dest='cmd')
    args = parser.parse_args()
    result = check(args.host, args.port, args.user, args.passw, args.cmd, domain=args.domain)
    print(result)
