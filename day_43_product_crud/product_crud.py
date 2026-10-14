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

    def post (self,title=None,category=None,price=None,rating=None):

        query = """
            insert into product (title,category,price,rating) values (%s,%s,%s,%s)
        """

        values = [title,category,price,rating]

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

    def put(self,id=None,price=None,rating=None):

        query = """
                update product set price = %s , rating = %s where id = %s
            """

        values = [price,rating,id]

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