
class Person:
    
    # is a relationshiop
    def __init__(self, name, account):
        self.name = name
        self.account = account


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
                overdraft +=200
                print("overdraft limit increased by 200")

            else:
                self.currentBalance -= amount
                print(f"Withdrawal successful!")
                print(f"New balance: {self.currentBalance}")

        elif self.accountType == "savings":

            overdraft = -1200

            overdraftProtection = self.currentBalance - amount
            if overdraftProtection < overdraft:
                print(f"Sorry you have exceeded overdraft limit by : {overdraft}")
                overdraft +=200
                print("overdraft limit increased by 200")
            else:
                self.currentBalance -= amount
                print(f"Withdrawal successful!")
                print(f"New balance: {self.currentBalance}")


    def deposit(self, amount):
        self.currentBalance += amount



class Chequing(Account):
    pass


class Savings(Account):
    pass