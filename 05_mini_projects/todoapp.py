import time
import sys

tasks = []

def type_text(text, speed=0.05):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(speed)
    print()

while True:
    print("\n1. Add task")
    print("2. Remove task")
    print("3. View tasks")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        print(f"{task} is added to your list")
    
    elif choice == "2":
        task = input("Enter the task you want to remove: ")
        if task in tasks:
            tasks.remove(task)
            print(f"{task} is removed")
        else:
            print("Task not found!")

    elif choice == "3":
        print("\nYour tasks:")
        for i in tasks:
            print("-", i)

    elif choice == "4":
        time.sleep(0.3)
        type_text("bye!!!!! 👋", 0.1)
        break

    else:
        print("Invalid choice")
        size = 11 
        for i in range(size):
            for j in range(size):
                if i == j or i + j == size - 1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()  
            
            
     

