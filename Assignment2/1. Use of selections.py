# Write a program that would use nested if /if-else. 
# In this program a variable called temper stores a randomly generated number between 1 and 400. 
# If the generated value is above 100, the program prints “ temperature above boiling point” 
# and uses a second if to check whether the temper is above 320 degrees;
# in that case the program prints “temperature above smoke point”. 
# For temper lower than 100 the program prints “ temperature is not very high”. 
# Flowchart is required in this program. 
# Student should also suggest what are some of the weaknesses in this problem


import random

def tempCheck():

    # prints temp
    temper = random.randint(1, 400)

    # if temp is above 100
    if temper > 100:
        # this will be blank ( due to nested if )
        if temper > 320:
            # if temp above 320 bellow will print
            print ("Temperature:", temper)
            print ("Temperature above smoke point")

        else: 
            # if temp is not above 320 it will use else
            print ("Temperature:", temper)
            print("Temperature above boling point!")

    # if temp is bellow 100
    elif temper < 100:
        print("Temperature:", temper)
        print("Temperature is not very high")

# Loop to run the program x amount of times 
for loop in range (1, 4):
    print("--------------------------------")
    tempCheck()
print("--------------------------------")