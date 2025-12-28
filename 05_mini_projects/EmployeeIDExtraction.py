import re

EMP_IDS = [
    "EMP1234",
    "EMP5678",
    "EMP12A4",
    "EM12345",
    "EMP9101",
    "EMP112",
    "EMP3141",
    "EMP51616",
    "EPM7181",
    "EMP9202"
]

Clean_IDS= []



pattern = "^EMP\d{4}$"

try:
    while True:
        info = input("Enter employee's id('Stop' when done): ")
        if info.lower() == 'stop':
            break
        else:
            EMP_IDS.append(info)
            print(f"{info} :has been added") 
except Exception as e:
    print("Unexpected error")       

def validate_employee_id(emp_id):
    for ID in emp_id:
        match = re.match(pattern,ID)
        if match:
            Clean_IDS.append(ID)
              
        
validate_employee_id(EMP_IDS)
    

print("\t\tValid EMP ID")
for i in (Clean_IDS):
    print("Valid ID:",i)
print("\t\tInvalid EMP ID")
for j in EMP_IDS:
    if re.match(pattern,j):
        pass
    else:
        print("Invalid ID:",j)