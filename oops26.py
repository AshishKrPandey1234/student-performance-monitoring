class Bank:
    bank_name="bank of india"
    rate=3.47
    @staticmethod#now i can access rate from class which is class variable
    def simpleinterest(p,t):
        si=p*t*Bank.rate
        print(si)
p=float(input("enter principal"))
t=int(input("enter time"))
Bank.simpleinterest(p,t)