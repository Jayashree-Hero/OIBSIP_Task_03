import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random
import string
import pyperclip

def generate_password(length, use_uppercase, use_numbers, use_special):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for i in range(length))
    return password

class PasswordGenerator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Password Generator")
        self.geometry("400x400")
        self.configure(bg="#ADD8E6")  # Light blue background
        self.create_widgets()

    def create_widgets(self):
        label_style = {'bg': "#ADD8E6", 'font': ("Helvetica", 12, "bold")}

        tk.Label(self, text="Password Length:", **label_style).grid(row=0, column=0, pady=10, padx=10)
        self.length_entry = tk.Entry(self)
        self.length_entry.grid(row=0, column=1, pady=10, padx=10)

        self.uppercase_var = tk.BooleanVar()
        self.numbers_var = tk.BooleanVar()
        self.special_var = tk.BooleanVar()

        tk.Checkbutton(self, text="Include Uppercase", variable=self.uppercase_var, bg="#ADD8E6", font=("Helvetica", 10)).grid(row=1, columnspan=2)
        tk.Checkbutton(self, text="Include Numbers", variable=self.numbers_var, bg="#ADD8E6", font=("Helvetica", 10)).grid(row=2, columnspan=2)
        tk.Checkbutton(self, text="Include Special Characters", variable=self.special_var, bg="#ADD8E6", font=("Helvetica", 10)).grid(row=3, columnspan=2)

        self.result_label = tk.Label(self, text="", bg="#ADD8E6", font=("Helvetica", 12, "bold"))
        self.result_label.grid(row=4, columnspan=2, pady=10)

        button_style = {'bg': "#4682B4", 'fg': "white", 'font': ("Helvetica", 10, "bold"), 'width': 20, 'height': 2}
        tk.Button(self, text="Generate Password", command=self.on_generate, **button_style).grid(row=5, columnspan=2, pady=10)
        tk.Button(self, text="Copy to Clipboard", command=self.copy_to_clipboard, **button_style).grid(row=6, columnspan=2, pady=10)

    def on_generate(self):
        try:
            length = int(self.length_entry.get())
            use_uppercase = self.uppercase_var.get()
            use_numbers = self.numbers_var.get()
            use_special = self.special_var.get()

            password = generate_password(length, use_uppercase, use_numbers, use_special)
            self.result_label.config(text=password)
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number for password length.")

    def copy_to_clipboard(self):
        password = self.result_label.cget("text")
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Copied", "Password copied to clipboard.")
        else:
            messagebox.showerror("No Password", "Please generate a password first.")

if __name__ == "__main__":
    app = PasswordGenerator()
    app.mainloop()
