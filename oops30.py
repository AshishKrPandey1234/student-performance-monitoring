#super function
class computer(object):
    def __init__(self):
        self.ram='8gb'
        self.storage='512 gb'
        print("computer class constructor called")
class mobile(computer):
    def __init__(self):
        super().__init__()
        self.model='iphone x'
        print("mobile class constructor called")
Apple=mobile()
print(Apple.__dict__)