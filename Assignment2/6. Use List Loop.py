# b) Write a program that uses a list called scores initialized with 10 values.
# The program iterates over the list and determines student’s grade for the given score, 
# as done in week3 lesson. Student must use elif construct to determine the grades based 
# on the following criteria: score>80 is grade A, score between 70 and 80 is grade B, 
# score between 60 and 70 is grade C, score between 50 and 60 is grade D and score less than 50 is grade D. 
# Use any loop of you choice. Student must provide a flowchart for this program


def Grade():
    
    average = Avg(scores)

    if average > 80:
        print("Grade: A")
    elif average > 70 and average < 80 :
        print("Grade: B")
    elif average > 60 and average < 70 :
        print("Grade: C")
    elif average > 50 and average < 60 :
        print("Grade: D")
    else:
        print("Grade: D")


def Avg(list):

    # calculate sum
    total = 0 
    for number in list:
        total+=number
    # get amount of elements in list
    elements = len(list)

    score = (total/elements)
    
    return score



scores = [96,90,82,92,76,64,75,81,90,72]

print(Grade())