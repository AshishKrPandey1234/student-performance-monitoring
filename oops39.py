#encapsulation using protected access specifier
class Employee:
    def __init__(self,name,sal):
        self._name=name
        self._sal=sal
class HR(Employee):
    def task(self):
        print(f"{self._name} will manage employee whose salary is {self._sal}")
obj=HR("Jury",40000)
print(obj._name)
obj.task()