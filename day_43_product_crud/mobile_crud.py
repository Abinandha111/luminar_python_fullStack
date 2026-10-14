from mysql.connector import connect 


class MobileListCreateUpdateRetrieveDelete:

    def __init__(self,user,password):

        self.connection = connect(
            user = user,
            password = password,
            database = "mobile_db",
            host = "localhost"
        )

        self.cursor = self.connection.cursor()

    def post (self,**kwargs):

            keys = [k for k in kwargs.keys()]

            place_holder = ",".j(keys)

            query = f"""
                insert into mobile ({place_holder}) values (%s,%s,%s,%s,%s)

            """

            values = [v for v in kwargs.values()]

            self.cursor.execute(query,values)

            self.connection.commit()

    def get(self):
         query = "select * from mobile"

         self.cursor.execute(query)

         records = self.cursor.fetchall()

         for r in records:
              print(r)

    def retrieve(self,id=None):
         query = "select * from mobile where id = %s"

         values = [id]

         self.cursor.execute(query,values)

         record = self.cursor.fetchone()

         print(record)

    def put(self,id=None,**kwargs):

         
         place_holder=""

         for k in kwargs.keys():
              place_holder+=k+"=%s,"

         place_holder = place_holder.rstrip(",")
         query = f"update mobile set {place_holder} where id = %s"

         values = [v for v in kwargs.values]
         values.append(id)

         self.cursor.execute(query,values)

         self.connection.commit()

         print("updated.....")

    def delete(self,id=None):
         query = "delete from mobile where id = %s"

         values = [id]

         self.cursor.execute(query,values)

         self.connection.commit()

         
mobile_instance = MobileListCreateUpdateRetrieveDelete(user="root",password="Password@123")

# mobile_instance.post(name='Vivo V40',brand= 'Vivo', specs='256GB, 8GB RAM',price= 34999,rating= 4.3)

# mobile_instance.get()

# mobile_instance.retrieve(id=1)

# mobile_instance.put(id=1,specs='512GB, 16GB RAM',price=69999)

# mobile_instance.retrieve(id=1)

# mobile_instance.delete(id=2)

mobile_instance.get()

