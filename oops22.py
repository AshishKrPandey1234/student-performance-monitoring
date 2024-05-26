class student:
    def __init__(self,nm,m):
        self.name=nm
        self.marks=m
    def display(self):
        print(self.name,self.marks)
    def change_data(self):
        self.name='deepak'
        self.marks=94
std1=student('Ashish',93)
std2=student('Abhay',89)
std3=student('jay',84)
std2.change_data()
print(std2.__dict__)
