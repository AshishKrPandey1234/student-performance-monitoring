#student
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name)
        print(self.age)
student1=Student("ashish" ,18)
student1.display()