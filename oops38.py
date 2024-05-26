class Animal:
    name=" "
    def eat(self):
        print("I can eat fruits")
class Dog(Animal):
    def sleep(self):
        print(self.name,"can sleep for 6 hrs")
Labroder=Dog()
Labroder.name="Oreo"
Labroder.eat()
Labroder.sleep()
