import tkinter as tk

root = tk.Tk()
root.title("Tk dropdown example")
root.geometry('500x500')

# Create a Tkinter variable
tkvar = tk.StringVar(root)

# Dictionary with options
choices = {'Pizza', 'Lasagne', 'Fries', 'Fish', 'Potatoe'}
tkvar.set('Pizza')  # set the default option

popupMenu = tk.OptionMenu(root, tkvar, *choices)
tk.Label(root, text="Choose a dish").grid(row=1, column=1)
popupMenu.grid(row=2, column=1)

# on change dropdown value


# def change_dropdown(*args):
#     print(type(tkvar.get()))


# # link function to change dropdown
# tkvar.trace('w', change_dropdown)

root.mainloop()
