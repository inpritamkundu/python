import tkinter as tk
root = tk.Tk()


def mainFunction():
    print(var1.get())


generatedataButton = tk.Button(root, text="Generate Data",
                               width=15, command=mainFunction)
generatedataButton.grid(row=1, column=0, pady=20)

root.mainloop()
