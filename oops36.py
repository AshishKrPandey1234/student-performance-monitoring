class Rectangle:
    __length=0
    __breadth=0
    def __init__(self):
        self.__length=4
        self.__breadth=5
        print("length is",self.__length)
        print("breadth is",self.__breadth)
obj=Rectangle()
print(obj._Rectangle__length)
print(obj._Rectangle__breadth)