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
   
   # average - from avg function
    average = Avg(list)

    # ssd = sum(xi - average)^2
    # set intial value to zero 
    # than calculate formula for each element
    ssd = 0           
    for xi in list:                         
        total = (xi - average)**2          
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


# set up list()
#myList = [1,2,3,4]

myList = []
for number in range [1,5]:
    ans = int(input("Input Number: "))
    myList.append = ans


print(f"Average: {Avg(myList)}")
print(f"Sum of Squared Differences: {sumSqDiff(myList)}")
print(f"Standard Deviation: {stdDeviation(myList)}")