class shape:
    def __init__(self,len,bred):
        self.len=len
        self.bred=bred
    def Perimeter(self):
        pass
class Rectangle(shape):
    def __init__(self,len,bred):
        super().__init__(len,bred)
    def Perimeter(self):
        return 2*(self.len+self.bred)
class Square(shape):
    def __init__(self,len):
        super().__init__(len,len)
    def Perimeter(self):
        return 4*self.len
s=Rectangle(6,4)
s1=Square(6)
print("perimeter of square",s.Perimeter())
print("perimeter of square" ,s1.Perimeter())    