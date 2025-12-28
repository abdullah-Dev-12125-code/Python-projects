import re

Passwords = []
Clean_passwords = []
Wrong_password = []

pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%&]).{8,16}$'

def validate_passwords(password):
    for check in password:
        match = re.match(pattern,check)
        if match:
            Clean_passwords.append(check) 
            print("Valid:",check)
        if not match:
            Wrong_password.append(check)

while True:
    Password_input = input("Enter your Passwords('Done'When done): ")
    if Password_input.lower() == 'done':
        break
    else:
        Passwords.append(Password_input)

validate_passwords(Passwords)

print("\t\tValid passwords\n")
for i, words in enumerate(Clean_passwords,start=1):
    print(f"{i}:{words}")