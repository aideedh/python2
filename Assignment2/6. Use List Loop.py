# b) Write a program that uses a list called scores initialized with 10 values.
# The program iterates over the list and determines student’s grade for the given score, 
# as done in week3 lesson. Student must use elif construct to determine the grades based 
# on the following criteria: score>80 is grade A, score between 70 and 80 is grade B, 
# score between 60 and 70 is grade C, score between 50 and 60 is grade D and score less than 50 is grade D. 
# Use any loop of you choice. Student must provide a flowchart for this program


def Grade(list):
    # needs to have list parameter to pass any list rather than pre defined list
    # paramters make functions flexable
    
    average = Avg(list)

    if average > 80:
        grade = "A"
    elif average > 70 and average < 80 :
        grade = "B"
    elif average > 60 and average < 70 :
        grade = "C"
    elif average > 50 and average < 60 :
        grade = "D"
    else:
        grade = "F"

    return grade


def Avg(list):

    # calculate sum
    total = 0 
    for number in list:
        total+=number
    # get amount of elements in list
    elements = len(list)
    # calculate average
    score = (total/elements)
    
    return score


# Random list of grades for 2 students
scores = [96,90,82,92,76,64,75,81,90,72]
scores2 = [43,30,7,51,24,40,86,44,84,43]

print("Student 1 - Grade:", Grade(scores), "Average:", Avg(scores))
print("Student 2 - Grade:", Grade(scores2), "Average:", Avg(scores2))