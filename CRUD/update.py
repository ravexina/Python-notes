from my_conn import conn
connection = conn()

with connection.cursor() as cursor:

    sql = "UPDATE users  SET `name` = %s WHERE `id` = %s"

    try:
        cursor.execute(sql, ('ravexina', 1))
        print('Updated...');
        connection.commit();
    except:
        print('Something went wrong while running sql')
    finally:
        connection.close()

    

