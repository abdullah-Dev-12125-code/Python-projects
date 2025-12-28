import matplotlib.pyplot as plt

students = ["Alice", "Bob", "Charlie", "David", "Emma"]
scores   = [85, 78, 92, 74, 88]
colors   = ["red", "blue", "green", "orange", "purple"]

plt.bar(students, scores, color=colors)
plt.xlabel("Students")
plt.ylabel("Scores")
plt.title("Math Exam Scores")
plt.axhline(y=80, linestyle="--")
plt.show()
