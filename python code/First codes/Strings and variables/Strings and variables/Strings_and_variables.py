name = input("What is yor name? ")
print(name)

# Different line

print("What is yor name? ")
name = input("")

# You can change values of variables in code

name = input("What is yor name? ")
print(name)
name = "Mary"
print(name)

# Combining Variables and Strings

firstname = input("What is your first name? ")
surname = input("What is your surname? ")
print("Hello " + firstname + " " + surname)

#

name = input("What is your name? ")
print("Hello " + name)

# Manipulating Variables

message = ("Hello World")
print(message.upper())
print(message.lower())
print(message.swapcase())

#

name = input("What is your name? ")
name = name.upper()
country = input("What country do you live in? ")
country = country.upper()
print(" ")
print("Hello, " + name + ". You live in " + country)

message = "Hello world"
print(message.find("world"))
print(message.count("o"))
print(message.capitalize())
print(message.replace("Hello","Hi"))

# Converting lower case input and printing it as upper case

postalcode = input("Please enter your postal code? ")
postalcode = postalcode.upper()
print(" ")
print(postalcode)