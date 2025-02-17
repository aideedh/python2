# a)	Write a program that takes integer inputs from a user in a while loop in a variable called num
# and prints the value of num. The loop terminates if the user types a negative number. 
# The program should also count the number of times the loop iterates.
# Student should provide a flow chart for this problem

def huhu():

    loop = True
    count = 0
    value = 0 

    while loop:
        
        num = int(input("Enter a number: "))

        if num >= 0:
            # implement logic for if number is greater than 0 
            count+=1 
        else:
            # implement logic if number is negative / less than 0 
            print("Sorry, only numbers >= 0 are Allowed!")
            print("Terminating ... .. .")
            break

