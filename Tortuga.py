from turtle import *

screen = Screen()
screen.bgcolor("lightblue")
screen.title("my name")
screen.setup(width = 1000,height = 500)

tortuga1 = Turtle()
tortuga1.shape("turtle")
tortuga1.color("Green")


tortuga1.penup()
tortuga1.goto(-400,150)
tortuga1.pd()
tortuga1.forward(150)
tortuga1.backward(75)
tortuga1.right(90)
tortuga1.forward(150)
tortuga1.circle(-50,180)

tortuga1.pu()
tortuga1.goto(-150,150)

tortuga1.pd()
tortuga1.goto(-250,-50)
tortuga1.goto(-150,150)
tortuga1.goto(-50,-50)
tortuga1.goto(-150,150)
tortuga1.goto(-225,0)
tortuga1.goto(-75,0)

























screen.exitonclick()