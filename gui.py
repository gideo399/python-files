from tkinter import *
from PIL import Image, ImageTk  # Import the necessary libraries

window = Tk()
window.title("This is my first GUI")

# Correct the file path
icon_path = r"C:/Users/lenovo/Pictures/snake.jpg"  # Use raw string

# Load the image using Pillow
image = Image.open(icon_path)
icon = ImageTk.PhotoImage(image)

# Keep a reference to avoid garbage collection
window.iconphoto(True, icon)

window.mainloop()