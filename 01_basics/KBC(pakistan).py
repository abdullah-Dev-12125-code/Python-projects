import time
import sys

def type_text_with_dots(text, dot_count=3, speed=0.1, dot_speed=0.5):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(speed)
    for _ in range(dot_count):      
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(dot_speed)
    print() 

questions = [
    ["What is the name of the bank which is the most active", "A.Karachi central", "B.bank allied", "C.allied bank", "D.Alfala bank", "C"],
    ["What is the first space mission named", "A.appolos", "B.blows mision", "C.heinsenbergh", "D.kitosis", "C"]
]

user = input("Enter your name: ")
greet = "Hello!!"
print(f"{greet}, {user}")

while True:
    query = input("Do you want to play KBCP (Yes/No): ")
    query = query.capitalize()
    if query == 'No':
        print("Exit")
        break
    if query == 'Yes':
        print("It is being processed")
        type_text_with_dots("Loading")

        for q in questions:
            print("\n" + q[0])  
            print(q[1])
            print(q[2])
            print(q[3])
            print(q[4])
            
            answer = input("Enter your answer (A/B/C/D): ").upper()
            if answer == q[5]:
                print("✅ Correct!")
            else:
                print(f"❌ Wrong! The correct answer was {q[5]}")
            
            time.sleep(1) 
