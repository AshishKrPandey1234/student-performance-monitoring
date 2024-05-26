class Student:
    def __init__(self,nm,ag):
        self.name=nm
        self.age=ag
std1=Student('Akshay',89)
std2=Student('Raj',90)
std3=Student('aman',94)
std1.age=25#so we can update the value of student1
print(std1.__dict__)