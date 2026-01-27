import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Привітання")
root.geometry("400x200")

text = tk.StringVar(value="")

exit_button = ttk.Button(root, text="Вийти", command=root.destroy)
exit_button.pack(side=tk.TOP, anchor=tk.NE, fill=tk.X)

label = ttk.Label(root, textvariable=text)
label.pack(expand=True)


def greet():
    text.set("Вітаю, користувач!")

def clear():
    text.set("")

bottom_frame = ttk.Frame(root)
bottom_frame.pack(side=tk.BOTTOM, pady=20)

greet_button = ttk.Button(bottom_frame, text="Привітати", command=greet)
greet_button.pack(side=tk.LEFT, padx=5)

clear_button = ttk.Button(bottom_frame, text="Очистити", command=clear)
clear_button.pack(side=tk.RIGHT, padx=5)

root.mainloop()