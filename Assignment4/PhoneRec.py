
'''
2.	Write a Python program that reads phone numbers from a dictionary called phonebook 
and writes them to a file named "SpeedDial1.txt", with each phone number appearing 
in a single-column format (one number per line).

The dictionary follows this structure:
phonebook = {  
    'John': ('209 Trafalgar Road', '905-666-7777'),  
    'Rosie': ('1439 Trafalgar Road', '487-423-7721')  
}
(You may add more entries to the dictionary.)
Create a Git repository for this project.
Name the Python file "PhoneRec.py" and mark it as Version 1 in your Git history.
'''


# refrence:
# https://www.youtube.com/watch?v=1IYrmTTKOoI -  WRITE FILES using Python! (.txt, .json, .csv) ✍ 
# https://www.youtube.com/watch?v=Uh2ebFW8OYM - Python Tutorial: File Objects - Reading and Writing to Files

# useful:
# https://www.youtube.com/watch?v=MZZSMaEAC2g - Python dictionaries are easy 📙  min 5:00
# https://www.geeksforgeeks.org/write-a-dictionary-to-a-file-in-python/ 
# https://www.geeksforgeeks.org/how-to-print-a-dictionary-in-python/



# first need to create the dictionary 

PhoneBook = {
    'John': ('209 Trafalgar Road', '905-666-7777'),  
    'Rosie': ('1439 Trafalgar Road', '487-423-7721')  
}

# create file

# ---------------------------------------------------------------------------
# This method is using tuple unpacking not learned in class so i wont use it
# ---------------------------------------------------------------------------
# with open("SpeedDial1.txt", "w") as file:   
#     for key, (value1, value2) in PhoneBook.items():
#         file.write(f"{key}, {value1}, {value2} \n")
# ---------------------------------------------------------------------------

with open("SpeedDial1.txt", "w") as file:
    
    for key, value in PhoneBook.items():

        address = value[0]
        phone = value[1]

        # file only takes 1 arg so need to use f
        file.write(f"{key}: ({address}, {phone}) \n")



# print message to confirm file created
print("File created ... .. .")

# read all lines in the file
with open("SpeedDial1.txt", "r") as file:
    info = file.read()
    print(info)
