import json

# Dictionary 

PhoneBook = {
    'John': ('209 Trafalgar Road', '905-666-7777'),  
    'Rosie': ('1439 Trafalgar Road', '487-423-7721'),
    'Alex': ('12 Lakeshore Blvd', '416-555-1234'),
    'Samantha': ('300 King Street West', '647-888-9999'),
    'David': ('55 Bloor Street East', '905-222-1111'),
    'Emily': ('789 Queen Street', '289-333-4444'),
    'Michael': ('99 Dundas Street West', '416-777-8888'),
    'Olivia': ('150 Front Street', '437-555-0000')
}


# create file
with open("speeddial2.json", "w") as file:
    # indent will make it formated line by line instead of string
    json.dump(PhoneBook, file, indent=4)

# read file
with open("speeddial2.json", "r") as file:
    info = file.read()
    print(info)