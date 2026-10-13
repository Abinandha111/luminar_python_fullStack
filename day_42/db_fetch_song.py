from mysql.connector import connect

connection = connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="song_db"
)


cursor = connection.cursor()

query = """
    select * from song
"""
cursor.execute(query)

records = cursor.fetchall()

for r in records:
    print(r)