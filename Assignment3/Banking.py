
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

        if self.currentBalance - amount > self.overdraft:
            print("Sorry, your overdraft limit {self.overdraft} has been exceeded")
        else:
            self.currentBalance -= amount
            print(f"Withdrawl Successful - Updated Balance {self.currentBalance}")


            # this  is redundant logic ignore this just for future refrence

        # if self.accountType == "chequing":

        #     overdraft = -1000

        #     overdraftProtection = self.currentBalance - amount
        #     if overdraftProtection < overdraft:
        #         print(f"Sorry you have exceeded overdraft limit by : {overdraft}")
        #         overdraft +=200
        #         print("overdraft limit increased by 200")

        #     else:
        #         self.currentBalance -= amount
        #         print(f"Withdrawal successful!")
        #         print(f"New balance: {self.currentBalance}")

        # elif self.accountType == "savings":

        #     overdraft = -1200

        #     overdraftProtection = self.currentBalance - amount
        #     if overdraftProtection < overdraft:
        #         print(f"Sorry you have exceeded overdraft limit by : {overdraft}")
        #         overdraft +=200
        #         print("overdraft limit increased by 200")
        #     else:
        #         self.currentBalance -= amount
        #         print(f"Withdrawal successful!")
        #         print(f"New balance: {self.currentBalance}")


    def deposit(self, amount):
        self.currentBalance += amount



class Chequing(Account):

    def __init__(self, currentBalance):
        super.__init__(currentBalance)
        self.overdraft = -1000


class Savings(Account):

    def __init__(self, currentBalance):
        super.__init__(currentBalance)


accountOne = Account("chequing", 600)
Adam = Person("Adam", accountOne)