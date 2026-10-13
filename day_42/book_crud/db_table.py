from mysql.connector import connect

connection = connect (
    user = "root",
    password = "Password@123",
    host = "localhost",
    database = "book_db"

)

cursor = connection.cursor()

query = """
    create table book(
        id int auto_increment primary key,
        title varchar(200) not null,
        author varchar(200) not null,
        price decimal(8,2) default 0.00,
        pages int not null

    )
"""

cursor.execute(query)
