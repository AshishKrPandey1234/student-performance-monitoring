'''built in class attribute are: __dict__,__doc__,__name__,__module__,__bases__'''
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

e1 = Employee('jay', 21)
e2 = Employee('raj', 23)

print(Employee.__doc__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
