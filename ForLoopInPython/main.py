total = 0.0
price = float(input("Enter price (negative value to stop): "))
while price >= 0:
    number = int(input("Enter the number of items: "))
    total += price*number
    price = float(input("Enter the item price: "))
print("The total price is:", str(total))
