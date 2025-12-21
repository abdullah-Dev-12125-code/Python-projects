import tkinter as tk
import random

# Quiz questions
questions = [
    ["What is the capital of Pakistan?", "Islamabad", "Lahore", "Karachi", "Multan", "A"],
    ["Which language is used to write Python?", "Snake", "English", "Programming", "Binary", "C"],
    ["What is 5 + 7?", "10", "11", "12", "13", "C"],
    ["What is the capital of France?", "Paris", "London", "Rome", "Berlin", "A"],
    ["Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Saturn", "B"],
    ["What is the national sport of Pakistan?", "Hockey", "Cricket", "Football", "Kabaddi", "A"],
    ["Who wrote Python programming language?", "Guido van Rossum", "Elon Musk", "Bill Gates", "Mark Zuckerberg", "A"],
    ["What is the largest mammal?", "Elephant", "Whale Shark", "Blue Whale", "Giraffe", "C"],
    ["What is 2 + 2?", "3", "4", "5", "6", "B"],
    ["What is 10 - 4?", "5", "6", "7", "8", "B"],
    ["What is 3 × 6?", "16", "17", "18", "19", "C"],
    ["What is 12 ÷ 3?", "3", "4", "5", "6", "B"],
    ["What is the capital of India?", "Mumbai", "Delhi", "Chennai", "Kolkata", "B"],
    ["Which gas do humans need to breathe?", "Carbon Dioxide", "Oxygen", "Nitrogen", "Helium", "B"],
    ["Who was the first man on the Moon?", "Neil Armstrong", "Buzz Aldrin", "Yuri Gagarin", "Michael Collins", "A"],
    ["What is the smallest prime number?", "0", "1", "2", "3", "C"],
    ["Which is the fastest land animal?", "Tiger", "Lion", "Cheetah", "Horse", "C"],
    ["What is H2O commonly known as?", "Water", "Oxygen", "Hydrogen", "Salt", "A"],
    ["What is 7 × 8?", "54", "5x 5", "56", "57", "C"],
    ["Which continent is Egypt in?", "Asia", "Europe", "Africa", "South America", "C"],
    ["What is 15 ÷ 3?", "3", "4", "5", "6", "C"],
    ["Who is known as the Father of Computers?", "Charles Babbage", "Albert Einstein", "Isaac Newton", "Alan Turing", "A"]
]

random.shuffle(questions)

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.root.title("Made by NBPYT")
        self.score = 0
        self.q_index = 0

        self.question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=400, justify="center")
        self.question_label.pack(pady=20)

        self.buttons = []
        for i in range(4):
            btn = tk.Button(root, text="", font=("Arial", 12), width=30, command=lambda idx=i: self.check_answer(idx))
            btn.pack(pady=5)
            self.buttons.append(btn)

        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

        self.next_button = tk.Button(root, text="Next", command=self.next_question)
        self.next_button.pack(pady=10)

        self.load_question()

    def load_question(self):
        if self.q_index < len(questions):
            q = questions[self.q_index]
            self.question_label.config(text=q[0])
            self.buttons[0].config(text="A. " + q[1])
            self.buttons[1].config(text="B. " + q[2])
            self.buttons[2].config(text="C. " + q[3])
            self.buttons[3].config(text="D. " + q[4])
            self.result_label.config(text="")
        else:
            self.end_quiz()

    def check_answer(self, idx):
        correct = questions[self.q_index][5]
        chosen = ["A", "B", "C", "D"][idx]
        if chosen == correct:
            self.result_label.config(text="✅ Correct!", fg="green")
            self.score += 1
        else:
            self.result_label.config(text=f"❌ Wrong! Correct answer: {correct}", fg="red")

    def next_question(self):
        self.q_index += 1
        self.load_question()

    def end_quiz(self):
        self.question_label.config(text=f"🎯 Final Score: {self.score} / {len(questions)}")
        for btn in self.buttons:
            btn.pack_forget()
        self.next_button.pack_forget()
        self.result_label.pack_forget()

root = tk.Tk()
app = QuizApp(root)
root.mainloop()

