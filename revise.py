class Triangle:
    def __init__(self,a,b,c):
        self.side1=a
        self.side2=b
        self.side3=c
    def Perimeter(self):
        return self.side1+self.side2+self.side3
a=int(input())
b=int(input())
c=int(input())
t=Triangle(a,b,c)
print(t.Perimeter())