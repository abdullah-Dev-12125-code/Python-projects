print("Enter numbers one by one. Type 'done' when finished.")

total = 0
count = 0

while True:
    num = input("Enter number (or 'done' to finish): ")
    if num.lower() == "done":
        break

    total += float(num)
    count += 1

if count > 0:
    mean = total / count
    print("Sum of n = ",total ,"Arithmetic Mean =", mean)
else:
    print("No numbers entered.")
