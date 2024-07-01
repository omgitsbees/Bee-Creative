import tkinter as tk
from tkinter import messagebox

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y
    
def button_click(value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text + value)

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")

# Create the main window
root = tk.Tk()
root.title("Beeculator")

# Create an entry widget
entry = tk.Entry(root, width=16, font=('Arial', 24), bd=8, insertwidth=2, justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Define button labels
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

# Add buttons to the window
row = 1
col = 0
for button in buttons:
    if button == '=':
        btn = tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 18), command=calculate)
    elif button == 'C':
        btn = tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 18), command=clear_entry)
    else:
        btn = tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 18), command=lambda b=button: button_click(b))
    btn.grid(row=row, column=col, sticky="nsew")
    col += 1
    if col > 3:
        col = 0
        row += 1

# Make the grid cells expand to fill the window
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(5):
    root.grid_rowconfigure(i, weight=1)

# Run the application
root.mainloop()