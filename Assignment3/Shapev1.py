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

# Move to draw the back square
myturtle.penup()
myturtle.right(45)
myturtle.forward(50)
myturtle.left(45)
myturtle.pendown()

for _ in range(4):
    myturtle.forward(100)
    myturtle.right(90)


myturtle.penup()
myturtle.right(45)
myturtle.backward(50)
myturtle.pendown()
myturtle.left(45)
myturtle.forward(100)

myturtle.penup()
myturtle.right(90)
myturtle.forward(100)
myturtle.pendown()
myturtle.right(45)
myturtle.forward(50)

myturtle.penup()
myturtle.right(135)
myturtle.forward(100)
myturtle.pendown()
myturtle.right(45)
myturtle.forward(50)

screen.exitonclick()
