# we will create a class and use the functions to create a print button and create a exit button

import tkinter as tk

c = 0


class button:

    def __init__(self, root):
        self.root = root
        self.frameButton = tk.Frame(self.root)
        self.frameButton.pack()
        self.frameLabel = tk.Frame(self.root)
        self.frameLabel.pack()
        self.label = tk.Label(self.frameLabel)
        self.label.pack()

    def printButton(self):
        self.printButton = tk.Button(self.frameButton, text="Print button",
                                     command=self.onclick)
        self.printButton.pack()

    def exitButton(self):
        self.exitButton = tk.Button(
            self.frameButton, text="exit", command=self.frameButton.tk.quit)  # quit is a predefined function for closing window
        self.exitButton.pack()

    def onclick(self):
        global c  # This step will link to global c or else it will work as local c
        c = c+1
        txt = "button clicked " + str(c)
        print(txt)
        self.label['text'] = txt  # to change text at same label


root = tk.Tk()
button = button(root)
button.printButton()
button.exitButton()

root.mainloop()
