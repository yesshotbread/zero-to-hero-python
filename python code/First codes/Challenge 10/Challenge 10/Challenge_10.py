
filename = "demo.csv"
WRITE = "w"
APPEND = "a"
READWRITE = "w+" 

myfile = open(filename, mode = READWRITE)
myfile.write("Doyle McCarty, 27\n")
myfile.write(" Jodi Mills, 25\n")
myfile.write("Nicholas Rose, 32\n")
myfile.write("Kian Goddard, 36\n")
myfile.write("Zuhu Hanania, 26\n")
myfile.close()

print("File written successfully")

# Using input function 

filename = "demo.csv"
WRITE = "w"
APPEND = "a"
READWRITE = "w+" 


data = input("Please input data (use commas)" )
myfile = open(filename, mode = READWRITE)
myfile.write(data)
