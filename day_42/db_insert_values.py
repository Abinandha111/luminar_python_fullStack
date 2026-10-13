from mysql.connector import connect

connection = connect (
    user = "root",
    password = "Password@123",
    host="localhost",
    database = "song_db"
)

cursor = connection.cursor()

query = """

    insert into song(title,singers,track_num,duration) values (%s,%s,%s,%s)

                                                            
"""
values = ["stay","Justin Bieber",1,2.5]

cursor.execute(query,values)

connection.commit()