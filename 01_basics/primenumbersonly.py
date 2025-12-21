n = int(input("Enter a number: "))
n1 = int(input("Enter number here to specify where to start: "))
print("Prime numbers up to", n, "are:")

for num in range(n1, n + 1):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
