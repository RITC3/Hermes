from ..mod_check import app
import paramiko
from paramiko.ssh_exception import SSHException

check_command = 'cat /home/scoring/check.txt'


@app.task
def check(host, port, username, password):
    client = paramiko.SSHClient()
    try:
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.WarningPolicy())

        client.connect(hostname=host, port=port, username=username, password=password)
        _, stdout, _ = client.exec_command(check_command, timeout=10)
        output = stdout.read()

        if output:
            result = output.decode('utf-8')
        else:
            result = False
    except SSHException as e:
        print(e)
        result = False

    client.close()
    return result
