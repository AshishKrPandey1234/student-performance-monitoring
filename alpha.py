class Employee:
    def __init__(self,nm,sal):
        self.name=nm
        self.salary=sal
    def getName(self):
        return self.name
    def getSalary(self):
        return self.salary
class sales(Employee):
    def __init__(self,nm,sal,inc):
        super().__init__(nm,sal)#due to this we do not have take input self.name and self.sal in sale class
        self.increment=inc
    def getSalary(self):
        return self.salary+self.increment
e1=Employee("rakeh", 65520)
s1=sales("Ashish", 66202, 1000)
print((f"total salary for {e1.getName()} is rs. {e1.getSalary()}"))
print(f"total salary for {s1.getName()} is rs.{s1.getSalary()}")