students_list = [85, 90, 78, 92, 88, 76, 95, 89]
print(students_list)


def addscore():
   add = float(input("Enter the score of student you want to add: "))
   students_list.append(add)
   print(f"{add} is added to the list")


def removescore():
   remove = float(input("Enter name of student to remove: "))
   students_list.remove(remove)
   print(f"{remove} is removed from the list")


def heighest_score():
   print("\n here is the list of students score more then 85")
   for i in students_list:
       if i >=85:
           students_list.sort()
           print(i)
            


addscore()
removescore()
heighest_score()