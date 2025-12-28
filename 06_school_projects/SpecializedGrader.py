Quiz_score = 0
Assignment_score = 0
Exam_score = 0

def Calculate_final_grade(quiz_score_input, assignment_score_input, exam_score_input):
    Quiz_score = 0
    Assignment_score = 0
    Exam_score = 0

    if 0 <= quiz_score_input <= 25:
        Quiz_score += quiz_score_input
    else:
        print("Invalid Quiz score! Must be 0-25.")

    if 0 <= assignment_score_input <= 35:
        Assignment_score += assignment_score_input
    else:
        print("Invalid Assignment score! Must be 0-35.")

    if 0 <= exam_score_input <= 40:
        Exam_score += exam_score_input

    
    else:
        print("Invalid Exam score! Must be 0-40.")



    return Quiz_score, Assignment_score, Exam_score 

def Grade_category(Final_grade):
    if Final_grade >= 85:
        return "A"
    elif Final_grade >= 70:
        return "B"
    elif Final_grade >= 50:
        return "C"
    elif Final_grade < 50:
        return "F"


try:
    quiz_score_input = int(input("Enter Quiz score (Out of 25): "))
    assignment_score_input = int(input("Enter Assignment score (Out of 35): "))
    exam_score_input = int(input("Enter Exam score (Out of 40): "))
except (ValueError):
    print("Accepts only numeric input!!")
    exit()
except Exception as e:
    print("Unexpected Error",e)
    exit()


Quiz_score, Assignment_score, Exam_score = Calculate_final_grade(quiz_score_input, assignment_score_input, exam_score_input)
sums = Quiz_score + Assignment_score + Exam_score
Final_score = Grade_category(sums)


print(" \t\tFinal Scores:")
print(f"|\tQuiz Score: {Quiz_score}             |")
print(f"|\tAssignment Score: {Assignment_score}       |")
print(f"|\tExam Score: {Exam_score}             |")
print(f"|\tGrade: {Final_score}                   |")
 