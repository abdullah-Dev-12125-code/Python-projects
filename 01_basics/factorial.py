def factorial(num):
    if num == 0: 
        return 1
    elif num == 1:
        return 1
    else:
        return num * factorial(num - 1)

num = int(input("Enter a integer: "))

if num < 0:
    print("Factorial is not defined for negative numbers")
else:
    print("Factorial of", num, "is:", factorial(num))
