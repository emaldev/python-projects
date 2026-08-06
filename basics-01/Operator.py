age = int(input("Enter your age :"))

if age >= 100:
    print("You are too old to sign up!")
elif age >= 18:
    print("You are new siged up!")
elif age < 0:
    print("You must be 18 to sign up!")
