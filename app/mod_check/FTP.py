from ftplib import FTP, all_errors
from tempfile import SpooledTemporaryFile
from ..mod_check import app

scoring_file = '/scoring_engine-do_not_remove'

@app.task
def check(host, port, username, password):
    # catch FTP ser
    try:
        # get an FTP context
        with FTP() as ftp:
            # connect to the FTP server and login
            ftp.connect(host=host, port=port)
            ftp.login(user=username, passwd=password)

            # list all files
            file_list = list(ftp.mlsd())
            if file_list:
                with SpooledTemporaryFile(max_size=100) as f:
                    ftp.retrbinary(f'RETR {scoring_file}', f.write)
                    f.seek(0)
                    result = f.read().decode('utf8').rstrip('\n')
            else:
                result = False
    except all_errors as e:
        print(e)
        result = False

    return result
