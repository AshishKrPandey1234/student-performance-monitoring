#instance function :check object is of that class or not.
class Demo:
    pass
d1=Demo()
class Employee:
    '''this is employee class for mai9intaining employee data'''
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"name is {self.name} and age is {self.age}")
e1=Employee('jay',21)
e2=Employee('raj',23)
print(isinstance(e1,Employee))
print(isinstance(d1,Employee))