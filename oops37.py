class Employee:
    def __init__(self,sal,hrs):
        self.sal=sal
        self.hrs=hrs
    def get_info(self):
        return self.sal
    def Add_sal(self):
        if (self.sal<=500 and self.sal>=0):
            self.sal=self.sal+100
        return self.sal
sal=int(input("enter salary"))
hrs=int(input("enter hours "))
Emp1=Employee(sal,hrs)
print(Emp1.get_info())
print(Emp1.Add_sal())