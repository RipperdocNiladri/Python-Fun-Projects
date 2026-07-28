import tkinter as tk
from tkinter import messagebox
import secrets
import string


# -----------------------------
# Password Generator Function
# -----------------------------
def generate_password():

    characters = ""

    if upper_var.get():
        characters += string.ascii_uppercase

    if lower_var.get():
        characters += string.ascii_lowercase

    if number_var.get():
        characters += string.digits

    if symbol_var.get():
        characters += string.punctuation

    if not characters:
        messagebox.showwarning(
            "Selection Required",
            "Please select at least one character type."
        )
        return

    length = length_scale.get()

    password = "".join(
        secrets.choice(characters)
        for _ in range(length)
    )

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)


# -----------------------------
# Copy Password
# -----------------------------
def copy_password():

    password = password_entry.get()

    if password == "":
        messagebox.showwarning(
            "No Password",
            "Generate a password first!"
        )
        return

    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()

    messagebox.showinfo(
        "Copied!",
        "Password copied to clipboard."
    )


# -----------------------------
# GUI
# -----------------------------
root = tk.Tk()
root.title("Secure Password Generator")
root.geometry("470x430")
root.resizable(False, False)

title = tk.Label(
    root,
    text="🔐 Secure Password Generator",
    font=("Segoe UI", 18, "bold")
)
title.pack(pady=15)

password_entry = tk.Entry(
    root,
    font=("Consolas", 15),
    justify="center",
    width=30
)
password_entry.pack(pady=10)

length_label = tk.Label(
    root,
    text="Password Length",
    font=("Segoe UI", 11)
)
length_label.pack()

length_scale = tk.Scale(
    root,
    from_=4,
    to=50,
    orient="horizontal",
    length=250
)
length_scale.set(16)
length_scale.pack()

upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
number_var = tk.BooleanVar(value=True)
symbol_var = tk.BooleanVar(value=True)

frame = tk.Frame(root)
frame.pack(pady=15)

tk.Checkbutton(
    frame,
    text="Uppercase",
    variable=upper_var,
    font=("Segoe UI", 10)
).grid(row=0, column=0, sticky="w")

tk.Checkbutton(
    frame,
    text="Lowercase",
    variable=lower_var,
    font=("Segoe UI", 10)
).grid(row=1, column=0, sticky="w")

tk.Checkbutton(
    frame,
    text="Numbers",
    variable=number_var,
    font=("Segoe UI", 10)
).grid(row=0, column=1, padx=20)

tk.Checkbutton(
    frame,
    text="Symbols",
    variable=symbol_var,
    font=("Segoe UI", 10)
).grid(row=1, column=1, padx=20)

generate_btn = tk.Button(
    root,
    text="Generate Password",
    font=("Segoe UI", 11, "bold"),
    width=22,
    command=generate_password
)
generate_btn.pack(pady=10)

copy_btn = tk.Button(
    root,
    text="Copy Password",
    font=("Segoe UI", 11),
    width=22,
    command=copy_password
)
copy_btn.pack()

footer = tk.Label(
    root,
    text="Made with Python & Tkinter",
    font=("Segoe UI", 9)
)
footer.pack(side="bottom", pady=12)

root.mainloop()