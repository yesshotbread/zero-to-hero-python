
import turtle
sides = input("How many sides do you want your polygon to have? ")
sides = int(sides)
for steps in range(sides):
    turtle.forward(100)
    turtle.left(360/sides)
    for moresteps in range(sides):
        turtle.forward(50)
        turtle.left(360/sides)