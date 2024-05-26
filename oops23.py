class Employee:
    company_name="infosys"
    def __init__(self,name,sal):
        self.name=name
        self.salary=sal
e1=Employee("Ashish",56000)
e2=Employee("vikash",50000)
print(Employee.company_name)
print(e1.company_name)