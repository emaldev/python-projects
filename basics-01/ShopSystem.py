#This is a smal shop mabnagment for me 

name_product = input("Enter name of product:")
price = float(input("Enter pirce of product:"))
quantity = int(input("Enter quantity of product:"))

total_sell = price * quantity
discount = total_sell * 0.10

if total_sell > 100:
    total_sell -= discount
    print(total_sell)
else:
    print("You don't have discount")
    print(total_sell)
