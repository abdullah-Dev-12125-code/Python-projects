import regex as re

raw_emails = [
    "111111@university.edu",   
    "222222@university.edu",   
    "333333@university.edu",   
    "444444@university.edu",   
    "55555@university.edu",    
    "6666666@university.edu",  
    "abc123@university.edu",   
    "123456@university.com",   
    "123456@university.edu.pk"
    "123456@gmail.com"         
]

Valid_Emails=[]

Pattern = '^\d{6}@university\.edu$' 

def validate_email(emails):
    for match in emails:
        if re.match(Pattern,match):
            Valid_Emails.append(match)
        
validate_email(raw_emails)


print("\n\t\tValid Email list\n")

for i in Valid_Emails:
    print(i)