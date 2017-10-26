import pymysql.cursors
from ..mod_check import app


@app.task
def check(host, port, username, password, db):
    connection = pymysql.connect(host=host,
                                 port=port,
                                 user=username,
                                 password=password,
                                 db=db,
                                 charset='utf8mb4',
                                 autocommit=True,
                                 cursorclass=pymysql.cursors.DictCursor)

    result = None
    try:
        with connection.cursor() as cursor:
            cursor.execute('SELECT @@version AS version')
            res = cursor.fetchone()

            if isinstance(res, dict):
                result = res.get('version', None)
    except pymysql.Error:
        result = False
    finally:
        connection.close()

    return result
