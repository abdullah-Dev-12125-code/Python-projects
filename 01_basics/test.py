"""
i usually test Heere and experiments on diffrent things 
(Deleted alot of stuff)


"""





name = "Abdullah"
print(name)


x = 10 
y = 20

sum = x + y

diffrence = y - x

product = x * y

print(f"The sum is {sum} | The diffrence is {diffrence} | The product is {product}")


x = "123"

li = int(x)

y = 10

print(y + li)


age = input("Enter your age: ")
ageconverted = int(age)

print(f"You are {ageconverted} Years old!!")


import  math 
a = math.floor(3.231234)
print(a)

def factorial(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        fact = num * factorial(num-1)
        return fact
    
num = int(input("Enter a number: "))
print(factorial(num))
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

num = int(input("Enter a number: "))
result = factorial(num)
print("Factorial of", num, "is", result)



# 1. What will be the output?

a = [1, 2, 3]
b = a
b.append(4)
print(a)

# [1,2,3,4]

if a is b:
    print(a)

