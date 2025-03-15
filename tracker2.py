import tkinter as tk

#tasks to complete and servers at 30C
tasks_needed_to_be_completed = [f"task{i}" for i in range(1, 101)]
C = 1  # Temperature increment per task
servers = servers = [
    ["serv1", 30 * C, []], 
    ["serv2", 30 * C, []], 
    ["serv3", 30 * C, []], 
    ["serv4", 30 * C, []]
]
MAX_TEMP = 49 * C
TTime = 30000  #30 seconds

# Function to distribute tasks across servers
def complete_task(task):
    for server in servers:
        if server[1] <= MAX_TEMP:
            server[2].append(task)
            server[1] += C  # Increase temperature
            schedule_task_removal(server, task)  # Call the function to remove task after 30 sec
            break
    display_tasks()  # Update task display after adding a task

# Function to schedule task removal after TTime (30 seconds)
def schedule_task_removal(server, task):
    main_win.after(TTime, remove_task, server, task)

# Function to remove task from server after 30 seconds
def remove_task(server, task):
    server[2].remove(task)
    server[1] -= C  # Decrease temperature
    display_tasks()  # Update task display after removing a task

# Function to distribute tasks automatically
def distribute_tasks():
    if tasks_needed_to_be_completed:
        complete_task(tasks_needed_to_be_completed.pop(0))  # Pop a task from the list and distribute it
        main_win.after(1000, distribute_tasks)  # Distribute next task after 1 second

# Function to update the display of server data in the GUI
def display_tasks():
    # Clear existing labels and text widgets by destroying old ones
    for widget in main_win.winfo_children():
        widget.destroy()

    # Display updated server data
    for server in servers:
        tk.Label(main_win, text=f"{server[0]} - Temperature: {server[1]}°C", font=("Arial", 12)).pack(anchor='w', pady=5)

        task_display = tk.Text(main_win, width=50, height=5, wrap=tk.WORD, font=("Arial", 10))
        task_display.pack(padx=10, pady=5)
        task_display.insert(tk.END, "\n".join([f"  - {task}" for task in server[2]]) or "  No tasks assigned.\n")

# Set up the main window
main_win = tk.Tk()
main_win.title("Server Task Distribution")
main_win.geometry("600x700")

# Title Label
tk.Label(main_win, text="Automated Task Distribution Across Servers", font=("Arial", 14)).pack(pady=10)

# Start automatic distribution of tasks
main_win.after(1000, distribute_tasks)

# Run the application
main_win.mainloop()
