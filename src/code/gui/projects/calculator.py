import tkinter as tk
import parser    # Used for conversion of string to expressions
root = tk.Tk()
root.title("calculator")

i = 0

# ===============================================================================================================


# Step 2
# Creating functionality for inserting button values to entry form


def insertValueToEntryForm(num):
    global i
    display.insert(i, num)   # Takes (index position, value)
    i += 1


# Creating functionality for clear
def clear():
    display.delete(0, tk.END)   # Takes (starting position, ending position)


# Creating functionality for undo function
# def undo():
#     string = display.get()    # To get the elements of entry form
#     # print(string)
#     if(string):
#         string = string[:-1]
#         # print(string)
#         clear()
#         display.insert(0, string)
#     else:
#         clear()


# Calculating the values
def calculate():
    string = display.get()
    try:
        # expr is to convert string in expression and eval to calculate
        result = eval(parser.expr(string).compile())
        # print(result)
        clear()
        display.insert(0, result)
    except Exception:
        clear()
        display.insert(0, "Error")


# =========================================================================================================================
# Step 1
# Creating entry form
display = tk.Entry(root)
display.grid(row=0, columnspan=28, sticky=tk.W+tk.E, padx=3, pady=3)

# Creating buttons
tk.Button(root, text="1", width=5,
          command=lambda: insertValueToEntryForm(1)).grid(row=1, column=0,)     # Used lambda because we need to send data to the function
tk.Button(root, text="2", width=5,
          command=lambda: insertValueToEntryForm(2)).grid(row=1, column=1,)
tk.Button(root, text="3", width=5,
          command=lambda: insertValueToEntryForm(3)).grid(row=1, column=2,)

tk.Button(root, text="4", width=5,
          command=lambda: insertValueToEntryForm(4)).grid(row=2, column=0,)
tk.Button(root, text="5", width=5,
          command=lambda: insertValueToEntryForm(5)).grid(row=2, column=1,)
tk.Button(root, text="6", width=5,
          command=lambda: insertValueToEntryForm(6)).grid(row=2, column=2,)

tk.Button(root, text="7", width=5,
          command=lambda: insertValueToEntryForm(7)).grid(row=3, column=0,)
tk.Button(root, text="8", width=5,
          command=lambda: insertValueToEntryForm(8)).grid(row=3, column=1,)
tk.Button(root, text="9", width=5,
          command=lambda: insertValueToEntryForm(9)).grid(row=3, column=2,)

# Adding other elements
tk.Button(root, text="AC", width=5, command=clear).grid(row=4, column=0,)
tk.Button(root, text="0", width=5,
          command=lambda: insertValueToEntryForm(0)).grid(row=4, column=1,)
tk.Button(root, text="=", width=5, command=calculate).grid(row=4, column=2,)

# Adding operators
tk.Button(root, text="+", width=5,
          command=lambda: insertValueToEntryForm('+')).grid(row=1, column=3,)
tk.Button(root, text="-", width=5,
          command=lambda: insertValueToEntryForm('-')).grid(row=2, column=3,)
tk.Button(root, text="*", width=5,
          command=lambda: insertValueToEntryForm('*')).grid(row=3, column=3,)
tk.Button(root, text="/", width=5,
          command=lambda: insertValueToEntryForm('/')).grid(row=4, column=3,)


root.mainloop()
