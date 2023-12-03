import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Hello world")
root.geometry("1024x768")

header = ttk.Label(root, text="Hello world")
header.pack()

root.mainloop()