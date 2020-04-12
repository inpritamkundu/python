# Draw rectangles and squares on a canvas

import tkinter as tk

root = tk.Tk()

# Creating canvas
canvas = tk.Canvas(root, height=300, width=500)
canvas.pack()

# Drawing line on canvas
# Coordinates of points (x1,y1,x2,y2)
canvas.create_line(100, 100, 200, 200)
canvas.create_line(250, 250, 300, 300)


root.mainloop()
