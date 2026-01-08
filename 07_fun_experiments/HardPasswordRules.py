pwd = "Adm1n@2025!"

length = len(pwd)

# Rule: at least 3 digits anywhere
rule_3nums = sum(c.isdigit() for c in pwd) >= 3

# Rule: a digit in the middle of the password
mid_index = length // 2
if length % 2 == 0:
    # For even length, check either middle character
    rule_num_mid = pwd[mid_index].isdigit() or pwd[mid_index - 1].isdigit()
else:
    rule_num_mid = pwd[mid_index].isdigit()

# Other rules
rules = [
    length >= 10,                  # Minimum length
    any(c.isupper() for c in pwd), # At least one uppercase
    any(c.islower() for c in pwd), # At least one lowercase
    any(c.isdigit() for c in pwd), # At least one digit
    any(not c.isalnum() for c in pwd), # At least one special character
    pwd[:8].isalnum(),             # First 8 characters alphanumeric
    pwd[-1] in "!@#$%",            # Last character is special
    rule_3nums,                     # At least 3 digits anywhere
    rule_num_mid                    # Digit in the middle
]

# Final validation
if all(rules):
    print("Valid Password")
else:
    print("Invalid Password")
