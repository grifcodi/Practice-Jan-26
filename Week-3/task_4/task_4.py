import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Калькулятор")
root.geometry("300x250")

result = tk.StringVar(value="")
def calculate(num1, num2, operator):
    res = 0
    try:
        a = float(num1.get())
        b = float(num2.get())
        operator = operator.get()

        if operator == "+":
            res = a + b
        if operator == "-":
            res = a - b
        if operator == "*":
            res = a * b
        if operator == "/":
            if b == 0:
                res = "Помилка: ділення на нуль"
            else:
                res = a / b
    except ValueError:
        res = "Помилка: введіть числа"
    result.set(res)

ttk.Label(root, text="Число 1:").grid(row=0, column=0)
num1 = ttk.Entry(root)
num1.grid(row=0, column=1)

ttk.Label(root, text="Число 2:").grid(row=3, column=0)
num2 = ttk.Entry(root)
num2.grid(row=3, column=1)

operator_frame = ttk.Frame(root)
operator_frame.grid(row=1, column=0)

operator = tk.StringVar()
ttk.Radiobutton(operator_frame, text="+", variable=operator, value="+").grid(row=0, column=0, padx=5)
ttk.Radiobutton(operator_frame, text="-", variable=operator, value="-").grid(row=0, column=1, padx=5)
ttk.Radiobutton(operator_frame, text="*", variable=operator, value="*").grid(row=0, column=2, padx=5)
ttk.Radiobutton(operator_frame, text="/", variable=operator, value="/").grid(row=0, column=3, padx=5)

ttk.Button(root, text="Обчислити", command=lambda: calculate(num1, num2, operator)).grid(row=4, column=0, columnspan=2, padx=10, pady=10)

ttk.Label(
    root,
    textvariable=result,
    relief=tk.SOLID,
    padding=10,
    anchor=tk.CENTER,
).grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="we")

root.mainloop()