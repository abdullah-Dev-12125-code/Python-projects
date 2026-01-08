numbers=[1,2,2,3,4,4,5]
unique_number=[]

for num in numbers:
    if num not in unique_number:
        unique_number.append(num)
        unique_number.sort(reverse=True)
        print("Unique Numbers :",unique_number)

length= len(unique_number)
print("The length of unique_numbers is",length)