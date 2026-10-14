from mysql.connector import connect

class AssesPro:

    def __init__(self,user=None,password=None):

        self.connection = connect(
            user=user,
            password=password,
            database="assesment_db",
            host="localhost"
        )

        self.cursor = self.connection.cursor()

    def post(self,**kwargs):

        keys = [k for k in kwargs.keys()]

        place_holder = ",".join(keys)

        query = f"insert into assesment ({place_holder}) values (%s,%s,%s,%s)"

        values = [v for v in kwargs.values()]

        self.cursor.execute(query,values)

        self.connection.commit()

    def get(self):

        query="select * from assesment"

        self.cursor.execute(query)

        records = self.cursor.fetchall()

        for i in records:
            print(i)

    def put(self,id=None,**kwargs):
        place_holder=""

        for k in kwargs.keys():
            place_holder+=k+"=%s,"

        place_holder=place_holder.rstrip(",")

        query = f"update assesment set {place_holder} where id = %s"

        values = [v for v in kwargs.values()]
        values.append(id)

        self.cursor.execute(query,values)

        self.connection.commit()
        print("record updated......")
asses_instance = AssesPro(user="root",password="Password@123")

# asses_instance.post(title="mysql_main_exam",batch="django_june",start_date="2026-12-20",duration=2)

asses_instance.get()


# asses_instance.put(id=2,start_date="2026-12-10")