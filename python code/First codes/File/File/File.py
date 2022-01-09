
filename = "demo.txt"
WRITE = "w"

file = open(filename, mode = WRITE)
# "WRITE" function overwrites existing text

# Use "APPEND" function if you want to add to existing text

filename = "demo.txt"
WRITE = "w"
APPEND = "a"

myfile = open(filename, mode = WRITE)
myfile.write("Hi, there! ")
myfile.write("How are you? ")

# On different line (\n)

filename = "demo.txt"
WRITE = "w"
APPEND = "a"

myfile = open(filename, mode = WRITE)
myfile.write("Hi, there!\n")
myfile.write("How are you? ")

# Closing it

filename = "demo.txt"
WRITE = "w"
APPEND = "a"

myfile = open(filename, mode = WRITE)
myfile.write("Hi, there! ")
myfile.write("How are you? ")
myfile.close()

print("File written successfully")

# Reading and writing code at the same time
 
filename = "demo.txt"
WRITE = "w"
APPEND = "a"
READWRITE = "w+"

myfile = open(filename, mode = READWRITE)
myfile.write("Hi, there! ")
myfile.write("How are you? ")

print("File written successfully")
 