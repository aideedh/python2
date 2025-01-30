'''
4.	User inputs and concatenation
Write a program called greet.py  that asks the user to type their name and store it in a 
variable called name. The program should print a greeting for the user. For example if the 
user’s name is Joe, the program should print “ Good Morning Joe”.  Use comments wherever applicable. 
Explain your logic. Create a version2 of this problem in your git repository.
 In version2 you should print the message three times. 
 Give screenshots of the code, outputs and the git repository
'''

#v1

name = input("What is your name: ")
print (f"Good Morning {name}") # or print("Good Morning" + str(name))


#v2

#for loop
name = input("What is your name: ")
for loop in range(1,4):
    print("Good Morning " + str(name))

# While loop
count = 1
name = input("What is your name: ")
while count <= 3:
    print ("Good morning", (name))
    count+=1
