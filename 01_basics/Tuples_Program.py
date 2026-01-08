import pandas as pd

# ------------------------
# Simple tuple unpacking
# ------------------------
data = (101, "Ali", 3.9)
roll, name, gpa = data

print("Roll:", roll)
print("Name:", name)
print("GPA:", gpa)

# Iterating through a tuple
for item in data:
    print(item)

# Creating a DataFrame from a single tuple (needs nested list/tuple)
df = pd.DataFrame([data], columns=["Roll", "Name", "GPA"])
print(df)

# ------------------------
# Nested tuple unpacking
# ------------------------
students = (
    (101, "Ali", (3.9, "A")),
    (102, "Sara", (3.5, "B")),
    (103, "Bilal", (3.8, "A-"))
)

# Unpack the first student's data
roll, name, (gpa, grade) = students[0]
print("Roll:", roll, "Name:", name, "GPA:", gpa, "Grade:", grade)

# ------------------------
# Unpacking with *
# ------------------------
data_extended = (101, "Ali", 3.9, "A", "CS", 2025)
roll, *mid, year = data_extended

print("Roll:", roll)
print("Middle values:", mid)
print("Year:", year)

# ------------------------
# DataFrame from nested tuples
# ------------------------
df_students = pd.DataFrame(students, columns=["Roll", "Name", "GPA_Grade"])
print(df_students)
