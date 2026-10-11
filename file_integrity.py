
import hashlib
import tkinter as tk
from tkinter import filedialog, messagebox
import os

reference_hash = None
selected_file = None


def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while True:
            data = file.read(4096)
            if not data:
                break
            sha256.update(data)

    return sha256.hexdigest()


def select_file():
    global selected_file, reference_hash

    folder = os.path.dirname(os.path.abspath(__file__))

    file_path = filedialog.askopenfilename(
        title="Select a File",
        initialdir=folder
    )

    if file_path:
        selected_file = file_path
        reference_hash = None

        file_label.config(
            text="Selected File: " + os.path.basename(file_path)
        )

        hash_text.delete("1.0", tk.END)
        current_hash_text.delete("1.0", tk.END)
        result_label.config(text="")

        status_label.config(
            text="File selected. Generate the reference hash."
        )


def generate_hash():
    global reference_hash

    if not selected_file:
        messagebox.showwarning("Warning", "Please select a file first.")
        return

    try:
        reference_hash = calculate_hash(selected_file)

        hash_text.delete("1.0", tk.END)
        hash_text.insert(tk.END, reference_hash)

        current_hash_text.delete("1.0", tk.END)
        result_label.config(text="")

        status_label.config(text="Reference hash generated successfully.")

    except OSError as error:
        messagebox.showerror("Error", str(error))


def verify_file():
    if not selected_file or not reference_hash:
        messagebox.showwarning(
            "Warning", "Select a file and generate its reference hash first."
        )
        return

    try:
        current_hash = calculate_hash(selected_file)

        current_hash_text.delete("1.0", tk.END)
        current_hash_text.insert(tk.END, current_hash)

        if current_hash == reference_hash:
            result_label.config(
                text="FILE INTEGRITY VERIFIED",
                fg="green"
            )
        else:
            result_label.config(
                text="FILE MODIFICATION DETECTED",
                fg="red"
            )

        status_label.config(text="Verification completed.")

    except OSError as error:
        messagebox.showerror("Error", str(error))


root = tk.Tk()
root.title("File Integrity Verification using SHA-256")
root.geometry("750x550")
root.configure(bg="#f0f4f8")

tk.Label(
    root,
    text="File Integrity Verification using SHA-256",
    font=("Arial", 16, "bold"),
    bg="#f0f4f8"
).pack(pady=15)

tk.Button(
    root, text="Select File", command=select_file,
    width=20
).pack(pady=5)

file_label = tk.Label(
    root, text="Selected File: None",
    bg="#f0f4f8", wraplength=700
)
file_label.pack(pady=5)

tk.Button(
    root, text="Generate SHA-256 Hash",
    command=generate_hash, width=25
).pack(pady=8)

tk.Label(
    root, text="Reference SHA-256 Hash:",
    bg="#f0f4f8", font=("Arial", 10, "bold")
).pack()

hash_text = tk.Text(root, height=3, width=78, wrap="word")
hash_text.pack(pady=5)

tk.Button(
    root, text="Verify File Integrity",
    command=verify_file, width=25
).pack(pady=8)

tk.Label(
    root, text="Current SHA-256 Hash:",
    bg="#f0f4f8", font=("Arial", 10, "bold")
).pack()

current_hash_text = tk.Text(root, height=3, width=78, wrap="word")
current_hash_text.pack(pady=5)

result_label = tk.Label(
    root, text="", font=("Arial", 13, "bold"),
    bg="#f0f4f8"
)
result_label.pack(pady=8)

status_label = tk.Label(
    root, text="Ready",
    bg="#f0f4f8", fg="blue"
)
status_label.pack(pady=5)

root.mainloop()
