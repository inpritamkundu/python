import tkinter as tk
import tkinter.font as font
import psycopg2
import tkinter.messagebox


root = tk.Tk()
root.geometry('1000x700')
root.title("Teckat")

# creating connection to database
connection = psycopg2.connect(dbname="postgres", user="postgres",
                              password="mithukundu60@", host="localhost", port="5432")
print("connection established")

# Changing font style
fontSizeHeading = font.Font(size=20)
fontsizeData = font.Font(size=15)

# #To change font configuration
# fontStyle.configure(size=fontStyle['size']+20)
# print(fontStyle['size'])


# ====================================================  function  ============================================================

# Will submit query when submit entry is clicked

def addQuery():
    name = entryAddName.get()
    address = entryAddAddress.get()
    age = entryAddAge.get()
    if (name and address and age):
        cursor = connection.cursor()
        query = ''' INSERT INTO student(NAME,ADDRESS,AGE) VALUES(%s,%s,%s);'''
        cursor.execute(query, (name, address, age))
        connection.commit()
        tk.messagebox.showinfo(
            "Teckat", "Your data inserted successfully. Enter new data.")

        # Takes (starting position, ending position)
        entryAddName.delete(0, tk.END)
        entryAddAddress.delete(0, tk.END)
        entryAddAge.delete(0, tk.END)
        entryAddName.focus()
    else:
        tk.messagebox.showinfo(
            "Teckat", "Enter valid data.")


    # ======================================================   GUI   =============================================================
    # Adding frame
frame = tk.Frame(root)
frame.place(relx=0.2, rely=0.1, relwidth=0.8, relheight=0.8)

# Adding main label
addDataLabel = tk.Label(frame, text="Add Data",
                        font=fontSizeHeading)
addDataLabel.grid(row=0, column=1)

# Adding data label
entryAddNameLabel = tk.Label(frame, text="Name : ", font=fontsizeData)
entryAddNameLabel.grid(row=1, column=0, pady=2)

entryAddAddressLabel = tk.Label(frame, text="Address : ", font=fontsizeData)
entryAddAddressLabel.grid(row=2, column=0, pady=2)

entryAddAgeLabel = tk.Label(frame, text="Age : ", font=fontsizeData)
entryAddAgeLabel.grid(row=3, column=0, pady=2)


# Adding entry form for data label
entryAddName = tk.Entry(frame, width=50, font=fontsizeData)
entryAddName.grid(row=1, column=1, pady=10, ipady=7)
entryAddName.focus()

entryAddAddress = tk.Entry(frame, width=50, font=fontsizeData)
entryAddAddress.grid(row=2, column=1, pady=10, ipady=7)

entryAddAge = tk.Entry(frame, width=50, font=fontsizeData)
entryAddAge.grid(row=3, column=1, pady=10, ipady=7)


# Create button for entry
entryAddButton = tk.Button(frame, text="Submit Entry",
                           width=15, font=fontsizeData, command=addQuery)
entryAddButton.grid(row=4, column=1, ipady=5, pady=5)


root.mainloop()
