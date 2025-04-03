'''
1. Write a Python program that reads data from the file "ApplicationLog.csv"
and extracts the date and time of all entries labeled as "Universal Print”
The program should format the output as:
hours:seconds \t day:month:year
Each numeric value in the output should be right-aligned within a 6-character space. 
Additionally, provide a flowchart that illustrates your program's logic.
'''

# refrence:
# https://www.youtube.com/watch?v=1IYrmTTKOoI

import csv

# this will open and read the file
with open("ApplicationLog.csv","r") as file:
    reader = csv.reader(file)
    header = next(reader)

# check the rows
    for row in reader:

        # try to check 
        try:
            if row[2] == "Universal Print":

                # split the info
                datetime = row[1].split()
                date = datetime[0].split("-")  
                clock = datetime[1].split(":")

                # format the info
                hourSecond = f"{clock[0]}:{clock[2]}"
                formattedDate = f"{date[2]}:{date[1]}:{date[0]}"

                # display the info
                print(row[2], f"{hourSecond} \t {formattedDate}")

        # if i dont have this it will crash 
        except IndexError:
            pass

