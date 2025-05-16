import pymysql

# Connect to the MySQL database
try:
    connection = pymysql.connect(
        host='localhost',         # or an IP address
        user='root',
        password='kole',
        database='Assignments',
        port=3306                 # default MySQL port
    )

    print("Connected to MySQL!")

    # Create a cursor object
    cursor = connection.cursor()

    # Execute a query
    cursor.execute("SELECT * FROM sales;")
    result = cursor.fetchall()
    for row in result:
        print(row)

except pymysql.MySQLError as e:
    print("Error!!! Only Collins is authorized:", e)

finally:
    if 'connection' in locals() and connection.open:
        cursor.close()
        connection.close()
        print("Connection closed")
