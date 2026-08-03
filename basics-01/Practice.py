price = "45.5"
quantity = "3"

# change String to float
price = float(price)
print(price)
print(type(price))

# change String to integer
quantity = int(quantity)
print(quantity)
print(type(quantity))

total = price * quantity
print(total)
print(type(total))

if quantity % 2 == 0:
    print("Quantity is even")
else:
    print("Quantity is odd")


print(f"Total price is ${total}")
