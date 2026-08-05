#This is a small calculator with input to day 

#Change variable Strig to float
number1 = float(input("Enter first number :"))
number2 = float(input("Enter second number: "))


total = number1 + number2
subtraction = number1 - number2
multipliction = number1 * number2

print("\n This is a smal calculator ")
print(f" This is my sum number {total} \n This is subtract : {subtraction} \n This is Multipication: {multipliction}")

if number2 == 0:
    print("Con't divide by zero ")
else:
    division = number1 / number2
    print(f" Divide: {division}")


