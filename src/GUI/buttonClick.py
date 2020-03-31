
# Creating a platform , when button is clicked it will count the value and replace the previous text in the label and print it


import tkinter as tk

c = 0
root = tk.Tk()

label = tk.Label(root)


def onclick():
    global c  # This step will link to global c or else it will work as local c
    c = c+1
    txt = "button clicked " + str(c)
    print(txt)
    label['text'] = txt  # to change text at same label


# command executes when the button is clicked
button = tk.Button(root, text="click here", command=onclick)

# button.pack(side=tk.LEFT)
# label.pack(side=tk.LEFT)

button.grid(row=0, column=0)
label.grid(row=0, column=1)


root.mainloop()
