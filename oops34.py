class BMW:
    def fuel_type(self):
        print("Diesel")
    def max_speed(self):
        print("maximum speed is 200")
class Ferrari:
    def fuel_type(self):
        print("petrol")
    def max_speed(self):
        print("maximum speed is 220")
def car_details(obj):
    obj.fuel_type()
    obj.max_speed()
bmw=BMW()
ferrari=Ferrari()
car_details(bmw)
car_details(ferrari)