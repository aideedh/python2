
# multiplication tables

# for number in range (1,4):
#     for times in range (1,4):
#         ans = number * times
#         print (f"{number} x {times} = {ans}" )

# x = 1
# for times in range(1,4):
#     test = x * times
#     print (f"{x} x {times} = {test}" )


ans = int(input("Number of rows: "))

# set up ans+1 because it starts at 1 or it will be 1 less row
for rows in range(1, ans+1):

    # set up space (user input - current itteration of rows)
    space = ans - rows
    # so if user = 6   current itteration = 1  so 6 - 1 = 5  than  " "*5 spaces infront 

    if rows % 2 != 0:
        print (" "*(space) + ("+"*((rows*2)-1)))
    else:
        print (" "*(space) + ("-"*((rows*2)-1)))


# # refrence used  : https://www.youtube.com/watch?v=ynEHb4kE6F0
# r = 9 
# for i in range (r):
#     print(" " *(r-i), "*"*(i*2+1))
