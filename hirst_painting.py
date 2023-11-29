"""HIRST PAINTING"""
# 10 x 10 size: 20 paces: 50
from random import randint
from turtle import Turtle, Screen
from important import random_color
colors = []
for i in range(100):
    colors.append(random_color())
brush = Turtle()
screen = Screen()
brush.speed(0)
brush.penup()
brush.hideturtle()
brush.setpos(-240, -260)
for i in range(10):
    for j in range(10):
        brush.dot(20, colors[i*10 +j])
        brush.forward(50)
    brush.setpos(-240, -260 + 50 * (i + 1))
screen.exitonclick()

