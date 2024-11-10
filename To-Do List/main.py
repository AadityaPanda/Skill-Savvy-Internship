import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.tasks = []
        self.completed_tasks = []

        # Main UI components
        self.task_list = tk.Listbox(root, width=50, height=15, selectmode=tk.SINGLE)
        self.task_list.pack(pady=10)

        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.pack(pady=5)

        # Buttons
        self.add_task_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=5)

        self.complete_task_button = tk.Button(root, text="Mark as Completed", command=self.complete_task)
        self.complete_task_button.pack(pady=5)

        self.update_task_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_task_button.pack(pady=5)

        self.delete_task_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack(pady=5)

        self.view_completed_button = tk.Button(root, text="View Completed Tasks", command=self.view_completed_tasks)
        self.view_completed_button.pack(pady=5)

    def add_task(self):
        task_info = self.task_entry.get()
        if task_info:
            self.tasks.append({"task": task_info, "completed": False})
            self.task_entry.delete(0, tk.END)
            self.refresh_task_list()
        else:
            messagebox.showwarning("Warning", "Please enter a task description.")

    def complete_task(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            task = self.tasks.pop(selected_index[0])
            task["completed"] = True
            self.completed_tasks.append(task)
            self.refresh_task_list()
        else:
            messagebox.showwarning("Warning", "Please select a task to mark as completed.")

    def update_task(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            updated_task = self.task_entry.get()
            if updated_task:
                self.tasks[selected_index[0]]["task"] = updated_task
                self.task_entry.delete(0, tk.END)
                self.refresh_task_list()
            else:
                messagebox.showwarning("Warning", "Please enter an updated task description.")
        else:
            messagebox.showwarning("Warning", "Please select a task to update.")

    def delete_task(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            self.tasks.pop(selected_index[0])
            self.refresh_task_list()
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def view_completed_tasks(self):
        completed_window = tk.Toplevel(self.root)
        completed_window.title("Completed Tasks")
        completed_list = tk.Listbox(completed_window, width=50, height=15)
        completed_list.pack(pady=10)
        for task in self.completed_tasks:
            completed_list.insert(tk.END, task["task"])

    def refresh_task_list(self):
        self.task_list.delete(0, tk.END)
        for task in self.tasks:
            self.task_list.insert(tk.END, task["task"])

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
