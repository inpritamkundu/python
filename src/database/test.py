# making label in gui

import tkinter as tk
root = tk.Tk()
frame = 0
frame = tk.Frame(root)
frame.pack()

for i in range(10):
    w = tk.Label(frame, text="Hello World")
    w.grid(row=i, column=0)

# deleting frame
frame.after(0, frame.destroy)
frame = tk.Frame(root)
frame.pack()

for i in range(10):
    w = tk.Label(frame, text="Hello World")
    w.grid(row=i, column=0)

# frame.destroy
root.mainloop()
