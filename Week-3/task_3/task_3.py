import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Анкета користувача")
root.geometry("800x400")

user_name = tk.StringVar()
user_sex = tk.StringVar()
user_agree = tk.BooleanVar()
user_info = tk.StringVar()

ttk.Label(root, text="Ім'я:").grid(row=0, column=0, padx=10, pady=5)
ttk.Entry(root, textvariable=user_name).grid(row=0, column=1, padx=10, pady=5)

ttk.Label(root, text="Стать:").grid(row=1, column=0, padx=10, pady=5)
ttk.Radiobutton(root, text="Чоловіча", variable=user_sex, value="Чоловіча").grid(row=1, column=1, sticky=tk.W)
ttk.Radiobutton(root, text="Жіноча", variable=user_sex, value="Жіноча").grid(row=1, column=1, sticky=tk.E)

def save_info():
    if not user_agree.get():
        return
    name = user_name.get()
    sex = user_sex.get()
    user_info.set(f"Ім'я: {name}\nСтать: {sex}")

def toggle_button():
    if user_agree.get():
        save_button.config(state=tk.NORMAL)
    else:
        save_button.config(state=tk.DISABLED)

ttk.Checkbutton(
    root,
    text="Погоджуюсь із умовами", 
    variable=user_agree, 
    command=toggle_button,
    ).grid(row=2, column=0, columnspan=2, pady=10)

save_button = ttk.Button(
    root,
    text="Зберегти",
    command=save_info,
    state=tk.DISABLED
)
save_button.grid(row=3, column=0, columnspan=2, pady=10)

ttk.Label(
    root,
    textvariable=user_info,
    relief=tk.SOLID,
    padding=10,
    anchor=tk.CENTER,
).grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="we")

root.mainloop()