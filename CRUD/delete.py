exec( open('./conn.py').read() );

with connection.cursor() as cursor:

    sql = "DELETE FROM users WHERE `id` = 1"

    try:
        cursor.execute(sql)
        print('Deleted...');
        connection.commit();
    except:
        print('Something went wrong while running sql')
    finally:
        connection.close()

    

