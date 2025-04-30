from constants import *
import tkinter as tk
from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap import Style
from PIL import *

# Window Properties
style = Style(theme="superhero")
root = style.master
root.title("Py-Calculator")
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
root.resizable(width=False, height=False)





# Buttons

# Bottom Row
zero_button = tk.Button(root, text="0", height=3, width=23)
zero_button.place(relx=0, rely=1, anchor=tk.SW)

period_button = tk.Button(root, text=".", height=3, width=10)
period_button.place(relx=0.5, rely=1, anchor=tk.SW)

equals_button = tk.Button(root, text="=", height=3, width=10)
equals_button.place(relx=0.75, rely=1, anchor=tk.SW)
















root.mainloop()

