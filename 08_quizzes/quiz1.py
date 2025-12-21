students_scores = {
"kamran": [85, 92, 78],
"asif": [79, 95, 88],
"abrar": [92, 90, 85],
"danyial": [70, 75, 80]
}


def calculate_averages(scores_dict):
   averages = {}
   for name, score in scores_dict.items():
       averages[name] = sum(score)/ len(score)
       return averages
  


averages = calculate_averages(students_scores)


MaxNumbers = max(averages, key=averages.get)
top_average = averages[MaxNumbers]


print("Students with hieghest average")
print(f"Name: {MaxNumbers} , average: {top_average} ")


