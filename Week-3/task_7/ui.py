# ui.py
import tkinter as tk
from tkinter import messagebox

class MainWindow:
    def __init__(self, root, logic_module):
        self.root = root
        self.logic = logic_module

        self.root.title("Текстовий аналізатор")
        self.root.geometry("400x300")

        self.text_area = tk.Text(root, wrap="word")
        self.button_frame = tk.Frame(root)

        self.button_frame.pack(side="top", fill="x")
        self.text_area.pack(side="top", fill="both", expand=True)

        self.word_count_btn = tk.Button(self.button_frame, text="Порахувати слова", command=self.show_word_count)
        self.word_count_btn.pack(side="left", padx=5, pady=5)

        self.char_count_btn = tk.Button(self.button_frame, text="Порахувати символи", command=self.show_char_count)
        self.char_count_btn.pack(side="left", padx=5, pady=5)

    def show_word_count(self):
        text = self.text_area.get("1.0", tk.END)
        count = self.logic.count_words(text)
        messagebox.showinfo("Результат", f"Слів у тексті: {count}")

    def show_char_count(self):
        text = self.text_area.get("1.0", tk.END)
        count = self.logic.count_characters(text)
        messagebox.showinfo("Результат", f"Символів у тексті: {count}")
