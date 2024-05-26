class Employee:
    def __init__(self,salary,age):
        self.salary=salary
        self.age=age
    def display(self):
        print(f"salary is {self.salary} and age is {self.age}")
e1=Employee(64000,24)
e2=Employee(68000,25)
print(e1.salary)
e1.salary=72000#updation of salary
print(e1.salary)

