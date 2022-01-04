age = 42
print(age)

#
width = 20
height = 5

area = width * height
perimeter = 2*(width + height)
print(area)
print(perimeter)

# Formatting Numbers

# Float

area = 0
height = 10
width = 20

area = width * height/2
print("The area of a triangle is %.2f" %area)

# Decimal

print("My favourite number is %d" %42)

#
print("My favourite number is %6d" %42)

#
print("My favourite number is %06d" %42)

# .Format syntax
area = 0
height = 10
width = 20

area = width * height/2

print("The area of the triangle would be {0:.2f} ".format(area))

#
print("My favorite number is {0:d}" .format(42))

#
print("Here are three numbers, first is {0:d}, second is {1:08d} and third is {2:d}" .format(6,5,4))

# When dealing with a long line of string

print("Here are three numbers, " + \
      "first is {0:d}, second is {1:08d} and third is {2:d}" .format(6,5,4))

# Asking for input

salary = input("please enter your salary? ")
bonus = input("Enter your bonus? ")

paycheck = salary + bonus
print(paycheck)

# Number functions

salary = input("please enter your salary? ")
bonus = input("Enter your bonus? ")

paycheck = float(salary) + float(bonus)
print(paycheck)