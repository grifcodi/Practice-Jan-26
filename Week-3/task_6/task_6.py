import tkinter as tk
from tkinter import filedialog, messagebox

root = tk.Tk()
root.title("Блокнот")
root.geometry("400x300")

text_change = False

def on_text_change(event):
    global text_change
    text_change = True
    text_area.edit_modified(False)

def open_file():
    global text_change
    file_path = filedialog.askopenfilename(filetypes=[("Текстові файли", "*.txt")])
    if file_path != "":
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                text_area.delete("1.0", tk.END)
                text_area.insert("1.0", content)
            text_change = False
            text_area.edit_modified(False)
        except Exception as e:
            messagebox.showerror("Помилка", f"Не вдалося відкрити файл:\n{e}")

def save_file():
    global text_change
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Текстові файли", "*.txt")])
    if file_path != "":
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                content = text_area.get("1.0", tk.END)
                f.write(content)
            text_change = False
        except Exception as e:
            messagebox.showerror("Помилка", f"Не вдалося зберегти файл:\n{e}")

def confirm_exit():
    if text_change:
        result = messagebox.askyesno("Підтвердження", "Є незбережені зміни. Ви дійсно хочете вийти?")
        if not result:
            return
    root.destroy()

text_area = tk.Text(root, wrap="word")
text_area.pack(expand=True, fill="both")
text_area.bind("<<Modified>>", on_text_change)

menu = tk.Menu(root)
root.config(menu=menu)

file = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Файл", menu=file)
file.add_command(label="Відкрити", command=open_file)
file.add_command(label="Зберегти", command=save_file)
file.add_command(label="Вийти", command=confirm_exit)

root.protocol("WM_DELETE_WINDOW", confirm_exit)

root.mainloop()