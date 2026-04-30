import tkinter as tk
from tkinter import messagebox
from tasks import Task, TaskManager, validate_time
import threading, time

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
    
    add_all_tasks_to_listbox()

def remove_task():
    selected = task_listbox.curselection()
    if not selected:
        messagebox.showerror("No selection", "Please select a task to remove")
        return

    index = selected[0]
    task_manager.remove_task(task_manager.tasks[index])
    task_listbox.delete(index)

def add_all_tasks_to_listbox():
    task_listbox.delete(0, tk.END)
    for task in task_manager.tasks:
        task_listbox.insert(tk.END, f"{'[DONE]' if task.completed else '[PENDING]'} {task.name} at {task.time} - {task.executable}")

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

tk.Button(root, text="Remove Task", command=remove_task).pack()

def main():
    stop_event = threading.Event()

    def run_loop(interval=1):
        print("Starting task tracking loop...")
        while not stop_event.is_set():
            print("Checking for pending tasks...")
            any_completed = task_manager.execute_pending_tasks()
            if any_completed:
                root.after(0, add_all_tasks_to_listbox)
            time.sleep(interval)
            
    
    def on_close():
        stop_event.set()
        root.destroy()

    
    thread = threading.Thread(target=run_loop)
    thread.start()

    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()
    
if __name__ == "__main__":
    main()