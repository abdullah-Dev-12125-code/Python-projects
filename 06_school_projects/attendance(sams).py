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