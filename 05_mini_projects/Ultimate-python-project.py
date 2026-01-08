import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ======================================================
# 1. REGEX PATTERNS
# ======================================================
email_pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z.-]+\.[A-Za-z]{2,}$"
cnic_pattern = r'^(?:\d{13}|\d{5}-\d{7}-\d)$'



# ======================================================
# 2. Recursive Function Example
# ======================================================
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


# ======================================================
# 3. NATIONAL CITIZENS DATABASE
# ======================================================
citizens = []


# ======================================================
# 4. ADD MULTIPLE CITIZENS
# ======================================================
def add_person():
    print("\n➡ MULTI-ENTRY MODE ENABLED (type 'stop' to finish)\n")

    while True:
        name = input("Enter full name (or 'stop' to finish): ").strip()
        if name.lower() in ["stop", "exit", "quit", "q"]:
            print("✔ Finished adding citizens.")
            break

        name = name.title()

        age = int(input("Enter age: "))

        # CNIC validation
        while True:
            cnic = input("Enter CNIC (13 digits): ").strip()
            if re.match(cnic_pattern, cnic):
                break
            print("❌ Invalid CNIC! Must be exactly 13 digits.")

        # Email validation
        while True:
            email = input("Enter email: ").strip()
            if re.match(email_pattern, email):
                break
            print("❌ Invalid email format!")

        city = input("Enter city: ").strip().title()
        province = input("Enter province: ").strip().title()

        income = int(input("Enter yearly income: "))
        family_members = int(input("Enter number of family members: "))
        happiness = int(input("Enter happiness score (0-100): "))

        person = {
            "name": name,
            "age": age,
            "cnic": cnic,
            "email": email,
            "city": city,
            "province": province,
            "income": income,
            "family_members": family_members,
            "happiness": happiness
        }

        citizens.append(person)
        print("✔ Citizen added successfully!\n")


# ======================================================
# 5. REMOVE PERSON
# ======================================================
def remove_person():
    cnic = input("Enter CNIC to remove: ").strip()
    for p in citizens:
        if p["cnic"] == cnic:
            citizens.remove(p)
            print("✔ Citizen removed.")
            return
    print("❌ Citizen not found.")


# ======================================================
# 6. SHOW PEOPLE
# ======================================================
def show_people():
    if not citizens:
        print("No citizens in database.")
        return

    print("\n=== NATIONAL CITIZENS LIST ===")
    for p in citizens:
        print(
            f"Name: {p['name']} | Age: {p['age']} | CNIC: {p['cnic']} | "
            f"Email: {p['email']} | City: {p['city']} | Province: {p['province']} | "
            f"Income: {p['income']} | Family: {p['family_members']} | Happiness: {p['happiness']}"
        )


# ======================================================
# 7. ANALYZE DATA (NUMPY + PANDAS + GRAPHS)
# ======================================================

def analyze_data():
    if not citizens:
        print("❌ Add citizens first!")
        return

    df = pd.DataFrame(citizens)
    print("\n=== NATIONAL DATAFRAME ===")
    print(df)

    # Calculate statistics
    avg_income = np.mean(df["income"])
    avg_happiness = np.mean(df["happiness"])

    print("\n=== NATIONAL STATISTICS ===")
    print("Average Yearly Income:", avg_income)
    print("Average Happiness Score:", avg_happiness)

    # Graph 1: Happiness by Province
    plt.figure(figsize=(6, 4))
    sns.barplot(x=df["province"], y=df["happiness"])
    plt.title("Average Happiness by Province")
    plt.show()

    # Graph 2: Income Distribution
    plt.figure(figsize=(6, 4))
    sns.histplot(df["income"], kde=True)
    plt.title("Income Distribution of Citizens")
    plt.show()


# ======================================================
# 8. SAVE & LOAD
# ======================================================
def save_data():
    df = pd.DataFrame(citizens)
    df.to_csv("national_database.csv", index=False)
    print("✔ Database saved!")


def load_data():
    global citizens
    try:
        df = pd.read_csv("national_database.csv")
        citizens = df.to_dict("records")
        print("✔ Database loaded!")
    except:
        print("❌ No saved file found.")


# ======================================================
# 9. MAIN MENU
# ======================================================
while True:
    print("""
======================================================
NATIONAL PEOPLE DATABASE SYSTEM
======================================================
1. Add New Citizens (Multi-entry Mode)
2. Remove Citizen (By CNIC)
3. Show All Citizens
4. Analyze Country Data (NumPy + Pandas + Graphs)
5. Save National Database
6. Load National Database
7. Population Factorial (Recursion Demo)
8. Exit
======================================================
""")

    choice = input("Choose an option: ")

    if choice == "1":
        add_person()

    elif choice == "2":
        remove_person()

    elif choice == "3":
        show_people()

    elif choice == "4":
        analyze_data()

    elif choice == "5":
        save_data()

    elif choice == "6":
        load_data()

    elif choice == "7":
        num = int(input("Enter a number for factorial: "))
        print("Population Factorial =", factorial(num))

    elif choice == "8":
        print("Exiting system... Goodbye!")
        break

    else:
        print("❌ Invalid option, try again.")



# Fake CNICs (Dashed)
# 42101-1234567-1
# 61102-9876543-2
# 37405-4567891-7
# 54321-1122334-9
# 13579-2468135-4
# 42203-7654321-8
# 31101-9998887-5
# 52525-1237894-3
# 72819-5556662-0
# 40201-3141592-6

# Fake CNICs (13-digit)
# 4210112345671
# 6110298765432
# 3740545678917
# 5432111223349
# 1357924681354
# 4220376543218
# 3110199988875
# 5252512378943
# 7281955566620
# 4020131415926

# Fake Emails
# abdullah.khan93@mail.com
# aisha.malik21@example.pk
# hassan.raza87@testmail.org
# fatima.shaikh04@demo.net
# usman.farooq12@sample.com
# zara.qureshi77@mailbox.pk
# bilal.javed05@mydomain.org
# sana.ansari44@test.org
# omer.mirza19@fakemail.pk
# noor.ahmed31@demo.com
