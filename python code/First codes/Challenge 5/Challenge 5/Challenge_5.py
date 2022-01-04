
purchase = input("Please enter the amount for your purchase? ")
purchase = float(purchase)
extrafee = False
if purchase < 50:
    extrafee = True
if extrafee:
    print("$10 will be added for shipping fee")
    total = purchase + 10
    print("Your total amount of purchase is $", total)
else:
    print("Your total amount of purchase is $", purchase)


#
purchase = input("Please enter the amount for your purchase? ")
purchase = float(purchase)
if purchase < 50:
    print("$10 will be added for shipping fee")
    total = purchase + 10
    print("Your total amount of purchase is $", total)
else:
    print("Your total amount of purchase is $", purchase)