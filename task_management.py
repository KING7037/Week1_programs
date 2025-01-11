import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root=tk.Tk()
root.title("Task Management System")

tk.Label(root,text="Task").grid(row=1,column=0,columnspan=4)
tk.Label(root,text="Date").grid(row=1,column=8,columnspan=4)


task_entry = tk.Entry(root,width=16)
due_date_entry = tk.Entry(root,width=16)

task_entry.grid(row=1,column=4,columnspan=4)
due_date_entry.grid(row=1,column=12,columnspan=4)

 # Create a Treeview widget to display contact details
tree = ttk.Treeview(root, columns=("Task", "Due Date", "Status", "Action"), show='headings')
tree.heading("Task", text="Task")
tree.column("Task", anchor=tk.CENTER)
tree.heading("Due Date", text="Due Date")
tree.column("Due Date", anchor=tk.CENTER)
tree.heading("Status", text="Status")
tree.column("Status", anchor=tk.CENTER)
tree.heading("Action", text="Action")
tree.column("Action", anchor=tk.CENTER, width=100)

# Position the Treeview
tree.grid(row=3, column=0, columnspan=20)

# Set default button action to "Save"
button_action = "Save"

def set_save_button_action():
    global button_action
    button_action = "Save"
    
    # Edit task action
def edit_action(item_id):
    if messagebox.askyesno("Edit Task", "Are you sure you want to edit this task?"):
        item = tree.item(item_id)
        task_tree = item['values'][0]
        due_date_tree = item['values'][1]

        # Clear and populate entry fields with selected task data
        task_entry.delete(0, tk.END)
        due_date_entry.delete(0, tk.END)

        task_entry.insert(tk.END, task_tree)
        due_date_entry.insert(tk.END, due_date_tree)
        
        set_edit_button_action()
        
def delete_action(item_id):
    if messagebox.askyesno("Delete  Data", "Are you sure to delete the task? "):
        tree.delete(item_id)

def on_row_click(event):
    global item_id
    item_id=tree.identify_row(event.y)
    col=tree.identify_column(event.x)
    print(event)

    if col == "#3":
        action=""
        if(event.x < 442):
            edit_action(item_id)
        else:
            delete_action(item_id)
        print(action)

tree.bind("<Button-1>", on_row_click)

data=[]
def save_data():
    print(button_action)
    task = task_entry.get()
    due_date = due_date_entry.get()
    is_update = button_action == "Edit"



   
    if is_update:
        # Update selected task
        tree.item(item_id, values=(task, due_date, "Pending", "Edit | Delete"))
        messagebox.showinfo("Update", "Task updated successfully")
    else:
        # Add new task if it's a save action
        tree.insert("", tk.END, values=(task, due_date, "Pending", "Edit | Delete"))
        messagebox.showinfo("Save", "Task added successfully")

    set_save_button_action()
    task_entry.delete(0, tk.END)
    due_date_entry.delete(0, tk.END)

# Button to save or update task data
tk.Button(root, text="Save / Update", command=save_data).grid(row=1, column=16)

# Run the main application loop
root.mainloop()