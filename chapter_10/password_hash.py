"""
Unit 11 – Tkinter Password Hash Demo

This standalone GUI teaches a key idea:
When you create a password on a website, the site does NOT save your
actual password. It runs the password through a one-way hash function
and stores the long resulting string. Even the company that owns the
server cannot turn that string back into your password.

Run this file with: python password_hash_gui.py
"""

import tkinter as tk
from tkinter import ttk
import hashlib


def hash_password(password: str) -> str:
    """
    Convert a password into a long, irreversible string using SHA-256.
    This is similar to what real websites do before storing a password.
    """
    # Encode the password to bytes, then hash it
    password_bytes = password.encode("utf-8")
    hash_object = hashlib.sha256(password_bytes)
    # Return the hexadecimal representation (a long string of letters and numbers)
    return hash_object.hexdigest()


def on_submit():
    """Read the password, hash it, and display the result."""
    password = password_entry.get()

    if not password:
        result_var.set("Please enter a password first.")
        return

    hashed = hash_password(password)
    result_var.set(hashed)
    # Clear the password field for safety (optional teaching moment)
    password_entry.delete(0, tk.END)


def clear_fields():
    """Reset both the password and the result."""
    password_entry.delete(0, tk.END)
    result_var.set("")


# ---------------------------------------------------------------------------
# Build the window
# ---------------------------------------------------------------------------
root = tk.Tk()
root.title("Password Hash Demo – Unit 11")
root.geometry("620x320")
root.resizable(False, False)

# Main container with a little padding
main_frame = ttk.Frame(root, padding=20)
main_frame.pack(fill=tk.BOTH, expand=True)

# Title
title_label = ttk.Label(
    main_frame,
    text="How Websites Store Passwords",
    font=("Segoe UI", 16, "bold"),
)
title_label.pack(pady=(0, 8))

# Short explanation
explain_label = ttk.Label(
    main_frame,
    text=(
        "Type a password and click Submit.\n"
        "The long string below is what a server would save — not your actual password."
    ),
    justify=tk.CENTER,
    wraplength=560,
)
explain_label.pack(pady=(0, 16))

# Password entry
password_frame = ttk.Frame(main_frame)
password_frame.pack(fill=tk.X, pady=6)

ttk.Label(password_frame, text="Password:", width=12, anchor=tk.W).pack(side=tk.LEFT)
password_entry = ttk.Entry(password_frame, width=40, show="*")
password_entry.pack(side=tk.LEFT, padx=(8, 0))
password_entry.focus()

# Buttons
button_frame = ttk.Frame(main_frame)
button_frame.pack(pady=12)

submit_button = ttk.Button(button_frame, text="Submit", command=on_submit)
submit_button.pack(side=tk.LEFT, padx=6)

clear_button = ttk.Button(button_frame, text="Clear", command=clear_fields)
clear_button.pack(side=tk.LEFT, padx=6)

# Result area
result_label = ttk.Label(main_frame, text="Hashed string stored on the server:")
result_label.pack(anchor=tk.W, pady=(8, 4))

result_var = tk.StringVar()
result_entry = ttk.Entry(
    main_frame,
    textvariable=result_var,
    width=70,
    state="readonly",
    font=("Consolas", 10),
)
result_entry.pack(fill=tk.X, pady=(0, 8))

# Footer note
footer = ttk.Label(
    main_frame,
    text="SHA-256 is one-way. The original password cannot be recovered from the hash.",
    font=("Segoe UI", 9),
    foreground="#555555",
)
footer.pack(pady=(4, 0))

# Allow Enter key to submit
root.bind("<Return>", lambda event: on_submit())

root.mainloop()