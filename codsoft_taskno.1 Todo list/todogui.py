import tkinter as tk
from tkinter import messagebox

# ---------------- Functions ---------------- #
def add_task():
    task = task_entry.get()
    if task.strip() != "":
        tasks_listbox.insert(tk.END, task + " [❌ Not Done]")
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    try:
        index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(index)
    except:
        messagebox.showwarning("Warning", "Select a task to delete")

def mark_task():
    try:
        index = tasks_listbox.curselection()[0]
        task = tasks_listbox.get(index)

        # Toggle status
        if "[❌ Not Done]" in task:
            task = task.replace("[❌ Not Done]", "[✅ Done]")
        elif "[✅ Done]" in task:
            task = task.replace("[✅ Done]", "[❌ Not Done]")

        tasks_listbox.delete(index)
        tasks_listbox.insert(index, task)
    except:
        messagebox.showwarning("Warning", "Select a task to mark")

def update_task():
    try:
        index = tasks_listbox.curselection()[0]
        task = tasks_listbox.get(index)

        # Get new text
        new_task = task_entry.get().strip()
        if new_task != "":
            # Preserve status
            status = "[✅ Done]" if "[✅ Done]" in task else "[❌ Not Done]"
            tasks_listbox.delete(index)
            tasks_listbox.insert(index, new_task + " " + status)
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")
    except:
        messagebox.showwarning("Warning", "Select a task to update")

# ---------------- UI ---------------- #
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x500")

# Entry field
task_entry = tk.Entry(root, width=35, font=("Arial", 12))
task_entry.pack(pady=10)

# Buttons Frame
btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

add_button = tk.Button(btn_frame, text="Add Task", width=12, command=add_task)
add_button.grid(row=0, column=0, padx=5)

update_button = tk.Button(btn_frame, text="Update Task", width=12, command=update_task)
update_button.grid(row=0, column=1, padx=5)

mark_button = tk.Button(btn_frame, text="Mark Done/Undone", width=15, command=mark_task)
mark_button.grid(row=1, column=0, padx=5, pady=5)

delete_button = tk.Button(btn_frame, text="Delete Task", width=12, command=delete_task)
delete_button.grid(row=1, column=1, padx=5, pady=5)

# Listbox
tasks_listbox = tk.Listbox(root, width=50, height=15, font=("Arial", 12))
tasks_listbox.pack(pady=10)

root.mainloop()