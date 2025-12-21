import time

def time_greet():
    hour = int(time.strftime('%H'))   
    
    if 5 <= hour < 12:
        return "Good Morning"
    elif 12 <= hour < 17:
        return "Good Afternoon"
    elif 17 <= hour < 21:
        return "Good Evening"
    else:
        return "Good Night"

p = input("Enter your name: ")
Greet = time_greet()

print(Greet, p,"!!!!!!!")


