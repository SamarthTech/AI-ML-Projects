import tkinter as tk

# Function to handle button click
def on_button_click():
    greeting_label.config(text="Hello, " + entry.get())

# Create the main window
window = tk.Tk()
window.title("Stylish GUI Example")

# Create and configure a label
greeting_label = tk.Label(
    window,
    text="Enter your name:",
    font=("Arial", 16),
    pady=10,
)
greeting_label.pack()

# Create and configure an entry widget
entry = tk.Entry(
    window,
    font=("Arial", 14),
)
entry.pack()

# Create and configure a button
button = tk.Button(
    window,
    text="Submit",
    command=on_button_click,
    font=("Arial", 14),
    bg="#4CAF50",
    fg="white",
    padx=20,
    pady=5,
)
button.pack()

# Configure the window size and position
window.geometry("400x200+100+100")

# Start the GUI event loop
window.mainloop()
