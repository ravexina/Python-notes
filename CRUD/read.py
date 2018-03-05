import my_conn as c

connection = c.conn()

with connection.cursor() as cursor:

    sql = "SELECT * FROM users WHERE `id` = 1"

    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            #print(row)
            print('name:', row[1]);
            print('address:', row[2]);
            print('\n --- \n');
    except:
        print('Something went wrong while running sql')
