import turtle

# this program will make a cube

screen = turtle.Screen()
screen.bgcolor("white")

myturtle = turtle.Turtle()
myturtle.shape("turtle")
myturtle.color("blue")

# Draw the front square
for loop in range(1,5):
    myturtle.forward(100)
    myturtle.right(90)

# Draw the back Square
myturtle.color("Red")
myturtle.left(45)
myturtle.forward(50)
myturtle.right(45)

myturtle.color("yellow")
for _ in range(4):
    myturtle.forward(100)
    myturtle.right(90)

# draw Top squre
myturtle.color("green")
myturtle.penup
myturtle.forward(100)
myturtle.right(90)
myturtle.right(45)
myturtle.forward(50)


# Reposition to the bottom left corner  of first sq
myturtle.color("black")
myturtle.left(45)
myturtle.forward(100)
myturtle.right(90)
myturtle.forward(100)

# draw sq behind front sq
myturtle.color("pink")
myturtle.right(135)
myturtle.forward(50)
myturtle.right(45)
myturtle.forward(100)
myturtle.right(135)
myturtle.forward(50)

# move turtle away from cube

myturtle.penup()
myturtle.forward(50) 

screen.exitonclick()
