import tkinter as tk
import tkinter.messagebox as msg
import random
import re

class PasswordGenerator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Password Generator")
        self.geometry("400x300")
        self.configure(bg="#333333")
        self.create_widgets()

    def create_widgets(self):
        # Heading Label
        heading_label = tk.Label(self, text="Password Generator", font=("Helvetica", 20), bg="#333333", fg="#ffffff")
        heading_label.pack(pady=10)

        # Length Input Frame
        length_input_frame = tk.Frame(self, bg="#333333")
        length_input_frame.pack(pady=5)

        length_label = tk.Label(length_input_frame, text="Password Length:", font=("Helvetica", 12), bg="#333333", fg="#ffffff")
        length_label.grid(row=0, column=0)

        self.length_entry = tk.Entry(length_input_frame, font=("Helvetica", 12))
        self.length_entry.grid(row=0, column=1, padx=10)

        # Strength Radio Frame
        strength_frame = tk.Frame(self, bg="#333333")
        strength_frame.pack(pady=5)

        strength_label = tk.Label(strength_frame, text="Password Strength:", font=("Helvetica", 12), bg="#333333", fg="#ffffff")
        strength_label.grid(row=0, column=0)

        self.strength_var = tk.StringVar()
        self.strength_var.set("low")

        low_strength_radio = tk.Radiobutton(strength_frame, text="Low", variable=self.strength_var, value="low", font=("Helvetica", 10), bg="#333333", fg="#ffffff", selectcolor="#333333")
        low_strength_radio.grid(row=0, column=1)

        medium_strength_radio = tk.Radiobutton(strength_frame, text="Medium", variable=self.strength_var, value="medium", font=("Helvetica", 10), bg="#333333", fg="#ffffff", selectcolor="#333333")
        medium_strength_radio.grid(row=0, column=2)

        high_strength_radio = tk.Radiobutton(strength_frame, text="High", variable=self.strength_var, value="high", font=("Helvetica", 10), bg="#333333", fg="#ffffff", selectcolor="#333333")
        high_strength_radio.grid(row=0, column=3)

        # Generate Button
        self.generate_button = tk.Button(self, text="Generate Password", font=("Helvetica", 12), bg="#4287f5", fg="#ffffff", command=self.generate_password)
        self.generate_button.pack(pady=10)

        # Display Password Label
        self.password_label = tk.Label(self, text="", font=("Helvetica", 14), bg="#333333", fg="#ffffff")
        self.password_label.pack(pady=5)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            strength = self.strength_var.get()

            if length < 4 or length > 80:
                msg.showwarning("Invalid Length", "Password length must be between 4 and 80 characters.")
                return

            password = self.generate_password_with_strength(length, strength)
            self.password_label.config(text=f"Generated Password: {password}")
        except ValueError:
            msg.showwarning("Invalid Input", "Please enter a valid password length.")

    def generate_password_with_strength(self, length, strength):
        password_chars = []

        if strength == "low":
            password_chars.extend([chr(random.randint(65, 90)) for _ in range(length)])  # Uppercase letters
            password_chars.extend([chr(random.randint(97, 122)) for _ in range(length)])  # Lowercase letters
        elif strength == "medium":
            password_chars.extend([chr(random.randint(65, 90)) for _ in range(length)])  # Uppercase letters
            password_chars.extend([chr(random.randint(97, 122)) for _ in range(length)])  # Lowercase letters
            password_chars.extend([str(random.randint(0, 9)) for _ in range(length)])  # Numbers
        elif strength == "high":
            password_chars.extend([chr(random.randint(33, 126)) for _ in range(length)])  # ASCII printable characters

        random.shuffle(password_chars)
        return ''.join(password_chars)

    def animate_button(self, color):
        self.generate_button.config(bg=color)
        self.after(100, lambda: self.animate_button("#4287f5"))

    def run(self):
        self.animate_button("#4287f5")
        self.mainloop()

if __name__ == "__main__":
    app = PasswordGenerator()
    app.run()
