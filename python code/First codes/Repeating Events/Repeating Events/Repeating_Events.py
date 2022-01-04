
import turtle
turtle.forward(100)
turtle.right(90)
turtle.color("red")
turtle.forward(100)

#
import turtle
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

# Loops with Turtle 

# For Loops

import turtle
for steps in range(4):
    turtle.forward(100)
    turtle.right(90)

#
import turtle
for steps in range(4):
    turtle.forward(100)
    turtle.right(90)
turtle.color("red")
turtle.forward(200)
turtle.right(90)

#
import turtle
for steps in range (4):
    turtle.forward(100)
    turtle.right(90)
    for moresteps in range (4):
        turtle.forward(50)
        turtle.right(90

#
import turtle
for steps in range (5):
    turtle.forward(100)
    turtle.right(360/5)
    for moresteps in range (5):
        turtle.forward(50)
        turtle.right(360/5)

# Using variables for loops

import turtle 
nbrsides = int(20)
for steps in range (nbrsides):
    turtle.forward(100)
    turtle.right(360/nbrsides)
    for moresteps in range (nbrsides):
        turtle.forward(50)
        turtle.right(360/nbrsides)

# Using for loops with values

for steps in range (4):
    print(steps)

#
for steps in range (1, 4):
    print(steps)

# Skipping loop values

for steps in range (1,10,2):
    print(steps)

# Printing exact values for loop

for steps in [1, 12, 23, 34, 45]:
    print(steps)

#
import turtle
for steps in ["red", "blue", "green", "purple"]:
    turtle.color(steps)
    turtle.forward(100)
    turtle.left(90)

