from constants import *
import tkinter as tk
from tkinter import Label
from ttkbootstrap import Style


# Window Properties
style = Style(theme="superhero")
root = style.master
root.title("Py-Calculator")
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
root.resizable(width=False, height=False)


# Variables
num_1 = ""
num_2 = ""
has_period_1 = False
has_period_2 = False
chosen_method = ""
editing_first_number = True
editing_second_number = False
result = 0

result_text = Label(root, text="",width=50,height=30)
result_text.place(rely=0)

def add_one_to_str():
    global num_1
    global num_2
    global editing_first_number
    global editing_second_number
    if editing_first_number:
        num_1 += "1"
        result_text.config(text=num_1)
    else:
        num_2 += "1"
        result_text.config(text=num_2)

def add_two_to_str():
    global num_1
    global num_2
    global editing_first_number
    global editing_second_number
    if editing_first_number:
        num_1 += "2"
        result_text.config(text=num_1)
    else:
        num_2 += "2"
        result_text.config(text=num_2)

def add_three_to_str():
    global num_1
    global num_2
    global editing_first_number
    global editing_second_number
    if editing_first_number:
        num_1 += "3"
        result_text.config(text=num_1)
    else:
        num_2 += "3"
        result_text.config(text=num_2)

def add_four_to_str():
    global num_1
    global num_2
    global editing_first_number
    global editing_second_number
    if editing_first_number:
        num_1 += "4"
        result_text.config(text=num_1)
    else:
        num_2 += "4"
        result_text.config(text=num_2)


def add_five_to_str():
    global num_1
    global num_2
    global editing_first_number
    global editing_second_number
    if editing_first_number:
        num_1 += "5"
        result_text.config(text=num_1)
    else:
        num_2 += "5"
        result_text.config(text=num_2)


def add_six_to_str():
    global num_1
    global num_2
    global editing_first_number
    global editing_second_number
    if editing_first_number:
        num_1 += "6"
        result_text.config(text=num_1)
    else:
        num_2 += "6"
        result_text.config(text=num_2)


def add_seven_to_str():
    global num_1
    global num_2
    global editing_first_number
    global editing_second_number
    if editing_first_number:
        num_1 += "7"
        result_text.config(text=num_1)
    else:
        num_2 += "7"
        result_text.config(text=num_2)


def add_eight_to_str():
    global num_1
    global num_2
    global editing_first_number
    global editing_second_number
    if editing_first_number:
        num_1 += "8"
        result_text.config(text=num_1)
    else:
        num_2 += "8"
        result_text.config(text=num_2)


def add_nine_to_str():
    global num_1
    global num_2
    global editing_first_number
    global editing_second_number
    if editing_first_number:
        num_1 += "9"
        result_text.config(text=num_1)
    else:
        num_2 += "9"
        result_text.config(text=num_2)


def add_zero_to_str():
    global num_1
    global num_2
    global editing_first_number
    global editing_second_number
    if editing_first_number:
        num_1 += "0"
        result_text.config(text=num_1)
    else:
        num_2 += "0"
        result_text.config(text=num_2)







def clear_all_numbers():
    global num_1
    global num_2
    global editing_first_number
    global editing_second_number
    global has_period_1
    global has_period_2
    num_1 = ""
    num_2 = ""
    editing_first_number = True
    editing_second_number = False
    has_period_2 = False
    has_period_1 = False
    result_text.config(text=num_1)

def add_period():
    global num_1
    global num_2
    global has_period_1
    global has_period_2
    if has_period_1 == False and editing_first_number == True:
        num_1 += "."
        result_text.config(text=num_1)
        has_period_1 = True
    else:
        pass
    if has_period_2 == False and editing_second_number == True:
        num_2 += "."
        result_text.config(text=num_2)
        has_period_2 = True
    else:
        pass

    

def set_method_to_divide():
    global chosen_method
    global editing_first_number
    global editing_second_number
    editing_first_number = False
    editing_second_number = True

    result_text.config(text="")
    chosen_method = "divide"

def set_method_to_add():
    global chosen_method
    global editing_first_number
    global editing_second_number
    editing_first_number = False
    editing_second_number = True

    result_text.config(text="")

    chosen_method = "add"

def set_method_to_minus():
    global chosen_method
    global editing_first_number
    global editing_second_number
    editing_first_number = False
    editing_second_number = True
    chosen_method = "minus"

    result_text.config(text="")

def set_method_to_times():
    global chosen_method
    chosen_method = "times"
def add():
    global num_2
    global num_1
    global result
    result = float(num_1) + float(num_2)

def minus():
    global num_1
    global num_2
    global result
    result = float(num_1) - float(num_2)

def divide():
    global num_1
    global num_2
    global result
    result = float(num_1) / float(num_2)



def equals():
    global result
    global editing_first_number
    global editing_second_number
    editing_first_number = True
    editing_second_number = False

    if chosen_method == "add":
        add()
        result_text.config(text=str(result))
    if chosen_method == "minus":
        minus()
        result_text.config(text=str(result))
    if chosen_method == "divide":
        divide()
        result_text.config(text=str(result))








# Buttons

# Fith Row
zero_button = tk.Button(root, text="0", font=("Nunito Sans", 10), height=3, width=23, command= add_zero_to_str)
zero_button.place(relx=0, rely=1, anchor=tk.SW)

period_button = tk.Button(root, text=".", font=("Nunito Sans", 10), height=3, width=10, command=add_period)
period_button.place(relx=0.5, rely=1, anchor=tk.SW)

equals_button = tk.Button(root, text="=", font=("Nunito Sans", 10), height=3, width=10, command=equals)
equals_button.place(relx=0.75, rely=1, anchor=tk.SW)

# Fourth Row
one_button = tk.Button(root, text="1", font=("Nunito Sans", 10), height=3, width=10, command=add_one_to_str)
one_button.place(relx=0, rely=0.905, anchor=tk.SW)

two_button = tk.Button(root, text="2", font=("Nunito Sans", 10), height=3, width=10, command=add_two_to_str)
two_button.place(relx=0.25, rely=0.905, anchor=tk.SW)

three_button = tk.Button(root, text="3", font=("Nunito Sans", 10), height=3, width=10, command=add_three_to_str)
three_button.place(relx=0.5, rely=0.905, anchor=tk.SW)

plus_button = tk.Button(root, text="+", font=("Nunito Sans", 10), height=3, width=10, command= set_method_to_add)
plus_button.place(relx=0.75, rely=0.905, anchor=tk.SW)

# Third Row
four_button = tk.Button(root, text="4", font=("Nunito Sans", 10), height=3, width=10, command= add_four_to_str)
four_button.place(relx=0, rely=0.815, anchor=tk.SW)

five_button = tk.Button(root, text="5", font=("Nunito Sans", 10), height=3, width=10, command= add_five_to_str)
five_button.place(relx=0.25, rely=0.815, anchor=tk.SW)

six_button = tk.Button(root, text="6", font=("Nunito Sans", 10), height=3, width=10, command= add_six_to_str)
six_button.place(relx=0.5, rely=0.815, anchor=tk.SW)

minus_button = tk.Button(root, text="-", font=("Nunito Sans", 10), height=3, width=10, command=set_method_to_minus)
minus_button.place(relx=0.75, rely=0.815, anchor=tk.SW)

# Second Row
seven_button = tk.Button(root, text="7", font=("Nunito Sans", 10), height=3, width=10, command= add_seven_to_str)
seven_button.place(relx=0, rely=0.725, anchor=tk.SW)

eight_button = tk.Button(root, text="8", font=("Nunito Sans", 10), height=3, width=10, command=add_eight_to_str)
eight_button.place(relx=0.25, rely=0.725, anchor=tk.SW)

nine_button = tk.Button(root, text="9", font=("Nunito Sans", 10), height=3, width=10, command= add_nine_to_str)
nine_button.place(relx=0.5, rely=0.725, anchor=tk.SW)

times_button = tk.Button(root, text="X", font=("Nunito Sans", 10), height=3, width=10, command= set_method_to_times)
times_button.place(relx=0.75, rely=0.725, anchor=tk.SW)

# First Row
ac_button = tk.Button(root, text="AC", font=("Nunito Sans", 10), height=3, width=10, command=clear_all_numbers)
ac_button.place(relx=0, rely=0.64, anchor=tk.SW)

change_sign_button = tk.Button(root, text="+/-", font=("Nunito Sans", 10), height=3, width=10)
change_sign_button.place(relx=0.25, rely=0.64, anchor=tk.SW)

percent_button = tk.Button(root, text="%",  font=("Nunito Sans", 10),height=3, width=10)
percent_button.place(relx=0.5, rely=0.64, anchor=tk.SW)

divide_button = tk.Button(root, text="÷", font=("Nunito Sans", 10), height=3, width=10, command=set_method_to_divide)
divide_button.place(relx=0.75, rely=0.64, anchor=tk.SW)

root.mainloop()

