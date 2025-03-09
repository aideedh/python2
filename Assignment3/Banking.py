
class Account:
    
    def __init__(self, accountType, minBalance, currentBalance):
        self.accountType = accountType
        self.minBalance = minBalance 
        self.currentBalance = currentBalance

    def withdraw(self, amount):
        
        if self.accountType == "chequing":
            overdraft = self.currentBalance - amount
            if overdraft < -1000:
                print(f"Sorry you have exceeded overdraft limit by : {overdraft}")
            else:
                self.currentBalance -= amount
                print(self.currentBalance)




class Chequing(Account):
    pass

class Savings(Account):
    pass