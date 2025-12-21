while True:
    def calculator(num1,op,num2):
        if op == '+':
            return num1 + num2
        elif op == '-':
            return num1 - num2
        elif op == '*':
            return num1 * num2
        elif op == '**':
            return num1 ** num2
        elif op == '/':
            if num2 == 0:
                print("you cant divide by zero")
            
            else:
                return num1 / num2
        else:
            print("Invalid operation")
            
    
    num1 = float(input("Enter number 1: "))
    op = input("Enter a valid operator(+,-,*,/,**): ")
    num2 = float(input("Enter number 2: "))
    calculators = calculator(num1,op,num2)
    
    print(f"the result of {num1} {op} {num2} is = {calculators}")
