#for 50 employee
class Employee:
    def __init__(self):
        self.name=input("enter name of employee")
        self.age=int(input("enter age"))
        self.salary=int(input("enter salary"))
    def display(self):
        print(self.name)
        print(self.age)
        print(self.salary)
employees=[]
for i in range(2):
    employee=Employee()
    employees.append(employee)
for emp in employees:
    emp.display()
