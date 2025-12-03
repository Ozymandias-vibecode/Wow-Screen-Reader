import tkinter as tk

# Create root window
root = tk.Tk()

# Remove window decorations (borderless)
root.overrideredirect(True)

# Make window always on top
root.attributes("-topmost", True)

# Make background transparent
root.attributes("-transparentcolor", "white")

# Set semi-transparency (0.0 = invisible, 1.0 = solid)
root.attributes("-alpha", 0.6)

# Set window size and position (circle will be 100x100)
root.geometry("100x100+500+300")  # width x height + x + y

# Create canvas
canvas = tk.Canvas(root, width=100, height=100, bg="white", highlightthickness=0)
canvas.pack()

# Draw a circle (oval)
canvas.create_oval(10, 10, 90, 90, fill="red", outline="")

root.mainloop()
