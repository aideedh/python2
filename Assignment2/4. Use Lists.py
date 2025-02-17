# Write a program to calculate standard deviation of a list of integers. 
# This program should use a function called Avg() that calculates and returns average of the list passed 
# as a parameter. 
# The main program passes that average to another function called sumSqDiff()
# that also accepts a list as an argument and returns the sum square of the difference of list values 
# and the average. sumSqDiff() implements this formula ssd





import math

def sumSqDiff(list):
   
   # set up formula variables 
    for number in list:       # xi - yes
        xi = number

    average = Avg(list)           # average - from avg function

    n = 0                     # n / count -  Total num of elements
    for number in list:
        n+=1

    ssd = (xi - average)**2       # ssd - Calculation
    
    stdDeviation = math.sqrt((ssd/n))

    print(stdDeviation)
    return ssd


def Avg(list):

    sum = 0
    count = 0

    # Thinking:
    # list passed as a paramenter
    # so the sum of the list must be done than divided by count of list

    for number in list:
        # calculate sum of nums in list
        sum+=number

    for number in list:
        # count amount of nums in list
        count+=1

    # calculate the Average
    return (sum / count)


# test avg
myList = [1,2,3,4]
print(Avg(myList))
myList = [1,2,3,4]
print(sumSqDiff(myList))