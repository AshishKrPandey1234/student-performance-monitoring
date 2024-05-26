import math
class circle:
    def __init__(self,radius):
        self.radius=radius
    def CalculateArea(self):
        return math.pi*self.radius**2
r=int(input("enter radius of circle"))
circle1=circle(r)
print("area of circle",circle1.CalculateArea())