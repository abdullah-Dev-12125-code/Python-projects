import tkinter as tk
from math import sin, cos, tan, sqrt, log, radians
import webbrowser
import threading
import time

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            expression = str(entry.get())
            result = eval(expression)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except ZeroDivisionError:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error: Divide by 0")
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "sin":
        try:
            val = radians(float(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, sin(val))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "cos":
        try:
            val = radians(float(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, cos(val))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "tan":
        try:
            val = radians(float(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, tan(val))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "√":
        try:
            val = float(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, sqrt(val))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "log":
        try:
            val = float(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, log(val))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "HB":  # Happy Birthday Easter egg 🎂
        start_animation()
    else:
        entry.insert(tk.END, text)


def start_animation():
    """Rickroll Animation 🎉"""
    anim = tk.Toplevel(root)
    anim.title("🎉 Surprise! 🎉")
    anim.geometry("400x200")
    anim.config(bg="black")

    label = tk.Label(anim, text="🎵 Click here 🎵", fg="pink", bg="black", font=("Arial", 16, "bold"))
    label.pack(expand=True)

    colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
    def color_cycle():
        for i in range(14):
            label.config(fg=colors[i % len(colors)])
            anim.update()
            time.sleep(0.2)
        anim.destroy()
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")  # Rickroll link

    threading.Thread(target=color_cycle).start()


# GUI setup
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x600")
root.config(bg="black")

# Entry field
entry = tk.Entry(root, font=("Arial", 24), bg="black", fg="white", borderwidth=0, justify="right")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15, padx=10, pady=20, sticky="nsew")

# Button layout
buttons = [
    ["C", "√", "log", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "**", "="],
    ["sin", "cos", "tan", "HB"]  # 🎉 added HB (Happy Birthday) button
]

# Create buttons with grid alignment
for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        if text == "":  # skip empty spaces
            continue
        btn = tk.Button(
            root, text=text, font=("Arial", 18, "bold"),
            relief="flat", bg="#222", fg="white",
            activebackground="#555", activeforeground="white",
            borderwidth=0, padx=10, pady=10
        )
        btn.grid(row=i+1, column=j, sticky="nsew", padx=3, pady=3)
        btn.bind("<Button-1>", click)

# Make all rows and columns expand evenly
for i in range(7):  # 1 entry + 6 button rows
    root.rowconfigure(i, weight=1)
for j in range(4):  # 4 columns 
    root.columnconfigure(j, weight=1)

root.mainloop()

