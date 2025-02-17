# Write a program to calculate standard deviation of a list of integers. 
# This program should use a function called Avg() that calculates and returns average of the list passed 
# as a parameter. 
# The main program passes that average to another function called sumSqDiff()
# that also accepts a list as an argument and returns the sum square of the difference of list values 
# and the average. sumSqDiff() implements this formula ssd





import math


def stdDeviation(list):
    # passed the peremeter for list to get the number of elments in the list

    count = 0

    # count number of elements in list
    for number in list:
        count+=1

    # calculate standard deviation
    stdDevi = math.sqrt((sumSqDiff(list)/count))
    
    return stdDevi



def sumSqDiff(list):
   
   # set up formula variables 
    average = Avg(list)                    # average - from avg function

    ssd = 0                                # ssd = sum(xi - average)^2         
    for xi in list:                        # set intial value to zero 
        total = (xi - average)**2            # than calculate formula for each element
        ssd+=total

    return ssd


def Avg(list):

    total = 0
    count = 0

    # Thinking:
    # list passed as a paramenter
    # so the sum of the list must be done than divided by count of list

    for number in list:
        # calculate sum of nums in list
        total+=number

    for number in list:
        # count amount of nums in list
        count+=1

    # calculate the Average
    return (total / count)


# test avg
myList = [1,2,3,4]
print(Avg(myList))
print(sumSqDiff(myList))
print(stdDeviation(myList))