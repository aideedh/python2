import turtle

screen = turtle.Screen()
screen.bgcolor("aqua")

myturtle = turtle.Turtle()
myturtle.shape = ("Turtle")
myturtle.color = ("Blue")

# Draw the front square
for loop in range(1,5):
    myturtle.forward(100)
    myturtle.right(90)

# Draw the back Square
myturtle.left(45)
myturtle.forward(50)
myturtle.right(45)

for _ in range(4):
    myturtle.forward(100)
    myturtle.right(90)

# draw Top squre
myturtle.penup
myturtle.forward(100)
myturtle.right(90)
myturtle.right(45)
myturtle.forward(50)






screen.exitonclick()
