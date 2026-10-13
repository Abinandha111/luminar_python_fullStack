from mysql.connector import connect

connection = connect (
    user = "root",
    password = "Password@123",
    host = "localhost",
    database = "book_db"

)

cursor = connection.cursor()

query = """

    insert into book (title,author,price,pages) values (%s,%s,%s,%s)

"""

values =["Legends & Lattes","Travis Baldree",650,790]

cursor.execute(query,values)

connection.commit()