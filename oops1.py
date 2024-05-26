#parameterized constructor
class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name,end="   ")
        print(self.age)
e1=Employee("ashish",25)
e2=Employee("Amit",23)
e1.display()
e2.display()

