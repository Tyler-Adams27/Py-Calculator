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

# Fith Row
zero_button = tk.Button(root, text="0", font=("Nunito Sans", 10), height=3, width=23)
zero_button.place(relx=0, rely=1, anchor=tk.SW)

period_button = tk.Button(root, text=".", font=("Nunito Sans", 10), height=3, width=10)
period_button.place(relx=0.5, rely=1, anchor=tk.SW)

equals_button = tk.Button(root, text="=", font=("Nunito Sans", 10), height=3, width=10)
equals_button.place(relx=0.75, rely=1, anchor=tk.SW)

# Fourth Row
one_button = tk.Button(root, text="1", font=("Nunito Sans", 10), height=3, width=10)
one_button.place(relx=0, rely=0.905, anchor=tk.SW)

two_button = tk.Button(root, text="2", font=("Nunito Sans", 10), height=3, width=10)
two_button.place(relx=0.25, rely=0.905, anchor=tk.SW)

three_button = tk.Button(root, text="3", font=("Nunito Sans", 10), height=3, width=10)
three_button.place(relx=0.5, rely=0.905, anchor=tk.SW)

plus_button = tk.Button(root, text="+", font=("Nunito Sans", 10), height=3, width=10)
plus_button.place(relx=0.75, rely=0.905, anchor=tk.SW)

# Third Row
four_button = tk.Button(root, text="4", font=("Nunito Sans", 10), height=3, width=10)
four_button.place(relx=0, rely=0.815, anchor=tk.SW)

five_button = tk.Button(root, text="5", font=("Nunito Sans", 10), height=3, width=10)
five_button.place(relx=0.25, rely=0.815, anchor=tk.SW)

six_button = tk.Button(root, text="6", font=("Nunito Sans", 10), height=3, width=10)
six_button.place(relx=0.5, rely=0.815, anchor=tk.SW)

minus_button = tk.Button(root, text="-", font=("Nunito Sans", 10), height=3, width=10)
minus_button.place(relx=0.75, rely=0.815, anchor=tk.SW)

# Second Row
seven_button = tk.Button(root, text="7", font=("Nunito Sans", 10), height=3, width=10)
seven_button.place(relx=0, rely=0.725, anchor=tk.SW)

eight_button = tk.Button(root, text="8", font=("Nunito Sans", 10), height=3, width=10)
eight_button.place(relx=0.25, rely=0.725, anchor=tk.SW)

nine_button = tk.Button(root, text="9", font=("Nunito Sans", 10), height=3, width=10)
nine_button.place(relx=0.5, rely=0.725, anchor=tk.SW)

times_button = tk.Button(root, text="X", font=("Nunito Sans", 10), height=3, width=10)
times_button.place(relx=0.75, rely=0.725, anchor=tk.SW)

# First Row
ac_button = tk.Button(root, text="AC", font=("Nunito Sans", 10), height=3, width=10)
ac_button.place(relx=0, rely=0.64, anchor=tk.SW)

change_sign_button = tk.Button(root, text="+/-", font=("Nunito Sans", 10), height=3, width=10)
change_sign_button.place(relx=0.25, rely=0.64, anchor=tk.SW)

percent_button = tk.Button(root, text="%",  font=("Nunito Sans", 10),height=3, width=10)
percent_button.place(relx=0.5, rely=0.64, anchor=tk.SW)

divide_button = tk.Button(root, text="÷", font=("Nunito Sans", 10), height=3, width=10)
divide_button.place(relx=0.75, rely=0.64, anchor=tk.SW)
















root.mainloop()

