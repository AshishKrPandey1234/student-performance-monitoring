class Father:
    def __init__(self):
        print("father constructer called")
        #self.vehicles="scooter"
class son(Father):
    def __init__(self):
        print("son constructor called")
        self.vehicles="car"
s=son()
print(s. __dict__)
#since construcor is passed so priority of own property incerases than the father property
