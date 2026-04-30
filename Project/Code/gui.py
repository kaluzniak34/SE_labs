import tkinter as tk
from tkinter import messagebox
from test import Task, TaskManager, validate_time

task_manager = TaskManager([])

def add_task():
    title = title_box.get()
    time = time_box.get()
    executable = executable_box.get()

    if not title or not time or not executable:
        messagebox.showerror("Missing fields", "Please fill in all fields")
        return

    try:
        time_validated = validate_time(time)
    except ValueError:
        messagebox.showerror("Invalid time format", "Please enter time in the format YYYY-MM-DD HH:MM:SS")
        return

    task_manager.add_task(Task(title, time_validated, executable))
    task_listbox.insert(tk.END, f"{title} at {time} - {executable}")


root = tk.Tk()
root.title("Workflow automator")

tk.Label(root, text="Add a new task", font=("Arial", 20)).pack()

tk.Label(root, text="Task Title").pack()
title_box = tk.Entry(root)
title_box.pack()

tk.Label(root, text="Task Time (YYYY-MM-DD HH:MM:SS)").pack()
time_box = tk.Entry(root)
time_box.pack()

tk.Label(root, text="Executable").pack()
executable_box = tk.Entry(root)
executable_box.pack()

tk.Button(root, text="Add Task", command=add_task).pack()

tk.Label(root, text="Scheduled tasks", font=("Arial", 20)).pack()
task_listbox = tk.Listbox(root, width=40)
task_listbox.pack()


root.mainloop()