class vehicles:#created class
    def __init__(self,mxspeed,milg):#constructor
        self.mxspeed=mxspeed#instance variable
        self.milg=milg#instance variable
        self.color="white"
        def capacity(self):
            return self.cap
        def display(self):
            print(self.mxspeed)
            print(self.milg)
car1=vehicles(240,12)
car2=vehicles(220,13)
car1.display()
car2.display()
print(car2.capacity(7))
print(car2.capacity(5))