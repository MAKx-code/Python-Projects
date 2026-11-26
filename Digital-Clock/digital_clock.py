
import tkinter as tk
import time

# Create the main window
root = tk.Tk()
root.title("MAKx - Digital Clock")
root.geometry("500x300")
root.configure(bg="#10101A")
root.resizable(False, False)

# Application title
title = tk.Label(
    root,
    text="MAKx DIGITAL CLOCK",
    font=("Arial", 16, "bold"),
    fg="#A970FF",
    bg="#10101A"
)
title.pack(pady=20)

# Clock display
clock_label = tk.Label(
    root,
    font=("Arial", 48, "bold"),
    fg="#00FFFF",
    bg="#10101A"
)
clock_label.pack(pady=10)

# Date display
date_label = tk.Label(
    root,
    font=("Arial", 16),
    fg="white",
    bg="#10101A"
)
date_label.pack(pady=10)


# Update the clock every second
def update_clock():
    current_time = time.strftime("%I:%M:%S %p")
    current_date = time.strftime("%A, %d %B %Y")

    clock_label.config(text=current_time)
    date_label.config(text=current_date)

    root.after(1000, update_clock)


# Start the clock
update_clock()

# Run the application
root.mainloop()
