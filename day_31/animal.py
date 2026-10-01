

class Animal:

    breed:str
    color:str
    height:int
    weight:int

    def eat(self):

        print("eat....")

    def sleep(self):

        print("sleep....")

animal_instance = Animal()

animal_instance2 = Animal()

animal_instance.sleep()

animal_instance2.eat()


