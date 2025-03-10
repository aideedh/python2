
class Person:
    
    # is a relationshiop
    def __init__(self, name, account):
        self.name = name
        self.account = account


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


class Chequing(Account):

    def __init__(self, currentBalance):
        super.__init__(currentBalance)
        self.overdraft = -1000


class Savings(Account):

    def __init__(self, currentBalance):
        super.__init__(currentBalance)


accountOne = Account("chequing", 600)
Adam = Person("Adam", accountOne)