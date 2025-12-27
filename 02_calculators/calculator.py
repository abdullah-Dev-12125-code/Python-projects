import math
while True:
    def calculator(num1,num2,op):
        if op =="+":
            return num1 + num2
        if op =="-":
            return num1 - num2
        if op =="*":
            return num1 * num2
        if op =="/":
            return num1 / num2
        if op =="**":
            return num1 ** num2
        if op =="√":
            return math.sqrt (num1)

    
    op = input("Enter operator here(+,-,*,/): ")
    if op == "√" :
        num1 = float(input("Enter number here: "))
        num2 = 0
        print(calculator(num1,num2,op))
    else:
        num1 = float(input("Enter number here: "))
        num2 = float(input("Enter number here: "))
        print(calculator(num1,num2,op))



