import tkinter as tk
from tkinter import ttk, colorchooser, filedialog, messagebox

class DrawBoard:
    def __init__(self, root):
        self.root = root
        self.root.title("Графіка")
        self.root.geometry("700x500")

        self.color = "black"
        self.drawing_mode = "line"
        self.start_x = None
        self.start_y = None

        self.toolbar = ttk.Frame(self.root)
        self.toolbar.pack(side=tk.TOP, fill=tk.X)

        self.color_button = ttk.Button(self.toolbar, text="Вибрати колір", command=self.choose_color)
        self.color_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.clear_button = ttk.Button(self.toolbar, text="Очистити", command=self.clear_canvas)
        self.clear_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.save_button = ttk.Button(self.toolbar, text="Зберегти", command=self.save_canvas)
        self.save_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.mode_button = ttk.Button(self.toolbar, text="Режим: Лінія", command=self.toggle_mode)
        self.mode_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.canvas = tk.Canvas(self.root, width=600, height=400, bg="white")
        self.canvas.pack(expand=True, fill=tk.BOTH)

        self.canvas.bind("<ButtonPress-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)

    def choose_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.color = color

    def clear_canvas(self):
        self.canvas.delete("all")

    def save_canvas(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".ps", filetypes=[("PostScript files", "*.ps")])
        if file_path:
            try:
                self.canvas.postscript(file=file_path)
            except Exception as e:
                messagebox.showerror("Помилка", f"Не вдалося зберегти файл:\n{e}")

    def toggle_mode(self):
        if self.drawing_mode == "line":
            self.drawing_mode = "circle"
            self.mode_button.config(text="Режим: Коло")
        else:
            self.drawing_mode = "line"
            self.mode_button.config(text="Режим: Лінія")

    def start_draw(self, event):
        self.start_x = event.x
        self.start_y = event.y

        if self.drawing_mode == "circle":
            r = 10
            self.canvas.create_oval(event.x - r, event.y - r, event.x + r, event.y + r, fill=self.color, outline=self.color)

    def draw(self, event):
        if self.drawing_mode == "line" and self.start_x is not None and self.start_y is not None:
            self.canvas.create_line(self.start_x, self.start_y, event.x, event.y, fill=self.color, width=2)
            self.start_x = event.x
            self.start_y = event.y

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawBoard(root)
    root.mainloop()