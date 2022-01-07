guests = ["Joojo", "Yess Hotbread", "Nathaniel"]

print(guests[0])
print(guests[1])

# Changing value in Lists

guests = ["Joojo", "Yess Hotbread", "Nathaniel"]
print("First value is " + guests[0])
guests[0] = "Steve"
print("First value is now " + guests[0])

# Adding values with append function

guests = ["Joojo", "Yess Hotbread", "Nathaniel"]
guests.append("Steve")

print(guests[-1])

# Removing values from the lists using the remove function

guests = ["Joojo", "Yess Hotbread", "Nathaniel"]
guests.remove("Nathaniel")

print(guests[-1])

# Removing values from the lists using the delete function

guests = ["Joojo", "Yess Hotbread", "Nathaniel"]
del guests[0]

print(guests[0])

# Add function

guests = ["Joojo", "Yess Hotbread", "Nathaniel"]
guests.append("Collin")
guests.append("Sonal")

print (guests[-1])

# Index Function

guests = ["Joojo", "Yess Hotbread", "Nathaniel"]
print(guests.index("Nathaniel"))

# Using loops to remove duplicates

guests = ["Joojo", "Yess Hotbread", "Nathaniel", "Satya", "Nathaniel", "Nathaniel", "Nathaniel"]

for name in guests[:]:
    print(name)
    if name == "Nathaniel":
        guests.remove(name)

print(guests)

# Using loops to process lists

guests = ["Joojo", "Yess Hotbread", "Nathaniel"]
for names in range(3):
    print(guests[names])

#Using len() function

guests = ["Joojo", "Yess Hotbread", "Nathaniel", "Joojo", "Yess Hotbread", "Nathaniel", "Satya", "Nathaniel", "Nathaniel", "Nathaniel"]

value_nbr = len(guests)
for names in range(value_nbr):
    print(guests[names])


guests = ["Joojo", "Yess Hotbread", "Nathaniel"]
for names in guests:
    print(names)

# Sortong a list

guests = ["Nathaniel", "Joojo", "Yess Hotbread"]
guests.sort()
for names in guests:
    print(names)









