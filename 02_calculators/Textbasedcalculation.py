# Work only when input is like "Solve this: (5 + 3)"

try:
    text = input("Enter what you want to solve (pattern: Solve this: (n p n )): ")

    # Extract the part inside parentheses
    start = text.index("(") + 1
    end = text.index(")")
    expression = text[start:end].strip()  # remove extra spaces

    # Find the operator
    op = None
    for char in expression:
        if char in "+-*":
            op = char
            break

    if op is None:
        raise ValueError("No valid operator found.")

    # Split numbers and convert to int
    num1, num2 = map(int, expression.split(op))

    # Perform calculation
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2

    print(f"Result: {result}")

except (ValueError, IndexError):
    print("Invalid input format. Please follow the pattern: Solve this: (n p n )")
except Exception as e:
    print(f"Unexpected error: {e}")
