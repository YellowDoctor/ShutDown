import tkinter as tk
from tkinter import messagebox
import os

def shutdown():
    # Get the selected time for shutdown
    hours = int(hours_var.get())
    minutes = int(minutes_var.get())

    # Calculate the time in seconds
    total_seconds = hours * 3600 + minutes * 60

    # Send the shutdown command
    os.system(f'shutdown -s -t {total_seconds}')

def change_theme(theme):
    if theme == "light":
        root.config(bg="white")
        label.config(bg="white", fg="black")
        hours_label.config(bg="white", fg="black")
        minutes_label.config(bg="white", fg="black")
        shutdown_button.config(bg="lightgray", fg="black")
    elif theme == "dark":
        root.config(bg="gray25")
        label.config(bg="gray25", fg="white")
        hours_label.config(bg="gray25", fg="white")
        minutes_label.config(bg="gray25", fg="white")
        shutdown_button.config(bg="gray50", fg="white")

# Create the main application window
root = tk.Tk()
root.title("Shutdown PC")
root.config(bg="white")  # Default light theme

# Set window size and center content
window_width = 300
window_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Add a label with a description
label = tk.Label(root, text="Select the time to shutdown:")
label.place(relx=0.5, rely=0.2, anchor="center")

# Create variables for hours and minutes
hours_var = tk.StringVar(root)
minutes_var = tk.StringVar(root)

# Create a dropdown menu for selecting hours
hours_label = tk.Label(root, text="Hours:")
hours_label.place(relx=0.3, rely=0.4, anchor="center")
hours_menu = tk.OptionMenu(root, hours_var, *range(24))
hours_menu.place(relx=0.7, rely=0.4, anchor="center")

# Create a dropdown menu for selecting minutes
minutes_label = tk.Label(root, text="Minutes:")
minutes_label.place(relx=0.3, rely=0.6, anchor="center")
minutes_menu = tk.OptionMenu(root, minutes_var, *range(60))
minutes_menu.place(relx=0.7, rely=0.6, anchor="center")

# Create a button to initiate shutdown
shutdown_button = tk.Button(root, text="Shutdown", command=shutdown)
shutdown_button.place(relx=0.5, rely=0.8, anchor="center")

# Create a menu for selecting theme
theme_menu = tk.Menu(root)
root.config(menu=theme_menu)

theme_submenu = tk.Menu(theme_menu, tearoff=False)
theme_menu.add_cascade(label="Theme", menu=theme_submenu)
theme_submenu.add_command(label="Light", command=lambda: change_theme("light"))
theme_submenu.add_command(label="Dark", command=lambda: change_theme("dark"))

# Run the main application loop
root.mainloop()
