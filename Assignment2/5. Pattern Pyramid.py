
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

for rows in range(1, ans+1):

    space = ans - rows
    if rows % 2 != 0:
        print (" "*(space) + ("+"*((rows*2)-1)))
    else:
        print (" "*(space) + ("-"*((rows*2)-1)))
