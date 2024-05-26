#for 3 employee
class Employee:
    def __init__(self):
        self.name=input("enter name")
        self.age=int(input("enter age"))
        self.salary=int(input("enter salary"))
    def display(self):
        print(self.name)
        print(self.age)
        print(self.salary)
Employee1=Employee()
Employee2=Employee()
Employee1.display()
Employee2.display()