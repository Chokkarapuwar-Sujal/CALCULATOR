import tkinter as tk
from tkinter import messagebox
import math
import os

class AdvancedCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")

        # Set window icon
        icon_path = os.path.join(os.path.dirname(__file__), "calculator.ico")
        if os.path.exists(icon_path):
            self.root.iconbitmap(icon_path)
        else:
            print("⚠️ Icon file not found. Make sure 'calculator.ico' is in the same directory.")

        self.root.geometry("420x600")
        self.root.resizable(False, False)
        self.expression = ""

        self.create_widgets()
        self.bind_keys()

    def create_widgets(self):
        self.entry_text = tk.StringVar()
        self.entry = tk.Entry(self.root, textvariable=self.entry_text,
                              font=('Arial', 24), bd=10, relief='sunken',
                              bg='white', fg='black', justify='right', width=20)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)
        self.entry.focus_set()

        buttons = [
            ("C", 1, 0), ("←", 1, 1), ("%", 1, 2), ("/", 1, 3),
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
            ("0", 5, 0), (".", 5, 1), ("√", 5, 2), ("=", 5, 3),
            ("x²", 6, 0), ("1/x", 6, 1)
        ]

        for (text, row, col) in buttons:
            self.create_button(text, row, col)

        for i in range(7):
            self.root.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.root.grid_columnconfigure(j, weight=1)

    def create_button(self, text, row, col):
        button = tk.Button(self.root, text=text,
                           font=('Arial', 16), width=5, height=2,
                           bg='#f0f0f0', fg='black', relief='raised',
                           command=lambda: self.on_click(text))
        button.grid(row=row, column=col, sticky='nsew', padx=5, pady=5)

    def on_click(self, char):
        try:
            if char == "C":
                self.expression = ""
            elif char == "←":
                self.expression = self.expression[:-1]
            elif char == "=":
                self.expression = str(eval(self.expression))
            elif char == "√":
                self.expression = str(math.sqrt(float(self.expression)))
            elif char == "x²":
                self.expression = str(float(self.expression) ** 2)
            elif char == "1/x":
                if float(self.expression) == 0:
                    raise ZeroDivisionError
                self.expression = str(1 / float(self.expression))
            else:
                self.expression += str(char)
        except ZeroDivisionError:
            self.expression = ""
            messagebox.showerror("Math Error", "Cannot divide by zero.")
        except Exception:
            self.expression = ""
            messagebox.showerror("Error", "Invalid Input")
        self.entry_text.set(self.expression)

    def bind_keys(self):
        self.root.bind("<Key>", self.key_input)
        self.root.bind("<Return>", lambda event: self.on_click("="))
        self.root.bind("<BackSpace>", lambda event: self.on_click("←"))

    def key_input(self, event):
        if event.char.isdigit() or event.char in '+-*/.%':
            self.expression += event.char
        self.entry_text.set(self.expression)

# Start the app
if __name__ == "__main__":
    root = tk.Tk()
    calc_app = AdvancedCalculator(root)
    root.mainloop()
