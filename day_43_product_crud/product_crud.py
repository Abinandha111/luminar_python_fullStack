from mysql.connector import connect

class productListCreateUpdateRetrieveDelete:

    def __init__(self,user=None,password=None):

        self.connection = connect(
            user = user,
            password = password,
            database = "inventory_db",
            host = "localhost"
        )

        self.cursor = self.connection.cursor()

    def post (self,**kwargs):

        keys = [k for k in kwargs.keys()]

        place_holder=",".join(keys)

        query = f"""
            insert into product ({place_holder}) values (%s,%s,%s,%s)
        """

        values = [v for v in kwargs.keys()]

        self.cursor.execute(query,values)

        self.connection.commit()

    def get(self):
        query = "select * from product"

        self.cursor.execute(query)

        records = self.cursor.fetchall()

        for r in records:
            print(r)

    def retrieve(self,id=None):
        query = "select * from product where id = %s"

        values = [id]

        self.cursor.execute(query,values)

        record = self.cursor.fetchone()

        print(record)

    def put(self,id=None,**kwargs):

        place_holder=""

        for k in kwargs.keys():
            place_holder+=k+"=%s,"
        
        place_holder = place_holder.rstrip(",")

        query = f"""
                update product set {place_holder} where id = %s
            """

        values = [v for v in kwargs.values]
        values.append(id)

        self.cursor.execute(query,values)

        self.connection.commit()

        print("record updated....")

    def delete(self,id=None):
        query = "delete from product where id = %s"

        values = [id]

        self.cursor.execute(query,values)

        self.connection.commit()

product_instance = productListCreateUpdateRetrieveDelete(user="root",password="Password@123")


# product_instance.post(title="Bluetooth Speaker",category="Electronics",price=4500,rating=8.5)

# product_instance.retrieve(id=1)

# product_instance.put(id=1,price=2000,rating=6.8)

# product_instance.retrieve(id=1)

product_instance.delete(id=2)
product_instance.get()

#mobile 

# id,name,brand,specs,price,rating