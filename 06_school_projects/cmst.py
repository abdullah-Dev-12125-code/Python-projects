courses = {
    "Data Structures": {"Alice": 85, "Bob": 90, "Charlie": 75},
    "Algorithms": {"Alice": 95, "Dave": 88},
    "Machine Learning": {"Bob": 82, "Eve": 91, "Frank": 78}
}

change = courses["Data Structures"]["Alice"] = 90
del courses["Data Structures"]["Charlie"] 

courses["Web Development"] = {"Grace": 92 , "Henry": 85}

if "Bob" in courses["Algorithms"]:
    print("\nBob is enrolled in Algorithms!!\n")
else:
    courses["Algorithms"]["Bob"] = 80

del courses["Machine Learning"]

print("\nThe average grade in Data Structures:\n")
data_structures_scores = courses["Data Structures"].values()
average = sum(data_structures_scores) / len(data_structures_scores)

print("Courses dictionary:\n", courses)
print("\nAverage:", average, "\n")
