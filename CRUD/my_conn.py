import pymysql

def conn():
    connection = pymysql.connect(
            host = '127.0.0.1',
            port = 32769,
            user = 'root',
            password ='root',
            db = 'python',
        )

    return connection
