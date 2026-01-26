import tkinter as tk

root = tk.Tk()
root.title("First program")
root.geometry("1024x768")

label = tk.Label(root, text="Hello, World!")

exit_button = tk.Button(root, text="Exit", command=root.destroy)

label.pack(pady=10)
exit_button.pack(pady=10)

root.mainloop()
