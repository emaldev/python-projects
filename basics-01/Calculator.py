#Python calculator
#This is a small calculator 
#Items used in this program (input, operator(+ , - , * , /), if/elif, change vairable (String to float), )
operator = input("Enter an operator (+ - * /) : ")

num1 = float(input("Enter number : "))
num2 = float(input("Enter second number : "))

if operator == "+":
    result = num1 + num2
    print(round(result))
elif operator == "-":
    result = num1 - num2
    print(round(result))
elif operator == "*":
    result = num1 * num2
    print(round(result))
elif operator == "/":
    result = num1 / num2
    print(round(result))

else:
    print(f'Invalid {operator}')
