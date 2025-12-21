def rate(rating):
    if rating == 5:
        return "1000"
    elif rating == 4:
        return "750"
    elif rating == 3:
        return "500"
    else:
        return "No bonus"

employee_ratings = {"Alice": 5, "Bob": 4, "Charlie": 3, "David": 2, "Eve": 5}

for name, rating in employee_ratings.items():
    print(f"{name}, your bonus is ${rate(rating)}.")
