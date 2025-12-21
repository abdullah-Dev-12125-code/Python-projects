import math


def calculator(num1 ,operator,num2=None):

    if operator == "+":
        return num1 + num2
    elif operator  == "-":
         return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    elif operator == "^":
        return num1 ** num2
    elif operator == "√":
        return math.sqrt(num1)
    else:
        print("invalid syntax")

operator = input("Enter the operator (+, -, *, /, ^, √): ")
if operator == "√":
    num1 = float(input("Enter number here: "))
    print("Result:", calculator(num1, operator))
else:
    num1 = float(input("Enter your number here: "))
    num2 = float(input("Enter your number here: "))
    print("Result:", calculator(num1, operator,num2))
    