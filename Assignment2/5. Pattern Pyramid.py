
# multiplication tables

# for number in range (1,4):
#     for times in range (1,4):
#         ans = number * times
#         print (f"{number} x {times} = {ans}" )

# x = 1
# for times in range(1,4):
#     test = x * times
#     print (f"{x} x {times} = {test}" )



for rows in range (1,5):
    if rows % 2 != 0:
        print ("+"*rows)
    else:
        print ("-"*rows)
