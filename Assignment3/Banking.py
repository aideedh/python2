
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
        print(" ")
        print("-Trying to Withdraw-")
        print(" ")


        if self.currentBalance - amount < -self.overdraft:
            print(f"Sorry, your overdraft limit of (${self.overdraft}) has been exceeded")
            print(f"Your current balance is :{self.currentBalance}")
            print("-------------------------------------")
            print("We have increased your over draft limit by $200")
            self.overdraft += 200
            print(f"Your new limit is now {self.overdraft}")
            print(" ")


        else:
            self.currentBalance -= amount
            print(f"Withdrawl Successful - Updated Balance {self.currentBalance}")
            print(" ")



    def deposit(self, amount):
        self.currentBalance += amount
        print(" ")
        print(f"${amount} Deposit Successful - Updated Balance: {self.currentBalance}")
        print(" ")


    # display info methods

    def showBalance(self):
        return self.currentBalance
    def showActType(self):
        return self.accountType


class Chequing(Account):

    def __init__(self, currentBalance):
        super().__init__("chequing", currentBalance)
        self.overdraft = 1000

class Savings(Account):

    def __init__(self, currentBalance):
        super().__init__("savings", currentBalance)
        self.overdraft = 1200


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

        # choose account type
        accountType = int(input("What is your accountType: 1. Chequing or 2. Savings: "))
        print(" ")

        # Chequing Account

        if accountType == 1 or accountType == "Chequing":
            print("Chequing Account Choosen:")

            # set starting balance
            while True:
                currentBalance = int(input("What is your starting balance - minimun 500: "))  
                if currentBalance >= 500:
                    break
                print("Error: Minimum balance must be 500 or more.")  

            # create Chequing class instance               
            chequingAccount = Chequing(currentBalance)

            # create Person class instance
            name = input("Choose your account name: " )
            person = Person(name, chequingAccount)


            # do banking stuff
            print(" ")
            print(f"Hello {person.name}")
            print("What would you like to do?")

            while True:

                ans = int(input("1. Show Balnce 2. Show ActType 3. withdraw 4. Deposit 5. Exit: "))
                print(" ")
                if ans == 1:
                    print(f"Account balance: {person.account.showBalance()}")
                    print(" ")
                    continue
                elif ans == 2:
                    print(f"Account Type: {person.account.showActType()}")
                    print(" ")
                    continue
                elif ans == 3:
                    ans = int(input("How much do you want to withdraw? "))
                    person.account.withdraw(ans)
                    continue
                elif ans == 4:
                    ans = int(input("How much do you want to deposit? "))
                    person.account.deposit(ans)
                    continue
                elif ans == 5:
                    print("exiting app thank you!")
                    exit()

        # Savings Account

        else:
            print("Savings Account Choosen:")

            # set starting balance
            while True:
                currentBalance = int(input("What is your starting balance - minimun 500: "))  
                if currentBalance >= 500:
                    break
                print("Error: Minimum balance must be 500 or more.")   

            # create Savings class instance                
            savingsaccount = Savings(currentBalance)              

            # create Person class instance
            name = input("Choose your account name: " )
            person = Person(name, savingsaccount)


            # do banking stuff
            print(" ")
            print(f"Hello {person.name}")
            print("What would you like to do?")

            while True:

                ans = int(input("1. Show Balnce 2. Show ActType 3. withdraw 4. Deposit 5. 10 deposits 6. Exit: "))
                print(" ")
                if ans == 1:
                    print(f"Account balance: {person.account.showBalance()}")
                    print(" ")
                    continue
                elif ans == 2:
                    print(f"Account Type: {person.account.showActType()}")
                    print(" ")
                    continue
                elif ans == 3:
                    ans = int(input("How much do you want to withdraw? "))
                    person.account.withdraw(ans)
                    continue
                elif ans == 4:
                    ans = int(input("How much do you want to deposit? "))
                    person.account.deposit(ans)
                    continue
                elif ans == 5
                elif ans == 6:
                    print("exiting app thank you!")
                    exit()
        

# instance of Application

app = Application()
app.showMenu()


# not needed

# accountOne = Account("chequing", 600)
# accountTwo = Chequing(800)
# Adam = Person("Adam", accountTwo)

# print(Adam.account.showBalance())
# print(Adam.account.showActType())

# Adam.account.withdraw(5000)