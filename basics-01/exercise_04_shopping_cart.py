
#This is an exercise to strengthen Python skills.
#This is my varaible this class 
item_name = "Laptop"
item_price = "899.99"
item_quantity = "2"
in_stock = "1"

#change String to float
item_price = float(item_price)
print(item_price)
print(type(item_price)) #this is my type varaible after change.

# change String to integer varaible 
item_quantity = int(item_quantity)
print(item_quantity)

# change String to iteger and boolean variable.
in_stock = int(in_stock)
print(in_stock)
in_stock = bool(in_stock)
print(in_stock)

total_const = item_price * item_quantity
print(total_const)

#This is if/else Condition 
if item_quantity % 2 == 0:
    print("even")
else:
    print("odd")

if in_stock:
    print("Item is in stock")
else:
    print("Item is out of stock")

print(f"You are buying {item_quantity} {item_name}(s) for a total of ${total_const}")
 