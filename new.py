class sunday:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.color = "white"  # Setting default value for color
    
    def display(self):
        print(self.name)
        print(self.id)
        print(self.color)

a = input("Enter name: ")
b = int(input("Enter ID: "))
obj = sunday(a, b)
obj.display()
