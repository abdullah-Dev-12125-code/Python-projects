import random

number = random.randint(1, 50)

print("Guess the number between 1 and 50!")

while True:
    guess = int(input("Enter your guess: "))
    if guess == number:
        print("🎉 You guessed it right!")
        break    
    elif guess < number:
        print("Too low! Try a bigger number.")
    elif guess > number:
        print("Too high! Try a smaller number.")
    
