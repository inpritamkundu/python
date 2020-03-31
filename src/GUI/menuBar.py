# we will create menu bar and and dropdowns

import tkinter as tk

root = tk.Tk()

# to create menu bar we have a predefined function
menu = tk.Menu(root)
root.config(menu=menu)

# Creating sub menu in the menu bar
file = tk.Menu(menu)
edit = tk.Menu(menu)

# Creating elements to the submenu elements
newFile = tk.Menu(file)


# Adding sub menu main menu
# over here menu means elements that should showup when file is clicked
menu.add_cascade(label="File", menu=file)
menu.add_cascade(label="Edit", menu=edit)


# Adding elements to submenu
# we can use command for sending to methods on clicked
file.add_cascade(label="New file", menu=newFile)
file.add_cascade(label="New window")

# Seperating the elements of submenu
file.add_separator()
file.add_cascade(label="exit")

edit.add_cascade(label="edit")
edit.add_cascade(label="undo")

# adding element to the elements of sebmenu
newFile.add_cascade(label="open")


# Toolbar
toolbar = tk.Frame(root, bg="#ff00ff")

printButton = tk.Button(toolbar, text="print")
printButton.pack(side=tk.LEFT, padx=5, pady=5)

toolbar.pack(side=tk.TOP, fill=tk.X)


#  Status Bar
# status = tk.Frame(root)
statusLabel = tk.Label(root, text="status", bd=5,
                       relief=tk.SUNKEN, anchor=tk.W, padx=10)
statusLabel.pack(side=tk.BOTTOM, fill=tk.X)
# status.pack(side=tk.BOTTOM, fill=tk.X)

root.mainloop()
