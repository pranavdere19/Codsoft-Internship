import tkinter as tk
from tkinter import messagebox

# Function to update expression in the text entry
def press(num):
    entry_text.set(entry_text.get() + str(num))

# Function to evaluate the final expression
def equal_press():
    try:
        result = str(eval(entry_text.get()))
        entry_text.set(result)
    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by Zero is not allowed")
        entry_text.set("")
    except Exception:
        messagebox.showerror("Error", "Invalid Input")
        entry_text.set("")

# Function to clear the entry
def clear():
    entry_text.set("")

# GUI window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("320x400")
root.resizable(False, False)

entry_text = tk.StringVar()
entry_frame = tk.Entry(root, textvariable=entry_text, font=('Arial', 20), bd=10, relief=tk.RIDGE, justify='right')
entry_frame.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=10, pady=10)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, fg="white", bg="green",
                        font=('Arial', 15, 'bold'), bd=5, width=5, height=2,
                        command=equal_press)
    else:
        btn = tk.Button(root, text=text, fg="black", bg="lightgray",
                        font=('Arial', 15, 'bold'), bd=5, width=5, height=2,
                        command=lambda t=text: press(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

# Clear button
clear_btn = tk.Button(root, text='C', fg="white", bg="red",
                      font=('Arial', 15, 'bold'), bd=5, width=23, height=2,
                      command=clear)
clear_btn.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

root.mainloop()