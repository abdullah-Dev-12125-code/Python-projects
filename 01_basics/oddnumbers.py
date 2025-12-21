num1 = int(input("Enter number 1 here: "))
num2 = int(input("Enter number 2 here: "))

for i in range(num1+1, num2):
    if i %2 == 1:
        print(i)

