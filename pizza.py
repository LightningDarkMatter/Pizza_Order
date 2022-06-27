print("Welcome to Pizza Planet!")
size = input("What size pizza do you want? [S]mall, [M]edium, [L]arge: ")
add_pepperoni = input("Do you want pepperoni? [Y]es, [N]o: ")
extra_cheese = input("Do you want extra cheese? [Y]es, [N]o: ")

price = 0

if size == "S":
    price += 10
elif size == "M":
    price += 15
elif size == "L":
    price += 20
else :
    print("Invalid size")
    exit()

if add_pepperoni == "Y":
    if size == "S":
        price += 2
    else:
        price += 3
if extra_cheese == "Y":
    price += 1

print(f"Your total is ${price}")