# Write a program that uses for loop to calculate the magnitude of a vector, where all dimensions (x,y,z)  
# of the vector are integers entered by the user. Flowchart is required in this program.

def calcMagnitude():

    # set variables to default value so it will still run
    x = 1
    y = 1 
    z = 1 
    # or x = y = z = 1

    for loop in range (1,4):
        # will loop this 3 times 
        ans = int(input("Please enter a number"))

        # first loop, it will assign value to x
        if loop == 1:
            x = ans
        # second loop, it will assign value to y
        elif loop == 2:
            y = ans
        # last loop, it will assign value to z
        else:
            z = ans

        