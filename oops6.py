class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def CalculateArea(self):
        A= self.length*self.breadth
        print("Area is",A)
l=int(input("enter length of rectangle"))
b=int(input("enter breadth of rectangle"))
object=Rectangle(l,b)
object.CalculateArea()
    
    
