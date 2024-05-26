class Human(object):
    def __init__(self):
        print("human being constructor called")
        self.name=input("enter name of employee ")
        print(self.name)
class Employee(Human):
    pass
class manager(Employee):
    pass
m1=manager()