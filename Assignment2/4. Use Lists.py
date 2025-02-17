# Write a program to calculate standard deviation of a list of integers. 
# This program should use a function called Avg() that calculates and returns average of the list passed 
# as a parameter. 
# The main program passes that average to another function called sumSqDiff()
# that also accepts a list as an argument and returns the sum square of the difference of list values 
# and the average. sumSqDiff() implements this formula ssd



def Avg(list):

    sum = 0
    count = 0

    for number in list:
        # calculate sum of nums in list
        sum+=number

    for number in list:
        # count amount of nums in list
        count+=1

    # calculate the Average
    return (sum / count)




