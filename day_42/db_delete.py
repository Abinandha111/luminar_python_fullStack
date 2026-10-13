from mysql.connector import connect

connection = connect(
    user = "root",
    host = "localhost",
    password = "Password@123",
    database = "song_db"
)

cursor = connection.cursor()

query = "delete from song where id = %s"

values = [1]

cursor.execute(query,values)

connection.commit()
# book 

# db,table,insert,list,retrieve,update,delete