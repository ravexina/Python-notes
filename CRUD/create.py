from my_conn import conn

connection = conn()

# Data
id = 1;
name = 'milad';
address = '132, Some Street, Somewhere, Some Town 12401 Some country'


# Creation
sql = "insert into users (`id`, `name`, `address`) values (%s, %s, %s);"

#  print(help(connection.cursor))

try:
    connection.cursor().execute(sql, (id, name, address))
    connection.commit()
    print('Added successfully');
except:
    print('Something went wrong while running sql')
finally:
    connection.close()
