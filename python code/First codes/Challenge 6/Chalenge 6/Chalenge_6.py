
gst = float(0.05)
hst = float(0.13)
pst = float(0.06)

country = input("What country are you from? ")
country = country.lower()

if country == "canada":
    province = input("Which province in canada do you stay? ")
    province = province.lower()

order = input("What is your order total? ")
order = float(order)

if country == "canada":
    if province == "alberta":
        order = order + (order * gst)
    elif province == "ontario" or province == "new brunswick" or province == "nova scotia":
        order = order + (order * hst)
    else:
        order = order + (order * (gst + pst))
print ("your total order including taxes is ${0:.2f}" .format(order))