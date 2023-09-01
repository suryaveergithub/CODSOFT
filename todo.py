import tkinter as tk
from tkinter import messagebox
def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")
def delete_task():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        task_list.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")
def clear_tasks():
    task_list.delete(0, tk.END)
root = tk.Tk()
root.title("To-Do List App")
task_entry = tk.Entry(root)
add_button = tk.Button(root, text="Add Task", command=add_task)
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
clear_button = tk.Button(root, text="Clear All", command=clear_tasks)
task_list = tk.Listbox(root)
task_entry.pack(pady=10)
add_button.pack()
delete_button.pack()
clear_button.pack()
task_list.pack(pady=10, fill=tk.BOTH, expand=True)
root.mainloop()