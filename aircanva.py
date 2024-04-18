import tkinter as tk
from tkinter import ttk, messagebox, colorchooser
from collections import deque
from PIL import Image, ImageDraw


class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Canvas Application")
        self.root.geometry("800x600")

        # Default values for color thresholds
        self.upper_hsv_default = (153, 255, 255)
        self.lower_hsv_default = (64, 72, 49)
        self.upper_hsv = self.upper_hsv_default
        self.lower_hsv = self.lower_hsv_default

        self.brush_size = tk.IntVar()
        self.brush_size.set(5)
        self.color_selected = tk.StringVar()
        self.color_selected.set("black")

        # Create canvas for drawing
        self.canvas = tk.Canvas(self.root, bg="white")
        self.canvas.pack(expand=True, fill="both")

        # Create toolbar frame
        self.toolbar_frame = ttk.Frame(self.root)
        self.toolbar_frame.pack(side="top", fill="x")

        # Create buttons
        self.clear_button = ttk.Button(
            self.toolbar_frame, text="Clear", command=self.clear_canvas)
        self.clear_button.grid(row=0, column=0, padx=10, pady=5)

        self.save_button = ttk.Button(
            self.toolbar_frame, text="Save", command=self.save_canvas)
        self.save_button.grid(row=0, column=1, padx=10, pady=5)

        self.brush_size_label = ttk.Label(
            self.toolbar_frame, text="Brush Size:")
        self.brush_size_label.grid(row=0, column=2, padx=10, pady=5)

        self.brush_size_scale = ttk.Scale(
            self.toolbar_frame, from_=1, to=20, variable=self.brush_size, orient="horizontal")
        self.brush_size_scale.grid(row=0, column=3, padx=5, pady=5)

        self.color_palette = ttk.Button(
            self.toolbar_frame, text="Color Palette", command=self.choose_color)
        self.color_palette.grid(row=0, column=4, padx=10, pady=5)

        # Bind mouse events to draw on canvas
        self.canvas.bind("<B1-Motion>", self.draw)

    def draw(self, event):
        x, y = event.x, event.y
        size = self.brush_size.get()
        color = self.color_selected.get()
        self.canvas.create_oval(x, y, x+size, y+size,
                                fill=color, outline=color)

    def clear_canvas(self):
        self.canvas.delete("all")

    def save_canvas(self):
        filename = tk.filedialog.asksaveasfilename(defaultextension=".png", filetypes=[
                                                   ("PNG files", "*.png"), ("All files", "*.*")])
        if filename:
            self.canvas.postscript(file=filename + ".eps")
            img = Image.open(filename + ".eps")
            img.save(filename)

    def choose_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.color_selected.set(color)


if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()
