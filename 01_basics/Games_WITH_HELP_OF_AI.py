import random
import time
import json
import os

# ---------- Utility Functions ----------
def print_slow(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_leaderboard():
    try:
        with open("leaderboard.json", "r") as file:
            return json.load(file)
    except:
        return {}

def save_leaderboard(board):
    with open("leaderboard.json", "w") as file:
        json.dump(board, file, indent=4)

# ---------- Mini Games ----------
def number_guessing(level):
    number = random.randint(1, 50 * level)
    max_attempts = 10 + level * 2
    attempts = 0
    score = max_attempts * 10

    print_slow(f"\n🎲 Number Guessing Game - Level {level}")
    print_slow(f"Guess a number between 1 and {50 * level}. You have {max_attempts} attempts.")

    while attempts < max_attempts:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("❌ Enter a valid number!")
            continue
        attempts += 1
        points_lost = attempts * level * 2

        if guess == number:
            print_slow(f"🎉 Correct! You guessed in {attempts} attempts.")
            print_slow(f"🏆 Score: {score - points_lost}")
            return score - points_lost
        elif abs(guess - number) <= 3:
            print_slow("🔥 Very close!")
        elif guess < number:
            print_slow("⬆️ Too low!")
        else:
            print_slow("⬇️ Too high!")

    print_slow(f"😢 Out of attempts! Number was {number}")
    return 0

def dice_roll_game():
    print_slow("\n🎲 Dice Roll Game")
    input("Press Enter to roll the dice...")
    player_roll = random.randint(1, 6)
    computer_roll = random.randint(1, 6)
    print_slow(f"You rolled: {player_roll}")
    print_slow(f"Computer rolled: {computer_roll}")

    if player_roll > computer_roll:
        print_slow("🎉 You win!")
        return 50
    elif player_roll < computer_roll:
        print_slow("💔 You lose!")
        return 0
    else:
        print_slow("🤝 It's a tie!")
        return 25

def rock_paper_scissors():
    print_slow("\n✂️ Rock-Paper-Scissors")
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    player = input("Choose rock, paper, or scissors: ").lower()
    if player not in choices:
        print("❌ Invalid choice!")
        return 0
    print_slow(f"Computer chose: {computer}")
    if player == computer:
        print_slow("🤝 It's a tie!")
        return 25
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print_slow("🎉 You win!")
        return 50
    else:
        print_slow("💔 You lose!")
        return 0

# ---------- Main Game Loop ----------
def main_game():
    clear_screen()
    print_slow("✨ Welcome to the Ultimate Python Game Collection ✨")
    username = input("Enter your name: ").strip()

    leaderboard = load_leaderboard()
    if username not in leaderboard:
        leaderboard[username] = 0

    level = 1
    total_score = leaderboard[username]

    while True:
        print_slow(f"\n🌟 Level {level} - Total Score: {total_score}")
        print_slow("Choose a game to play:")
        print("1. Number Guessing")
        print("2. Dice Roll")
        print("3. Rock-Paper-Scissors")
        print("4. View Leaderboard")
        print("5. Quit")

        choice = input("Enter choice: ")

        if choice == "1":
            score = number_guessing(level)
        elif choice == "2":
            score = dice_roll_game()
        elif choice == "3":
            score = rock_paper_scissors()
        elif choice == "4":
            print_slow("\n🏆 Leaderboard:")
            sorted_board = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)
            for i, (name, score) in enumerate(sorted_board, 1):
                print(f"{i}. {name} - {score} points")
            continue
        elif choice == "5":
            print_slow("👋 Thanks for playing! Goodbye!")
            break
        else:
            print_slow("❌ Invalid choice! Try again.")
            continue

        total_score += score
        leaderboard[username] = total_score
        save_leaderboard(leaderboard)

        print_slow(f"\n💰 Your total score: {total_score}")
        level += 1
        again = input("Do you want to continue to next level? (yes/no): ").lower()
        if again != "yes":
            print_slow("👋 See you next time!")
            break

# Start the game
main_game()
