import tkinter as tk
import tkinter.font as font
import psycopg2
import tkinter.messagebox
from tkinter import ttk


s = 0   # for counting number of times search button is placed
frameData = 0  # for creating global frame


root = tk.Tk()
root.geometry('1000x700')
root.title("Teckat")

height = root.winfo_screenheight()
container = ttk.Frame(root)
canvas = tk.Canvas(container, height=height-100)
scrollbar = ttk.Scrollbar(container, command=canvas.yview)
frame = ttk.Frame(canvas)

frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=frame)

canvas.configure(yscrollcommand=scrollbar.set)


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
# ================ add data ==================================================
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

      # ================== delete data ==============================================


def DeleteQuery():
    DeleteId = entryDeleteId.get()

    if (DeleteId):
        cursor = connection.cursor()
        query = "DELETE FROM student where id ="+DeleteId+";"
        print(query)
        cursor.execute(query)
        connection.commit()
        tk.messagebox.showinfo(
            "Teckat", "Your data deleted successfully.")
        # Takes (starting position, ending position)
        entryDeleteId.delete(0, tk.END)
        entryDeleteId.focus()

    else:
        tk.messagebox.showinfo(
            "Teckat", "Enter valid data.")

    # ================================= search data ======================================================


# Will search when submit entry is clicked

def searchQuery():
    searchId = entrySearchId.get()
    name = entrySearchName.get()
    address = entrySearchAddress.get()
    age = entrySearchAge.get()
    global s
    s += 1
    if ((searchId and name == '' and address == '' and age == '') or (searchId == '' and name and address == '' and age == '') or (searchId == '' and name == '' and address and age == '') or (searchId == '' and name == '' and address == '' and age)):
        if(searchId):
          # If search id present

            cursor = connection.cursor()
            query = "SELECT id ,name, address, age FROM student where id ="+searchId+";"
            print(query)
            cursor.execute(query)
            row = cursor.fetchall()  # fetches all at a time use fetchone for fetching one at a time
            print(row)

            # if row contains value
            if (row):
                global frameData
                if s == 1:
                    createFrame()
                    printDataOnWindow(row)
                else:
                    destroyFrame()
                    createFrame()
                    printDataOnWindow(row)
            else:
                tk.messagebox.showinfo(
                    "Teckat", "No data found.")

        elif(name):
            cursor = connection.cursor()
            query = "SELECT id ,name, address, age FROM student where name = '"+name+"';"
            # print(query)
            cursor.execute(query)
            row = cursor.fetchall()     # fetches all at a time
            print(row)

            if (row):
                global frameData
                if s == 1:
                    createFrame()
                    printDataOnWindow(row)
                else:
                    destroyFrame()
                    createFrame()
                    printDataOnWindow(row)
            else:
                tk.messagebox.showinfo(
                    "Teckat", "No data found.")

        elif(address):
            cursor = connection.cursor()
            query = "SELECT id ,name, address, age FROM student where address = '"+address+"';"
            # print(query)
            cursor.execute(query)
            row = cursor.fetchall()      # fetches all at a time

            if (row):
                if s == 1:
                    createFrame()
                    printDataOnWindow(row)
                else:
                    destroyFrame()
                    createFrame()
                    printDataOnWindow(row)
            else:
                tk.messagebox.showinfo(
                    "Teckat", "No data found.")

        elif(age):
            cursor = connection.cursor()
            query = "SELECT id ,name, address, age FROM student where age = '"+age+"';"
            # print(query)
            cursor.execute(query)
            row = cursor.fetchall()      # fetches all at a time
            print(row)

            if (row):
                if s == 1:
                    createFrame()
                    printDataOnWindow(row)
                else:
                    destroyFrame()
                    createFrame()
                    printDataOnWindow(row)
            else:
                tk.messagebox.showinfo(
                    "Teckat", "No data found.")

        # Takes (starting position, ending position)
        entrySearchId.delete(0, tk.END)
        entrySearchName.delete(0, tk.END)
        entrySearchAddress.delete(0, tk.END)
        entrySearchAge.delete(0, tk.END)
        entrySearchId.focus()

    else:
        cursor = connection.cursor()
        query = "SELECT id ,name, address, age FROM student;"
        # print(query)
        cursor.execute(query)
        row = cursor.fetchall()      # fetches all at a time
        print(row)
        if (row):
            createFrame()
            printDataOnWindow(row)
        else:
            tk.messagebox.showinfo(
                "Teckat", "No data found.")


# To create log generating frame


def createFrame():
    global frameData
    frameData = tk.Frame(frame)
    frameData.place(relx=0.01, rely=.68, relwidth=0.8, relheight=0.8)

# to destroy log generating frame


def destroyFrame():
    global frameData
    frameData.after(0, frameData.destroy)


# To print log on log generating frame

def printDataOnWindow(row):
    r = 14  # row
    c = 0  # column
    global frameData
    # create a frame for entry of data

    label = tk.Label(frameData, text="id", font=fontsizeData)
    label.grid(row=r, column=c, padx=(50, 0))

    label = tk.Label(frameData, text="Name", font=fontsizeData)
    label.grid(row=r, column=c+1, padx=(50, 0))

    label = tk.Label(frameData, text="Address", font=fontsizeData)
    label.grid(row=r, column=c+2, padx=(50, 0))

    label = tk.Label(frameData, text="Age", font=fontsizeData)
    label.grid(row=r, column=c+3, padx=(50, 0))

    for i in row:
        # print(i)
        r += 1
        c = 0
        for j in i:
            label = tk.Label(frameData, text=j, font=fontsizeData)
            label.grid(row=r, column=c, padx=(50, 0))
            c += 1

    # ======================================================   GUI   =============================================================


# Adding main label
addDataLabel = tk.Label(frame, text="Add Data",
                        font=fontSizeHeading)
addDataLabel.grid(row=0, column=1, pady=(height/5, 10))

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


# ================================================== Delete Data ==================================================================


# Adding main label
DeleteDataLabel = tk.Label(frame, text="Delete Data",
                           font=fontSizeHeading)
DeleteDataLabel.grid(row=5, column=1, pady=(height/3, 10))

# Adding data label
entryDeleteIdLabel = tk.Label(frame, text="Delete by ID : ", font=fontsizeData)
entryDeleteIdLabel.grid(row=6, column=0, pady=2)


# Adding entry form for data label
entryDeleteId = tk.Entry(frame, width=50, font=fontsizeData)
entryDeleteId.grid(row=6, column=1, pady=10, ipady=7)

# Create button for entry
entryDeleteButton = tk.Button(frame, text="Delete",
                              width=15, font=fontsizeData, command=DeleteQuery)
entryDeleteButton.grid(row=7, column=1, ipady=5, pady=5)

# ================================================== search data ======================================================

# Adding main label
searchDataLabel = tk.Label(frame, text="Search Data",
                           font=fontSizeHeading)
searchDataLabel.grid(row=8, column=1, pady=(height/3, 10))

# Adding data label
entrySearchIdLabel = tk.Label(frame, text="Search by ID : ", font=fontsizeData)
entrySearchIdLabel.grid(row=9, column=0, pady=2)

entrySearchNameLabel = tk.Label(
    frame, text="Search by Name : ", font=fontsizeData)
entrySearchNameLabel.grid(row=10, column=0, pady=2)

entrySearchAddressLabel = tk.Label(
    frame, text="Search by Address : ", font=fontsizeData)
entrySearchAddressLabel.grid(row=11, column=0, pady=2)

entrySearchAgeLabel = tk.Label(
    frame, text="Search by Age : ", font=fontsizeData)
entrySearchAgeLabel.grid(row=12, column=0, pady=2)


# Adding entry form for data label
entrySearchId = tk.Entry(frame, width=50, font=fontsizeData)
entrySearchId.grid(row=9, column=1, pady=10, ipady=7)

entrySearchName = tk.Entry(frame, width=50, font=fontsizeData)
entrySearchName.grid(row=10, column=1, pady=10, ipady=7)

entrySearchAddress = tk.Entry(frame, width=50, font=fontsizeData)
entrySearchAddress.grid(row=11, column=1, pady=10, ipady=7)

entrySearchAge = tk.Entry(frame, width=50, font=fontsizeData)
entrySearchAge.grid(row=12, column=1, pady=10, ipady=7)


# Create button for search
entrySearchButton = tk.Button(frame, text="Search",
                              width=15, font=fontsizeData, command=searchQuery)
entrySearchButton.grid(row=13, column=1, ipady=5, pady=(5, height))


container.pack(fill=tk.BOTH)
canvas.pack(side="left", fill=tk.BOTH, expand=True, padx=20, pady=20)
scrollbar.pack(side="right", fill="y")
root.mainloop()
