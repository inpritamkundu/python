# creating frames and adding buttons to it


import tkinter as tk
root = tk.Tk()

frameTop = tk.Frame(root)
frameTop.pack()

frameBottom = tk.Frame(root)
frameBottom.pack(side=tk.BOTTOM)

buttonTop = tk.Button(frameTop, text="click here", fg="#ff00ff")
buttonTop.pack()


buttonBottom = tk.Button(frameBottom, text="click here", fg="#ff00ff")
buttonBottom.pack()

root.mainloop()
