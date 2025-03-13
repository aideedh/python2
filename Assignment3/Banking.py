
class Person:
    
    # is a relationshiop
    def __init__(self, name, account):
        self.name = name
        self.account = account

"""
Note to self:
Inheritance means to remove the need for unseesary code
When it says child class inherits parent methods, it means the child class 
can reuse the metods of the parent class with out needed to copy and paste code
"""


class Account:
    
    def __init__(self, accountType, currentBalance, minBalance=500, overdraft = 0):
        self.accountType = accountType
        self.currentBalance = currentBalance
        self.minBalance = minBalance
        self.overdraft = overdraft


    def withdraw(self, amount):
        
        print("-Trying to Withdraw-")

        if self.currentBalance - amount < -self.overdraft:
            print("Sorry, your overdraft limit {self.overdraft} has been exceeded")
            self.overdraft += 200
        else:
            self.currentBalance -= amount
            print(f"Withdrawl Successful - Updated Balance {self.currentBalance}")


    def deposit(self, amount):
        self.currentBalance += amount
        print(f"${amount} Deposit Successful - Updated Balance: {self.currentBalance}")

    # display info methods

    def showBalance(self):
        return self.currentBalance
    def showActType(self):
        return self.accountType


class Chequing(Account):

    def __init__(self, currentBalance):
        super().__init__("chequing", currentBalance)
        self.overdraft = -1000



class Savings(Account):

    def __init__(self, currentBalance):
        super().__init__("savings", currentBalance)
        self.overdraft = -1200


    # add the profit method
    def profit(self):
        profit = self.currentBalance * 0.15
        self.currentBalance += profit


accountOne = Account("chequing", 600)
accountOn = Chequing()
Adam = Person("Adam", accountOne)

print(Adam.account.showBalance())
print(Adam.account.showActType())