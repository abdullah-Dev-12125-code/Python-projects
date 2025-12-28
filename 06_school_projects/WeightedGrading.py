weight_assignment = 0.40
weight_quizzes = 0.20
weight_exam = 0.40

def calculate_final_grade(assignment,quizzes,exam):
    Total_Marks =(assignment * weight_assignment)+(quizzes * weight_quizzes)+(exam * weight_exam)
    Rounded_Total = round(Total_Marks,2)
    return Rounded_Total


Name = input("Students Name: ")
assignment = int(input("Enter assignment marks: "))
quizzes = int(input("Enter quizzes marks: "))
exam = int(input("Enter exam score: "))

total = calculate_final_grade(assignment,quizzes,exam)

print("\n" + "="*60)
print("\t\t\tMARKS SHEET")
print("="*60)
print(f"Student Name:\t{Name}")
print("-"*60)
print(f"\t{'Marks Obtained':>20}")
print("-"*60)
print(f"{'Assignment':<20}{assignment:>20}")
print(f"{'Quizzes':<20}{quizzes:>20}")
print(f"{'Exam':<20}{exam:>20}")
print("-"*60)
print(f"{'Total':<20}{total:>20}")
print("="*60)
