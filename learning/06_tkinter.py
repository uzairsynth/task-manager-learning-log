import tkinter as tk


def add_task():
    task_name = task_entry.get()

    if task_name != "":
        task_list.insert(tk.END, task_name)
        task_entry.delete(0, tk.END)


def complete_task():
    selected = task_list.curselection()

    if selected:
        index = selected[0]
        task_name = task_list.get(index)

        task_list.delete(index)
        task_list.insert(index, "✓ " + task_name)


root = tk.Tk()

root.title("Personal Task Manager")
root.geometry("600x400")


task_label = tk.Label(
    root,
    text="Task:"
)

task_label.pack(pady=10)


task_entry = tk.Entry(
    root,
    width=40
)

task_entry.pack(pady=5)


add_button = tk.Button(
    root,
    text="Add Task",
    command=add_task
)

add_button.pack(pady=10)


complete_button = tk.Button(
    root,
    text="Complete Task",
    command=complete_task
)

complete_button.pack(pady=5)


task_list = tk.Listbox(
    root,
    width=50,
    height=10
)

task_list.pack(pady=20)


root.mainloop()