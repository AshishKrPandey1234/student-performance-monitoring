class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def CalculateArea(self):
        return self.length*self.breadth
l=int(input("enter length of rectangle"))
b=int(input("enter breadth of rectangle"))
object=Rectangle(l,b)
print("Area is",object.CalculateArea())
    
    
