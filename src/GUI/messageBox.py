# open a pop up message and also store response of user

import tkinter as tk
# To import message box

import tkinter.messagebox
root = tk.Tk()

# Pre-defined message box in tkinter

# For printing a message

# The first column becomes the title and the second column becomes the content
tk.messagebox.showinfo("Title", "welcome to Teckat")

# To ask questions

response = tk.messagebox.askquestion(
    "question 1", "Do you like this course offered by Teckat")

if(response == "yes"):
    tk.messagebox.showinfo("Teckat", "Thank you for your support.")
else:
    tk.messagebox.showinfo(
        "Teckat", "We will take your feedback as a positive response and try to improve our service better, Thank you.")

root.mainloop()
