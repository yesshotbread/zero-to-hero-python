
# Reading a file

# Opening file

namefile = open("Females.txt", "r")

filecontents = namefile.read()

print(filecontents)

# Reading line by line
namefile = open("Females.txt", "r")

firstname = namefile.readline()
print (firstname)

secondname = namefile.readline()
print (secondname)

# Using loop

namefile = open("Females.txt", "r")

for x in namefile:
    print(x)

# Using "import csv" and "with" function

import csv

with open("Females.txt", "r") as namefile:
    rowslist = csv.reader(namefile)
    
    for x in rowslist:
        print(x)

#List of lists  

import csv

with open("Females.txt", "r") as namefile:
    rowslist = csv.reader(namefile)
    
    for currentrow in rowslist:
        print(currentrow)
        for currentword in currentrow:
            print(currentword)

# Using the join function to remove the "[]"

import csv

with open("Females.txt", "r") as namefile:
    rowslist = csv.reader(namefile)
    
    for currentrow in rowslist:
          print(", ".join(currentrow))
          