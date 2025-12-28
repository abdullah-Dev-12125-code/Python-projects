import pandas as pd
import re

# Dirty dataset
data = {
    "Name": ["Alice", "Bob", None, "Charlie", "alice", "Eve", "Mallory", "Bob", "Trudy", None],
    "Age": ["25", "thirty", 22, None, 25, "28", 30, 29, None, "40"],
    "Salary": [50000, 60000, None, 45000, "50000", 70000, "not available", 60000, 52000, None],
    "Email": ["alice@example.com", "bob[at]example.com", "charlie@example.com", None,
              "alice@example.com", "eve@.com", "mallory@example", "bob@example.com", "trudy@example.com", "unknown"],
    "JoinDate": ["2020-01-15", "15/02/2019", "2018/03/12", None, "2020-01-15",
                 "2019-07-30", "30-06-2021", "2019-05-20", "01/01/2020", "not available"]
}

df = pd.DataFrame(data)

# Clean Name
df['Name'] = df['Name'].fillna('Unknown').str.title()
df = df.drop_duplicates(subset=['Name', 'Email'], keep='first')
    
# Clean Age
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
df['Age'] = df['Age'].fillna(df['Age'].median())

# Clean Salary
df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
df['Salary'] = df['Salary'].fillna(df['Salary'].median())

# Clean Email
df['Email'] = df['Email'].fillna('unknown@example.com')
df['Email_Valid'] = df['Email'].apply(lambda x: bool(re.match(r"[^@]+@[^@]+\.[^@]+", x)))
df = df[df['Email_Valid']].drop(columns=['Email_Valid'])

# Clean JoinDate
df['JoinDate'] = pd.to_datetime(df['JoinDate'], errors='coerce', dayfirst=True)
df['JoinDate'] = df['JoinDate'].fillna(pd.Timestamp('2020-01-01'))

# Save cleaned data
df.to_csv("clean_data.csv", index=False)

print("Clean data saved as clean_data.csv:\n")
print(df)
