# b) Use version management with git and make the following changes to the program in part a: 
# The loop breaks if the user types your student number print the message “ cutoff point”. 
# The loop should skip the statements in current iteration and does not increment count whenever 
# the user types a multiple of 11. Flowchart is required for this program

def huhu():

    loop = True
    count = 0
    sum = 0 

    while loop:
        # user input in while loop
        num = int(input("Enter a number: "))

        if num >= 0:
            # implement logic for if number is greater than 0 
            count+=1
            sum+=num  # sum of all positive user inputs
        else:
            # implement logic if number is negative / less than 0 
            print("Sorry, only numbers >= 0 are Allowed!")
            print("Terminating ..... ... .. .")
            break

    # loop termination logic 
    print("-------------------------------")
    print("Total loop iterations:", count)

    return sum  

# call function and than print information 
print("Sum of all positive numbers:", huhu())
print("-------------------------------")
