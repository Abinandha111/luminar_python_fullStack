

class Student:

    name:str
    roll_no:str
    age:str

    def submit_assignment(self):

        print("complete assignment....")

    def attend_class(self):

        print("attend class......")

    def eat(self):

        print("eat....")

student_instance = Student()

student_instance2 = Student()

student_instance.attend_class()

student_instance2.submit_assignment()

student_instance.eat()