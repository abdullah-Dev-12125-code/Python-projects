import regex as re
Raw_Emails = []
Invalid_emails = []
Valid_Email = []

try:
    def Validate_emails():
        pattern = r"^\d{6}@university\.edu$"
        matches = [s for s  in Raw_Emails if re.match(pattern,s)]
        return matches
    Validate_emails()
    while True:
        emails = input("Enter Emails!!('.' when done): ")
        if emails == '.':
            break
        else:
            if emails in Raw_Emails:
                print("Already in")
            else:
                Raw_Emails.append(emails)
                print(f"{emails} has been added to the list")
    check = Valid_Email(Raw_Emails)
    if check:
        Valid_Email.append(check)
    else:
        Invalid_emails.append(check)
except (ValueError,TabError):
    print("Enter a proper email (eg:studentID@university.edu)")

print("\n--Raw emails--\n")
print(Raw_Emails)
print("\n--valid emails--\n")
print(Valid_Email)
print("\n--Invalid emails--\n")
print(Invalid_emails)

