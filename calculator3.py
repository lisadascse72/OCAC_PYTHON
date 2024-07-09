import tkinter as tk
from math import *

# Create the main window
root = tk.Tk()
root.title("Lisa Ka Scientific Calculator")
root.configure(bg='pink')  # Set background color to pink

# Entry widget to display the expression
entry = tk.Entry(root, width=40, borderwidth=5, bg='pink', fg='white')
entry.grid(row=0, column=0, columnspan=5)

# Function to update the entry with the button clicked
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

# Function to clear the entry
def button_clear():
    entry.delete(0, tk.END)

# Function to calculate the expression
def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to handle square root
def button_sqrt():
    try:
        result = sqrt(float(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to handle exponentiation
def button_pow():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + "**")

# Function to handle sine
def button_sin():
    try:
        result = sin(radians(float(entry.get())))
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to handle cosine
def button_cos():
    try:
        result = cos(radians(float(entry.get())))
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to handle tangent
def button_tan():
    try:
        result = tan(radians(float(entry.get())))
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Creating button widgets
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0), ('sqrt', 5, 1), ('pow', 5, 2), ('sin', 6, 0),
    ('cos', 6, 1), ('tan', 6, 2), ('Enter', 6, 3)
]

for (text, row, column) in buttons:
    if text == 'sqrt':
        button = tk.Button(root, text=text, padx=20, pady=20, command=button_sqrt, bg='pink', fg='white')
    elif text == 'pow':
        button = tk.Button(root, text=text, padx=20, pady=20, command=button_pow, bg='pink', fg='white')
    elif text == 'C':
        button = tk.Button(root, text=text, padx=20, pady=20, command=button_clear, bg='pink', fg='white')
    elif text == '=':
        button = tk.Button(root, text=text, padx=20, pady=20, command=button_equal, bg='pink', fg='white')
    elif text == 'sin':
        button = tk.Button(root, text=text, padx=20, pady=20, command=button_sin, bg='pink', fg='white')
    elif text == 'cos':
        button = tk.Button(root, text=text, padx=20, pady=20, command=button_cos, bg='pink', fg='white')
    elif text == 'tan':
        button = tk.Button(root, text=text, padx=20, pady=20, command=button_tan, bg='pink', fg='white')
    elif text == 'Enter':
        button = tk.Button(root, text=text, padx=20, pady=20, command=button_equal, bg='pink', fg='white')
    else:
        button = tk.Button(root, text=text, padx=20, pady=20, command=lambda t=text: button_click(t), bg='pink', fg='white')
    button.grid(row=row, column=column)

# Run the main loop
root.mainloop()
