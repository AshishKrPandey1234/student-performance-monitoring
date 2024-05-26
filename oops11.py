class car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def display(self):
        print(self.make)
        print(self.model)
        print(self.year)
car1=car("Toyota","corolla","2020")
car1.display()
