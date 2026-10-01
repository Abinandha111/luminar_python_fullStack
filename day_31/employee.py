class Employee:

    name:str
    emp_id:int
    department:str
    experience:int
    salary:int

    def work(self):

        print("working.....")

    def attend_meeting(self):

        print("meetting method....")

    def complete_task(self):

        print("complete task method.....")


emp_instance = Employee()

emp_instance2 = Employee()

emp_instance.attend_meeting()

emp_instance2.complete_task()

