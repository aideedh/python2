
class Person:
    pass




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
                print(f"Withdrawal successful!")
                print(f"New balance: {self.currentBalance}")




class Chequing(Account):
    super.withdraw(self)


class Savings(Account):
    pass