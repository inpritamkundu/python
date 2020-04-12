# Creating Grid


import tkinter as tk
root = tk.Tk()

# creating labels entry and button , entry is the text field

usernameLabel = tk.Label(root, text="Username")
passwordLabel = tk.Label(root, text="password")

# Text fields

usernameText = tk.Entry(root)
passwordText = tk.Entry(root)

# Login button

login = tk.Button(root, text="LogIn")

# Arranging

usernameLabel.grid(row=0, column=0)
passwordLabel.grid(row=1, column=0)
usernameText.grid(row=0, column=2)
passwordText.grid(row=1, column=2)
login.grid(row=2, column=1)


root.mainloop()
