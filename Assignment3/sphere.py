# import turtle

# # set screen and back ground color
# screen = turtle.Screen()
# screen.bgcolor("aqua")

# # fixed the spelling error 
# myturtle = turtle.Turtle()
# myturtle.shape("turtle")
# myturtle.color("blue")

# num = 60

# # for loop to repeat code
# for loop in range (num, 0, -2):

#     # reposition the turtle
#     myturtle.penup()
#     myturtle.goto(0, -num)
#     myturtle.pendown()

#     # this will decrease the number of loops
#     # the lower it is the more space between circles
#     num -= 2

#     # function found trough googling
#     myturtle.circle(num)

# myturtle.penup()
# myturtle.forward(150)
# screen.exitonclick()


import turtle

# set screen and back ground color
screen = turtle.Screen()
screen.bgcolor("aqua")

# fixed the spelling error 
myturtle = turtle.Turtle()
myturtle.shape("turtle")
myturtle.color("blue")

num = 60

# for loop to repeat code
for loop in range (num, 0, -2):

    # this will decrease the number of loops
    # the lower it is the more space between circles
    num -= 2

    # function found trough googling
    myturtle.circle(num)

# move turtle away from sphere
myturtle.penup()
myturtle.forward(150)
screen.exitonclick()
