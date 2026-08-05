#This is temperture changer.

temperature = float(input("Enter temperature:"))
unit = input("Ente nuite (C/F) :").upper()

if unit == "C":
    F = (temperature * 9/5) + 32
    print(f"{temperature} C = {F} F")
elif unit == "F":
    C = (temperature - 32) * 5/9
    print(f"{temperature} F = {C} c")
else:
    print("Invlid unit.")