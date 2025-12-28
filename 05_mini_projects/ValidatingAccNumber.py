import re

account_numbers = []
context = []

pattern = r'ACC[A-Z]{2}\d{5}'

def validate_account_number(acc_number):
    for check in acc_number:
        matches = re.findall(pattern, check)
        for m in matches:
            print("Valid ACC NUMBER:", m)

Acc_input1 = input("Extract data From para(1) or (2) for list Cleaning: ")
while True:
    if Acc_input1 == '1':
        para = input("Enter Context('Done' when done): ")
        if para.lower() == 'done':
            break
        else:
            context.append(para)
    elif Acc_input1 == '2':
        Acc_input = input("Enter account number('DONE' When done): ")
        if Acc_input.lower() == 'done':
            break
        else:
            account_numbers.append(Acc_input)
            print(Acc_input, "Has been added")

if Acc_input1 == '2':
    validate_account_number(account_numbers)
elif Acc_input1 == '1':
    validate_account_number(context)
