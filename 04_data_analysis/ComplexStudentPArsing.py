records = "STU|Steamupqbh|AGE:22|GPA=3.44|DEPT-CS|CGPA-3|SEM-07|ROLLNUMBER=32|CREDITHOURS=17"

# Extract values using index slicing
name = records.split("|")[1]
age = int(records[records.index("AGE:") + 4 : records.index("|GPA")])
gpa = float(records[records.index("GPA=") + 4 : records.index("|DEPT")])
dept = records[records.index("DEPT-") + 5 : records.index("|CGPA")]
cgpa = records[records.index("CGPA-") + 5 : records.index("|SEM")]
sem = records[records.index("SEM-") + 4 : records.index("|ROLLNUMBER")]
roll_number = records[records.index("ROLLNUMBER=") + 11 : records.index("|CREDITHOURS")]
credit_hours = records[records.index("CREDITHOURS=") + 12 :]

# Print formatted output
print(f"Name: {name} | Roll Number: {roll_number} | Age: {age} | GPA: {gpa} | Dept: {dept} | CGPA: {cgpa} | Semester: {sem} | Credit Hours: {credit_hours}")

# Optional separate prints
print(f"Name: {name} : Roll Number: {roll_number}")
print(f"Age: {age} : GPA: {gpa}")
print(f"Dept: {dept} : CGPA: {cgpa}")
print(f"Semester: {sem} : Credit Hours: {credit_hours}")
