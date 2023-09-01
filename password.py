import tkinter as tk
import random
import string

class PasswordGeneratorApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.length_label = tk.Label(root, text="Password Length:")
        self.length_label.pack(pady=10)

        self.length_entry = tk.Entry(root)
        self.length_entry.pack()

        self.complexity_label = tk.Label(root, text="Password Complexity:")
        self.complexity_label.pack(pady=10)

        self.complexity_var = tk.StringVar(value="Medium")
        self.complexity_radio_frame = tk.Frame(root)
        self.complexity_radio_frame.pack()

        complexities = ["Easy", "Medium", "Hard"]
        for complexity in complexities:
            tk.Radiobutton(
                self.complexity_radio_frame,
                text=complexity,
                variable=self.complexity_var,
                value=complexity,
            ).pack(side=tk.LEFT, padx=10)

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=20)

        self.password_label = tk.Label(root, text="", font=("Helvetica", 16))
        self.password_label.pack()

    def generate_password(self):
        length = int(self.length_entry.get())
        complexity = self.complexity_var.get()

        if complexity == "Easy":
            characters = string.ascii_letters
        elif complexity == "Medium":
            characters = string.ascii_letters + string.digits
        else:
            characters = string.ascii_letters + string.digits + string.punctuation

        password = "".join(random.choice(characters) for _ in range(length))
        self.password_label.config(text=password)

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "_main_":
    main()