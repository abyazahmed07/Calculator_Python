import tkinter as tk
from tkinter.constants import SUNKEN

# Initialize the main window
window = tk.Tk()
window.title('Calculator by Abyaz Ahmed')
window.configure(bg='white')

# Frame for the entry widget
frame = tk.Frame(master=window, bg='white', padx=10)
frame.pack()

# Entry widget for displaying expressions and results
entry = tk.Entry(
    master=frame,
    relief=SUNKEN,
    borderwidth=3,
    width=30,
    bg='white',
    fg='black',
    insertbackground='black',
    font=('Arial', 14)
)
entry.grid(row=0, column=0, columnspan=4, ipady=10, pady=10)

# Function to handle button clicks
def myclick(number):
    entry.insert(tk.END, number)

# Function to evaluate the expression
def equal():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, 'Error')

# Function to clear the entry widget
def clear():
    entry.delete(0, tk.END)

# Button configuration
button_config = {
    'master': frame,
    'padx': 20,
    'pady': 10,
    'width': 3,
    'bg': 'black',
    'fg': 'grey',
    'activebackground': 'grey',
    'activeforeground': 'white',
    'borderwidth': 0,
    'font': ('Arial', 14)
}

# Numeric buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('0', 4, 1)
]

for (text, row, col) in buttons:
    tk.Button(
        text=text,
        command=lambda t=text: myclick(t),
        **button_config
    ).grid(row=row, column=col, pady=5)

# Operator buttons
operators = [
    ('+', 1, 3), ('-', 2, 3),
    ('*', 3, 3), ('/', 4, 3),
    ('C', 4, 0), ('=', 4, 2)
]

for (text, row, col) in operators:
    if text == 'C':
        tk.Button(
            text=text,
            command=clear,
            **button_config
        ).grid(row=row, column=col, pady=5)
    elif text == '=':
        tk.Button(
            text=text,
            command=equal,
            **button_config
        ).grid(row=row, column=col, pady=5)
    else:
        tk.Button(
            text=text,
            command=lambda t=text: myclick(t),
            **button_config
        ).grid(row=row, column=col, pady=5)

# Run the application
window.mainloop()