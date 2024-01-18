import tkinter as tk
from tkinter import messagebox

def add_task():
    new_task = entry.get()
    if new_task:
        tasks_listbox.insert(tk.END, new_task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    selected_index = tasks_listbox.curselection()
    if selected_index:
        tasks_listbox.delete(selected_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def mark_complete():
    selected_index = tasks_listbox.curselection()
    if selected_index:
        task = tasks_listbox.get(selected_index)
        tasks_listbox.itemconfig(selected_index, {'bg': 'light green'})
        messagebox.showinfo("Task Complete", f'Task "{task}" marked as complete.')
    else:
        messagebox.showwarning("Warning", "Please select a task to mark as complete.")

def display_tasks():
    tasks = tasks_listbox.get(0, tk.END)
    if tasks:
        task_list = "\n".join(tasks)
        messagebox.showinfo("Tasks", f"Tasks:\n{task_list}")
    else:
        messagebox.showinfo("Tasks", "No tasks available.")

# Create the main window
app = tk.Tk()
app.title("To-Do List Application")

label = tk.Label(app, text="To-Do List Application",bg="red",font=("Algerian",50, "bold"),foreground="black")
label.pack(pady=20)

# Create and pack widgets
label = tk.Label(app, text="Enter Task:",bg="gray",font=("Times New Roman",30, "bold"),foreground="maroon")
label.pack(pady=15)

entry = tk.Entry(app, width=30,font=('Arial', 25, "bold"),bg="pink")
entry.pack(pady=15)

add_button = tk.Button(app, text="Add Task", command=add_task,bg="gray",font=("Times New Roman",20, "bold"),foreground="maroon")
add_button.pack(pady=15)

delete_button = tk.Button(app, text="Delete Task", command=delete_task,bg="gray",font=("Times New Roman",20, "bold"),foreground="maroon")
delete_button.pack(pady=15)

complete_button = tk.Button(app, text="Mark as Complete", command=mark_complete,bg="gray",font=("Times New Roman",20, "bold"),foreground="maroon")
complete_button.pack(pady=15)

display_button = tk.Button(app, text="Display Tasks", command=display_tasks,bg="gray",font=("Times New Roman",20, "bold"),foreground="maroon")
display_button.pack(pady=15)




tasks_listbox = tk.Listbox(app, selectmode=tk.SINGLE, height=20, width=40,font=("Arial",20, "bold"),foreground="black",bg="pink")
tasks_listbox.pack(pady=15)
app.configure(bg='wheat')
app.mainloop()
