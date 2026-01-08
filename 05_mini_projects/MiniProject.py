import re
pattern = r"^[A-Za-z]+ [A-Za-z]+$"
name = input("Enter your full name: ")

if re.match(pattern,name):
    print(name)
    character = list(name)
    joint = ''.join(name).upper()
    
    print(joint)
else:
    print("Full name !!")

def calculate_salary(hours, rate):
    overtime = max(0, hours - 40)
    base = min(40, hours) * rate
    overtime_pay = overtime * rate * 1.5
    return base + overtime_pay

salary = calculate_salary(50, 1000)

























# import re






# pattern = r"^[A-Za-z]+ [A-Za-z]+$"
# name = input("Enter your full name: ")

# if re.match(pattern, name):
#     print("Valid name:", name)
# else:
#     print("Full name required!!")










name.reverse()
print(name)
joint = ''.join(name).upper()
print(joint)


# for s in list_names:
#     s += list_names
#     sum.append(s)
#     print(sum)