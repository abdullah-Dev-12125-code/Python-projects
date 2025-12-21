def grade_calculator(percentage):
    if percentage >= 95:
        print("A")
    elif percentage >= 85:
        print("B")
    elif percentage >= 75:
        print("C")
    elif percentage >= 65:
        print("D")
    elif percentage >= 55:
        print("D-")
    elif percentage >= 45:
        print("E")
    elif percentage >= 35:
        print("Passed")
    else:
        print("Fail")

p = int(input("Enter your percentage: "))
grade_calculator(p)



    
