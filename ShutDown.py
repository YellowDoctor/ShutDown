import tkinter as tk
import os

def shutdown():
    # Get the selected time for shutdown
    hours = int(hours_var.get())
    minutes = int(minutes_var.get())

    # Calculate the time in seconds
    total_seconds = hours * 3600 + minutes * 60

    # Send the shutdown command
    os.system(f'shutdown -s -t {total_seconds}')

# Create the main application window
root = tk.Tk()
root.title("Shutdown PC")

# Add a label with a description
label = tk.Label(root, text="Select the time to shutdown:")
label.pack()

# Create variables for hours and minutes
hours_var = tk.StringVar(root)
minutes_var = tk.StringVar(root)

# Create a dropdown menu for selecting hours
hours_label = tk.Label(root, text="Hours:")
hours_label.pack()
hours_menu = tk.OptionMenu(root, hours_var, *range(24))
hours_menu.pack()

# Create a dropdown menu for selecting minutes
minutes_label = tk.Label(root, text="Minutes:")
minutes_label.pack()
minutes_menu = tk.OptionMenu(root, minutes_var, *range(60))
minutes_menu.pack()

# Create a button to initiate shutdown
shutdown_button = tk.Button(root, text="Shutdown", command=shutdown)
shutdown_button.pack()

# Run the main application loop
root.mainloop()
