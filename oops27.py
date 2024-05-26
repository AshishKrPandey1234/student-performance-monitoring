#inheritance is the capability of one class to derive proprty from another class 
class Employee:
    bonus=2000
    def display(self):
        print("this is employee class")
class manager(Employee):
    bonus1=5000
    def show(self):
        print("this is manager mathod")
e1=Employee()
m1=manager()
e1.display()
m1.show()
print(m1.bonus1)
print(e1.bonus)