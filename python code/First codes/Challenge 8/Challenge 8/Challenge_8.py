import turtle

lineLength = int(input("How long would you like to make the line? (specify 0 to stop drawing) " ))
penColor = input("What pen color would you like to use? (black, blue, red, green): ")
angle = int(input("What angle would you like? (0-360): "))

print(" ")
while lineLength != 0 :
    turtle.color(penColor)
    turtle.right(angle)
    turtle.forward(lineLength)

    lineLength = int(input("How long would you like to make the line? (specify 0 to stop drawing) " ))
    if lineLength != 0 :
        penColor = input("What pen color would you like to use? (black, blue, red, green): ")
        angle = int(input("What angle would you like? (0-360): "))