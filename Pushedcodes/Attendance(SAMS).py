# #Steam up's
# attendance = []

# while True:
#     name = input("Enter your name (or 'Done' when finished): ")
#     if name.lower() == 'done':
#         break
#     if name in attendance:
#         attendance.remove(name)
#         print(f"{name} removed (duplicate entry undone).")
#     else:
#         attendance.append(name)
#         print(f"{name} added to the attendance list.")



# print("\nFinal attendance list (sorted): ")
# if attendance:
#     attendance.sort()
#     print(attendance)
#     print(f"Total number of students marked present:{len(attendance )} ")
# else:
#     print("No students were marked as present.")

# ask = input("Do you want to add a person(Yes/No): ")
# ask.capitalize()

# if ask == 'Yes':
#     addedstudent = input("Name of student: ")
#     attendance.append(addedstudent)
#     attendance.sort()
#     print(f"{addedstudent} is added to the list")
#     print(attendance)

# elif ask == 'No':
#     ask1 = input("Do you want to remove(Yes/No): ")
#     if ask == 'Yes':
#         removestudent = input("Name of student: ")
#         if removestudent in attendance:
#             attendance.remove(removestudent)
#             attendance.sort()
#             print(f"{removestudent} is removed from the list")
#             print(attendance)














# My program 
Students = []

while True:
    name = input("Enter name of students(Enter 'Done' when done): ")
    if name.lower() == 'done':
        break

    elif(name in Students):
        print(f"{name} already exists!!, Duplicate entry Undone!!!")
    else:
        Students.append(name)
        Students.sort()
        print(f"{name} added to your list")

print(f"\nFinal list of students{Students}")

while True:
    Inquiry = input("\nDo you want to add or remove(To remove'r' To add'a'press '.' to exit): \n")
    if Inquiry == '.':
        print(Students)
        break
    if Inquiry.lower() == 'r':
        Remove_Name = input("Enter Name you want to Remove: ")
        if(Remove_Name not in Students):
            print(f"{Remove_Name} Don't exists in list")
        else:
            Students.remove(Remove_Name)
            print(f"{Remove_Name} is removed from the list")    
            print("\nThe final list after removing\n")
            Students.sort()
            print(Students)
    if Inquiry == 'a':
        Add_Name = input("Enter the name you want to add: ")
        if Add_Name in Students:
            print("You can't add a same name twice")
        else:    
            Students.append(Add_Name)
            print(f"{Add_Name} is added to the list")
            print("\nThe final list after adding\n")
            Students.sort()
            print(Students)