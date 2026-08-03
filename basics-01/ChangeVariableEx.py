name = "Sara"
age = "25"
height = "1.68"
is_Married = "0"

# change variable String to integer
age = int(age)
print(age)
print(type(age))

#change variable String to float.
height = float(height)
print(height)
print(type(height))

print(f"{name} is {age} years old and {height}m tall")
#change string to integer
is_Married = int(is_Married)
#change integer {is_Married} to boolean.
is_Married = bool(is_Married)
print(type(is_Married))
if is_Married:
    print("You are married")
else:
    print("Your are not married")