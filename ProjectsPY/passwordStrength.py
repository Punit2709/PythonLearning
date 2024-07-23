import tkinter as tk

# Create a new Tkinter window
window = tk.Tk()

# Set the title of the window
window.title("My Tkinter Application")

# Set the size of the window
window.geometry("300x200")

# Add a label to the window
label = tk.Label(window, text="Hello, Tkinter!")
label.pack()

# Run the Tkinter event loop
window.mainloop()
