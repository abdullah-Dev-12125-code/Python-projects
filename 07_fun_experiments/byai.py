import tkinter as tk
from tkinter import messagebox

inventory = []

def add_fruit():
    fruit = fruit_entry.get()
    if fruit:
        inventory.append(fruit)
        fruit_listbox.insert(tk.END, fruit)
        fruit_entry.delete(0, tk.END)

def remove_fruit():
    selected = fruit_listbox.curselection()
    if selected:
        fruit = fruit_listbox.get(selected)
        inventory.remove(fruit)
        fruit_listbox.delete(selected)
    else:
        messagebox.showinfo("Info", "Select a fruit to remove")

root = tk.Tk()
root.title("Grocery Inventory System")

tk.Label(root, text="Enter Fruit Name:").pack()
fruit_entry = tk.Entry(root)
fruit_entry.pack()

tk.Button(root, text="Add Fruit", command=add_fruit).pack()
tk.Button(root, text="Remove Selected Fruit", command=remove_fruit).pack()

fruit_listbox = tk.Listbox(root)
fruit_listbox.pack()

root.mainloop()
