filename = "challenge 11.txt"
WRITE = "w"
APPEND = "a"
READWRITE = "w+"

myfile = open(filename, mode = READWRITE)
myfile.write("Linda, 10\n")
myfile.write("Barbara, 29\n")
myfile.write("Monica, 38\n")
myfile.write("Jessica, 47\n")
myfile.write("Sarah, 56\n")
myfile.write("Gifty, 74\n")
myfile.write("Diana, 83\n")

print("File written successfully")