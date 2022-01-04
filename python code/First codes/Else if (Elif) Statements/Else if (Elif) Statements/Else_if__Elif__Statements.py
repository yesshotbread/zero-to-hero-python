
country = input("Where are you from? ")
country = country.upper()
if country == "CANADA":
    print("Hello")
elif country == "GERMANY":
    print("Guten tag")
elif country == "FRANCE":
    print("Bonjour")
else:
    print("Hi")

#
team = input("Enter your favourite team? ")
team = team.upper()
if team == "TOTTENHAM":
    print("Best team ever!")
elif team == "CHELSEA":
    print("YUCK!!!!!")
else:
    print("I'm dissapointed")

# And / Or statements

 team = input("Enter your favourite team? ")
team = team.upper()
sports = input("Whatis you favourite sport? ")
sports = sports.upper()

if team == "TOTTENHAM" and sports == "SOCCER":
    print("To Dare is To Do!!")
else:
    print("I don't know that team")

#
 team = input("Enter your favourite team? ")
team = team.upper()
sports = input("Whatis you favourite sport? ")
sports = sports.upper()

if team == "TOTTENHAM" and sports == "SOCCER":
    print("To Dare is To Do!!")
elif team == "CHELSEA" or team == "MAN U":
    print("Your team is trash!!!")
else:
    print("I don't know that team")

# Multiple "And" / "Or" statements

team = input("Enter your favourite team? ")
team = team.upper()
sports = input("Whatis you favourite sport? ")
sports = sports.upper()

if sports == "SOCCER" and (team == "TOTTENHAM" or team == "PSG"):
    print("GANG!! GANG!!")
else:
    print("I don't know this team")

# Nesting if statements

team = input("Enter your favourite team? ")
team = team.upper()
sports = input("Whatis you favourite sport? ")
sports = sports.upper()

if sports == "SOCCER":
    print("I love Soccer!!")
    if team == "TOTTENHAM":
        print("Tottenham is the best!!")
print("Hip hip hurray!!!")

