import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")

        self.tasks = []

        self.task_entry = tk.Entry(master, width=40)
        self.task_entry.grid(row=0, column=0, padx=5, pady=5)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=5)

        self.task_listbox = tk.Listbox(master, width=50)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.remove_button = tk.Button(master, text="Remove Task", command=self.remove_task)
        self.remove_button.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        self.update_button = tk.Button(master, text="Update Task", command=self.update_task)
        self.update_button.grid(row=2, column=1, padx=5, pady=5, sticky="e")

        self.complete_button = tk.Button(master, text="Complete Task", command=self.complete_task)
        self.complete_button.grid(row=3, column=0, padx=5, pady=5, sticky="w")

        self.clear_button = tk.Button(master, text="Clear All", command=self.clear_all)
        self.clear_button.grid(row=3, column=1, padx=5, pady=5, sticky="e")

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text:
            self.tasks.append(task_text)
            self.update_task_display()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            del self.tasks[index]
            self.update_task_display()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to remove.")

    def update_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            updated_task_text = self.task_entry.get().strip()
            if updated_task_text:
                self.tasks[index] = updated_task_text
                self.update_task_display()
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "Please enter an updated task.")
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to update.")

    def complete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            task = self.tasks[index]
            if not task.startswith("✓"):
                self.tasks[index] = task + ' ✓'
                self.update_task_display()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to mark as completed.")

    def update_task_display(self):
        self.task_listbox.delete(0, tk.END)
        for i, task in enumerate(self.tasks, start=1):
            self.task_listbox.insert(tk.END, f"{i}. {task}")

    def clear_all(self):
        self.task_listbox.delete(0, tk.END)
        self.tasks.clear()


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
