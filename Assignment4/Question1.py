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

with open("ApplicationLog.csv","r") as file:
    reader =csv.reader(file)
    for row in reader:
        print(row)


