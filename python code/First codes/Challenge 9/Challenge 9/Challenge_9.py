name = " "
guest = []


while name != "DONE":
    name = input("Enter the name of the guest (Enter 'DONE' when list ends): ")
    name = name.upper()
    guest.append(name)

    guest.sort()
for x in guest:
    if x != "DONE":
        print(x)