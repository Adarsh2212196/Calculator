import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        master.resizable(False, False)

        self.entry = tk.Entry(master, width=20, font=("Arial", 24), bd=5, relief=tk.RIDGE, justify='right')
        self.entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            ('%', 1, 0), ('CE', 1, 1), ('C', 1, 2), ('⌫', 1, 3),
            ('1/x', 2, 0), ('x²', 2, 1), ('√x', 2, 2), ('/', 2, 3),
            ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('*', 3, 3),
            ('4', 4, 0), ('5', 4, 1), ('6', 4, 2), ('-', 4, 3),
            ('1', 5, 0), ('2', 5, 1), ('3', 5, 2), ('+', 5, 3),
            ('+/-', 6, 0), ('0', 6, 1), ('.', 6, 2), ('=', 6, 3)
        ]

        for (text, row, col) in buttons:
            if text == '=':
                btn = tk.Button(master, text=text, width=5, height=2, font=("Arial", 18),
                                command=self.calculate)
            elif text == 'C':
                btn = tk.Button(master, text=text, width=5, height=2, font=("Arial", 18),
                                command=self.clear)
            elif text == '⌫':
                btn = tk.Button(master, text=text, width=5, height=2, font=("Arial", 18),
                                command=self.backspace)
            elif text == '+/-':
                btn = tk.Button(master, text=text, width=5, height=2, font=("Arial", 18),
                                command=self.negate)
            elif text == 'x²':
                btn = tk.Button(master, text=text, width=5, height=2, font=("Arial", 18),
                                command=self.square)
            elif text == '√x':
                btn = tk.Button(master, text=text, width=5, height=2, font=("Arial", 18),
                                command=self.sqrt)
            elif text == '1/x':
                btn = tk.Button(master, text=text, width=5, height=2, font=("Arial", 18),
                                command=self.inverse)
            else:
                btn = tk.Button(master, text=text, width=5, height=2, font=("Arial", 18),
                                command=lambda t=text: self.append(t))
            btn.grid(row=row, column=col, padx=2, pady=2)

    def append(self, char):
        self.entry.insert(tk.END, char)

    def clear(self):
        self.entry.delete(0, tk.END)

    def backspace(self):
        current = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, current[:-1])

    def negate(self):
        try:
            current = self.entry.get()
            if current:
                if current.startswith('-'):
                    self.entry.delete(0)
                    self.entry.insert(0, current[1:])
                else:
                    self.entry.delete(0, tk.END)
                    self.entry.insert(0, '-' + current)
        except:
            pass

    def square(self):
        try:
            current = float(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(current ** 2))
        except:
            pass

    def sqrt(self):
        try:
            current = float(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(current ** 0.5))
        except:
            pass

    def inverse(self):
        try:
            current = float(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(1 / current))
        except:
            pass

    def calculate(self):
        try:
            result = eval(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))
        except:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")

if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
