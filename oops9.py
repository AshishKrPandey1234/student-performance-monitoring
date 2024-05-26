#bank account
class Bank:
    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.balance=balance
    def display_balance(self):
        print("acccount number",self.account_number)
        print("balance",self.balance)
account1=Bank(77866889,56763873576)
account2=Bank(74866889,56763873575)
account1.display_balance()
account2.display_balance()