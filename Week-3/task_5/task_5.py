import tkinter as tk
from tkinter import ttk, colorchooser
import os

COLOR_FILE = "color.txt"
TEXT_FILE = "note.txt"

def load_color():
    if os.path.exists(COLOR_FILE):
        with open(COLOR_FILE, "r") as f:
            color = f.read().strip()
            return color
    return None

def save_color(color):
    with open(COLOR_FILE, "w") as f:
        f.write(color)

def load_text():
    if os.path.exists(TEXT_FILE):
        with open(TEXT_FILE, "r", encoding="utf-8") as f:
            content = f.read().strip()
            return content
    return None
            
def save_text():
    with open(TEXT_FILE, "w", encoding="utf-8") as f:
        f.write(text_area.get("1.0", tk.END))

root = tk.Tk()
root.title("Notebook")
root.geometry("400x300")

bg_color = load_color() or "#ffffff"

style = ttk.Style(root)
style.theme_use("default")

style.configure("Custom.TNotebook", background=bg_color)
style.configure("Custom.TNotebook.Tab", background=bg_color)
style.configure("Tab.TFrame", background=bg_color)
style.configure("Tab.TLabel", background=bg_color)
style.configure("Tab.TButton", background=bg_color)

notebook = ttk.Notebook(root, style="Custom.TNotebook")
notebook.pack(expand=True, fill="both")

tab_main = ttk.Frame(notebook, style="Tab.TFrame")
tab_setting = ttk.Frame(notebook, style="Tab.TFrame")
tab_info = ttk.Frame(notebook, style="Tab.TFrame")

notebook.add(tab_main, text="Головна")
notebook.add(tab_setting, text="Налаштування")
notebook.add(tab_info, text="Про програму")

text_area = tk.Text(tab_main, bg=bg_color, wrap="word")
text_area.pack(expand=True, fill="both", padx=5, pady=5)
text_area.insert("1.0", load_text() or "")

def apply_color(color):
    for T in ["Custom.TNotebook", "Custom.TNotebook.Tab", "Tab.TFrame", "Tab.TLabel", "Tab.TButton"]:
        style.configure(T, background=color)
    text_area.config(bg=color)

def choose_color():
    global bg_color
    color = colorchooser.askcolor()[1]
    if color:
        bg_color = color
        apply_color(bg_color)
        save_color(bg_color)

color_button = ttk.Button(tab_setting, text="Колір фону", command=choose_color)
color_button.pack(padx=5, pady=5)

info_text = ttk.Label(tab_info, text="Розробник: Пінчук Кирило, студент 3-го курсу ОМФК", style="Tab.TLabel")
info_text.pack(padx=5, pady=5, anchor="nw")

def on_closing():
    save_text()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

apply_color(bg_color)
root.mainloop()