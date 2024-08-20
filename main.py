import tkinter as tk

# Function to update the expression in the input field
def click_button(value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + value)

# Function to evaluate the expression and display the result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to clear the input field
def clear():
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create and place the input field
entry = tk.Entry(root, font=("Arial", 24), bd=10, insertwidth=4, width=14, borderwidth=4)
entry.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0, 4)
]

# Create and place buttons
for (text, row, col, *span) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 18), command=calculate)
    elif text == 'C':
        btn = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 18), command=clear)
    else:
        btn = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 18), command=lambda t=text: click_button(t))
    
    btn.grid(row=row, column=col, columnspan=span[0] if span else 1)

# Run the application
root.mainloop()
