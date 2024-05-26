class Base: #created base class
    def __init__(self):#non parameterized constructor(special method)
        self._a=2#instance variable
class Derived(Base):#child class 
    def __init__(self):#non parameterized constructor
        Base.__init__(self)#method without parameter
        print(self._a)
obj=Derived()
print(obj._a)
obj1=Base()
print(obj1._a)
