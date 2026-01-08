import tkinter as tk
from tkinter import ttk
from collections import defaultdict

movies = []

# --- Functions ---
def add_movie():
    movie = add_entry.get().strip()
    if movie:
        movies.append(movie)
        add_entry.delete(0, tk.END)
        update_movie_list()
        status_label.config(text="Movie added!", foreground="lightgreen")

def remove_movie():
    movie_to_remove = remove_entry.get().strip()
    if movie_to_remove == ".":
        status_label.config(text="No movie removed.", foreground="yellow")
    elif movie_to_remove in movies:
        movies.remove(movie_to_remove)
        remove_entry.delete(0, tk.END)
        update_movie_list()
        status_label.config(text=f"Movie '{movie_to_remove}' removed.", foreground="lightgreen")
    else:
        status_label.config(text=f"Movie '{movie_to_remove}' not found.", foreground="red")

def update_movie_list():
    movie_listbox.delete(0, tk.END)
    movies.sort()
    grouped_movies = defaultdict(list)
    for movie in movies:
        first_letter = movie[0].lower()
        grouped_movies[first_letter].append(movie)

    for letter in sorted(grouped_movies.keys()):
        letter_movies = grouped_movies[letter]
        movie_listbox.insert(tk.END, f"Movies starting with '{letter}':")
        for movie in letter_movies:
            movie_listbox.insert(tk.END, f"  - {movie}")
        if len(letter_movies) > 1:
            movie_listbox.insert(tk.END, f"   (There are {len(letter_movies)} movies starting with '{letter}')")
        else:
            movie_listbox.insert(tk.END, f"   (Only one movie starts with '{letter}')")
        movie_listbox.insert(tk.END, "")  # spacing

# --- GUI Setup ---
root = tk.Tk()
root.title("My Modern Movie List")
root.geometry("600x500")
root.config(bg="#1E1E1E")

# --- Frames ---
top_frame = tk.Frame(root, bg="#1E1E1E")
top_frame.pack(pady=10)

mid_frame = tk.Frame(root, bg="#1E1E1E")
mid_frame.pack(pady=5)

bottom_frame = tk.Frame(root, bg="#1E1E1E")
bottom_frame.pack(pady=10, fill=tk.BOTH, expand=True)

# --- Add Movie Widgets ---
tk.Label(top_frame, text="Add a movie:", fg="white", bg="#1E1E1E", font=("Helvetica", 12)).grid(row=0, column=0, padx=5)
add_entry = ttk.Entry(top_frame, width=30)
add_entry.grid(row=0, column=1, padx=5)
add_button = ttk.Button(top_frame, text="Add", command=add_movie)
add_button.grid(row=0, column=2, padx=5)
add_entry.bind("<Return>", lambda event: add_movie())  # Press Enter to add

# --- Remove Movie Widgets ---
tk.Label(mid_frame, text="Remove a movie (or '.' to skip):", fg="white", bg="#1E1E1E", font=("Helvetica", 12)).grid(row=0, column=0, padx=5)
remove_entry = ttk.Entry(mid_frame, width=30)
remove_entry.grid(row=0, column=1, padx=5)
remove_button = ttk.Button(mid_frame, text="Remove", command=remove_movie)
remove_button.grid(row=0, column=2, padx=5)
remove_entry.bind("<Return>", lambda event: remove_movie())  # Press Enter to remove

# --- Status Label ---
status_label = tk.Label(root, text="", fg="yellow", bg="#1E1E1E", font=("Helvetica", 10, "bold"))
status_label.pack(pady=5)

# --- Movie Listbox with Scrollbar ---
scrollbar = tk.Scrollbar(bottom_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

movie_listbox = tk.Listbox(bottom_frame, width=70, height=15, font=("Helvetica", 12),
                           bg="#2E2E2E", fg="white", yscrollcommand=scrollbar.set, selectbackground="#555555")
movie_listbox.pack(fill=tk.BOTH, expand=True)
scrollbar.config(command=movie_listbox.yview)

root.mainloop()
