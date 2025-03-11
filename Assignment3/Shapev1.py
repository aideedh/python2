import turtle

# this program will make a cube

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


# Reposition to the bottom left corner  of first sq
myturtle.left(45)
myturtle.forward(100)
myturtle.right(90)
myturtle.forward(100)

# draw sq behind front sq
myturtle.right(135)
myturtle.forward(50)
myturtle.right(45)
myturtle.forward(100)
myturtle.right(135)
myturtle.forward(50)



screen.exitonclick()
