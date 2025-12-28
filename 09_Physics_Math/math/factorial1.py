def calculate_factorial_recursive(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return 1
    else:
        return n * calculate_factorial_recursive(n - 1)

number = int(input("Enter a non-negative integer: "))
print(f"The factorial of {number} is {calculate_factorial_recursive(number)}")

    