import turtle

screen = turtle.Screen()
screen.bgcolor("aqua")

myturtle = turtle.Turtle()
myturtle.shape = ("Turtle")
myturtle.color = ("Blue")


for loop in range (1,5):
    myturtle.forward(100)
    myturtle.right(90)

myturtle.left(45)
myturtle.forward(50)
myturtle.right(45)
myturtle.forward(60)



screen.exitonclick() 