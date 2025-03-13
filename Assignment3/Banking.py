
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
            print(f"Sorry, your overdraft limit of (${self.overdraft}) has been exceeded")
            print(f"Your current balance is :{self.currentBalance}")
            print("-------------------------------------")
            print("We have increased your over draft limit by $200")
            self.overdraft += 200
            print(f"Your new limit is now {self.overdraft}")

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



class Application:

    # this will be the interaction between person and the bank 

    def showMenu(self):

        print("--------------------------")
        print("Welcme to the banking app!")
        print("--------------------------")

        # get all info for Account Type 

        accountType = int(input("What is your accountType: 1. Chequing or 2. Savings"))
        if accountType == 1 or accountType == "Chequing":
            print("Chequing Account Choosen:")
            currentBalance = int("What is your starting balance - minimun 500: ")                   
            chequingAccount = Chequing(currentBalance)

            name = str(input("Choose your account name"))




        else:
            print("Savings Account Choosen:")
            currentBalance = int("What is your starting balance - minimun 500: ")     
            savingsaccount = Savings(currentBalance)              

            name = str(input("Choose your account name"))
        

    pass


accountOne = Account("chequing", 600)
accountTwo = Chequing(800)
Adam = Person("Adam", accountTwo)

print(Adam.account.showBalance())
print(Adam.account.showActType())

Adam.account.withdraw(5000)