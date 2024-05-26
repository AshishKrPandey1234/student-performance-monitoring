'''four built in class function are getattr(),setattr,delattr(),hasattr()'''
class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
e1=Employee('raj',21)
e2=Employee('jay',22)
print(getattr(e1,'age'))#we will get the value of e1 as output
print(setattr(e2,'name','Ashish'))#we will change the name from raj to ashish
print(e2. __dict__)
delattr(e2,'age')#it will delete age from e2
hasattr(e1,'name')#it will print name from e1
print(e1. __dict__)
print(e2. __dict__)
