#default  parametrized
#phone
class Phone:
    def __init__(self):
        self.brand=input("enter name of brand")
        self.model=input("enter model name")
        self.price=int(input("enter price of phone"))
    def display(self):
        print(f"welcome to {self.brand}")
        print(f"{self.brand} {self.model}")
        print(f"price of phone is ",self.price)
phone1=Phone()
phone1.display()