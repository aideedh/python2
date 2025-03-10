
class Person:
    pass




class Account:
    
    def __init__(self, accountType, minBalance, currentBalance):
        self.accountType = accountType
        self.minBalance = minBalance 
        self.currentBalance = currentBalance

    def withdraw(self, amount):
        
        if self.accountType == "chequing":

            overdraft = -1000

            overdraftProtection = self.currentBalance - amount
            if overdraftProtection < overdraft:
                print(f"Sorry you have exceeded overdraft limit by : {overdraft}")
            else:
                self.currentBalance -= amount
                print(f"Withdrawal successful!")
                print(f"New balance: {self.currentBalance}")

        elif self.accountType == "savings":
            




class Chequing(Account):
    super.withdraw(self)


class Savings(Account):
    pass