import turtle

screen = turtle.Screen()
screen.bgcolor("aqua")

myturtle = turtle.Turtle()
myturtle.shape = ("Turtle")
myturtle.color = ("Blue")

num = 60

for loop in range (num, 0, -2):
    num -= 2
    myturtle.circle(num)
    myturtle.left(90)
    myturtle.forward(1)


screen.exitonclick()
