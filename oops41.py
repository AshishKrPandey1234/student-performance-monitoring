class cat:#created class
    def __init__(self,name,age):#parameterized constructor
        self.name=name
        self.age=age
    def info(self):
        print("I am a Cat")
    def sound(self):
        print("meow")
class Dog:#created another class
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print("I am a dog")
    def sound(self):
        print("bark")
C=cat("Kitty",2)#object of class1
D=Dog("Oreo",4)#"   "   of class2
for i in (C,D):
    i.sound()
    i.info()
    #i.sound()


