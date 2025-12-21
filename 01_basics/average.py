def average(num1,num2,num3):
    sum = num1 + num2 + num3
    divisor = 3
    operation = (sum / divisor)
    return operation

num1 = int(input("Enter your number: "))
num2 = int(input("Enter your number: "))
num3 = int(input("Enter your number: "))

output = average(num1,num2,num3)
print(f"The average of {num1,num2,num3} is {output}")
