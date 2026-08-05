#this is a simple student information.
name = input("Enter your name:")
age = int(input("Enter your age:"))
score = float(input("Enter your score:"))

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Score: {score}\n")

if score >= 50:
    print(f"Passed {score}")
else:
    print(f"Failed {score}")



