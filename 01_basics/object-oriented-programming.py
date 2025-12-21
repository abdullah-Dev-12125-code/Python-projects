class Car:
    def __init__(self,Brand,model,color,condition):
        self.brand = Brand
        self.model = model
        self.color = color
        self.condition = condition

    def info(self):
        print(f"The brand is '{self.brand}' and model is '{self.model}'. The color is '{self.color}' and condition is '{self.condition}'")


a = Car("Toyota","Carolla","Blue","New")
a.info()


class calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
        if op == '+':
            return self.num1 + self.num2
    
    def Subtract(self):
        if op == '-':
            return self.num1 - self.num2
    
    def Multiply(self):
        if op == '*':
            return self.num1 * self.num2
        
    def Divide(self):
        if op == '/':
            return self.num1 / self.num2
        

num1 = int(input("enter a number: "))
op = input("enter op: ")
num2 = int(input("enter a number: "))

calculations = calculator(num1,num2)

if op == '+':
    print(calculations.add())
elif op == '-':
    print(calculations.Subtract())
elif op == '*':
    print(calculations.Multiply())
elif op == '/':
    print(calculations.Divide())
else:
    print("No proper operator only accepts(+ , - , * , /)")


