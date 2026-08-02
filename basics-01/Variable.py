# Variable = A container for a value (String , integer, float, boolean)
#            A variable bebaves as if it was the value it contains

# this is String variable 
first_name = "Emal"
food = "pizza"
email = "emalhasanzada82@gmail.com"
print(f"\n\nYou like{food}")
print(f"Hello{first_name}")
print(f"Your email is : {email}\n\n")

#this is Integer variable.
age = 20
quantity = 3
num_of_students = 30

print(f"I'm {age} years old")
print(f"You age buying {quantity} items")
print(f"Your class has {num_of_students} students \n\n")


#This is a Float variable.
price = 10.99
gpa = 3.2
distance = 5.5
print(f"The price is ${price}")
print(f"Your gpa is: {gpa}")
print(f"You ran {distance}km\n\n")

#Boolean variable



is_student = False
print(f"Are you a student?: {is_student}")
if is_student:
    print("You are a student")
else:
    print("Your are not a student\n\n")


for_sale = True

if for_sale:
     print("this is sale")
else:
     print("This is not sale\n\n")



is_online = True

if is_online:
      print("You are Online")
else:
      print("You are offline")
