import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
# here, we replace open("file.txt", "w") with tkinters function
with filedialog.asksaveasfile(mode="w", defaultextension=".txt") as f:
     f.write("blablahblah")
