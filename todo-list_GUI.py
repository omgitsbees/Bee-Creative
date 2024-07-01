import tkinter as tk
from tkinter import messagebox

# Define a dictionary to store tasks
tasks = {}

# Function to add a task
def add_task():
    task = task_entry.get()
    if task:
        tasks[len(tasks) + 1] = {'task': task, 'completed': False}
        update_task_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to mark a task as completed
def complete_task():
    task_id = int(task_listbox.curselection()[0]) + 1
    if task_id in tasks:
        tasks[task_id]['completed'] = True
        update_task_list()

# Function to update the task list
def update_task_list():
    task_listbox.delete(0, tk.END)
    for task_id, task_info in tasks.items():
        status = '✓' if task_info['completed'] else '✗'
        task_listbox.insert(tk.END, f"{task_id}. [{status}] {task_info['task']}")

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Task Entry
task_entry = tk.Entry(root, width=50)
task_entry.grid(row=0, column=0, padx=10, pady=10)

# Add Task Button
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.grid(row=0, column=1, padx=10, pady=10)

# Task Listbox
task_listbox = tk.Listbox(root, width=60, height=10)
task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Complete Task Button
complete_button = tk.Button(root, text="Complete Task", command=complete_task)
complete_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Initialize with existing tasks if any
update_task_list()

# Run the application
root.mainloop()
