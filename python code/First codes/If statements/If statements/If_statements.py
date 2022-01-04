
answer = input("Would you like express shipping? ")
if answer == "yes":
    print("That will be extra $10")
print("Have a nice day")

#
favouriteteam = input("What is your favourite team? ")
if favouriteteam == "Tottenham":
    print("To Dare is To Do")
    print("We will be great again!")
print("Awesome")

# Solving Case Sensitive Problems

favouriteteam = input("What is your favourite team? ")
favouriteteam = favouriteteam.upper()
if favouriteteam == "TOTTENHAM":
    print("To Dare is To Do")
    print("We will be great again!")
print("Awesome")

#
answer = input("Would you like express shipping? ")
answer = answer.upper()
if answer == "YES":
    print("That will be extra $10")
print("Have a nice day")

# If statements on numbers

deposit = input("How much did you deposit? ")
deposit = float(deposit)
if deposit > 100:
    print("You get a free toaster")
print("Have a nice day")

# Else statements

deposit = input("How much did you deposit? ")
deposit = float(deposit)
if deposit > 100:
    print("You get a free toaster!")
else:
    print("Enjoy your free mug!")
print("Have a nice day")

# True or False statements

deposit = input("How much would you like to deposit? ")
deposit = float(deposit)
freetoaster = False
if deposit > 100:
    freetoaster = True
if freetoaster:
    print("You get a free toaster!")
else:
    print("You get a free mug!")
print("Have a nice day")