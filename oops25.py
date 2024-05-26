class Employee:
    def setname(self,nm):
        self.name=nm
    def getname(self):
        print("the name is :",self.name)
e1=Employee()
e2=Employee()
e1.setname(input("enter name"))
e2.setname(input("enter Name"))
print("e1 is object",e1.__dict__)
print("e2 is object is:",e2.__dict__)
e1.getname()
e2.getname()