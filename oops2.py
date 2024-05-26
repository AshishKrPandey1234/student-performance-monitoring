#non parameterized constructor maam say it is default parameter
#default parameter
class Employee:
    def __init__(self):
        self.name="Ashish"
        self.age=25
e1=Employee()
e2=Employee()
print(e1.__dict__)
print(e2.__dict__)