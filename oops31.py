class Human(object):
    def __init__(self):
        print("human being constructor called")
        self.name=input("enter your name")
class Employee(Human):
    def __init__(self):
        print("employee constructor called")
        self.salary=float(input("enter alary of employee"))
class managers(Employee):
    def __init__(self):
        print("manager constructor called")
        self.bonus=float(input("enter bonus of employee"))
m1=managers()
print(m1.__dict__)