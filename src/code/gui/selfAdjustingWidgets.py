# adjusting the widgets at x and y axis


import tkinter as tk
root = tk.Tk()

labelx = tk.Label(root, text="Hello World", bg="Red")
labelx.pack(fill=tk.X)

labely = tk.Label(root, text="Hello World", bg="Green")
labely.pack(side=tk.LEFT, fill=tk.Y)

root.mainloop()
