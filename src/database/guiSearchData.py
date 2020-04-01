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

# Will search when submit entry is clicked

def searchQuery():
    searchId = entrySearchId.get()
    name = entrySearchName.get()
    address = entrySearchAddress.get()
    age = entrySearchAge.get()

    if ((searchId and name == '' and address == '' and age == '') or (searchId == '' and name and address == '' and age == '') or (searchId == '' and name == '' and address and age == '') or (searchId == '' and name == '' and address == '' and age)):
        if(searchId):
            cursor = connection.cursor()
            query = "SELECT id ,name, address, age FROM student where id ="+searchId+";"
            print(query)
            cursor.execute(query)
            row = cursor.fetchone()  # fetches one at a time
            print(row)
            connection.commit()
        elif(name):
            cursor = connection.cursor()
            query = "SELECT id ,name, address, age FROM student where name = '"+name+"';"
            # print(query)
            cursor.execute(query)
            row = cursor.fetchall()     # fetches all at a time
            print(row)
            connection.commit()
        elif(address):
            cursor = connection.cursor()
            query = "SELECT id ,name, address, age FROM student where address = '"+address+"';"
            # print(query)
            cursor.execute(query)
            row = cursor.fetchall()      # fetches all at a time
            print(row)
            connection.commit()
        elif(age):
            cursor = connection.cursor()
            query = "SELECT id ,name, address, age FROM student where age = '"+age+"';"
            # print(query)
            cursor.execute(query)
            row = cursor.fetchall()      # fetches all at a time
            print(row)
            connection.commit()

        # Takes (starting position, ending position)
        entrySearchId.delete(0, tk.END)
        entrySearchName.delete(0, tk.END)
        entrySearchAddress.delete(0, tk.END)
        entrySearchAge.delete(0, tk.END)
        entrySearchId.focus()

    else:
        tk.messagebox.showinfo(
            "Teckat", "Enter valid data.")

    # ======================================================   GUI   =============================================================
    # Adding frame
frame = tk.Frame(root)
frame.place(relx=0.2, rely=0.1, relwidth=0.8, relheight=0.8)

# Adding main label
searchDataLabel = tk.Label(frame, text="Search Data",
                           font=fontSizeHeading)
searchDataLabel.grid(row=0, column=1)

# Adding data label
entrySearchIdLabel = tk.Label(frame, text="Search by ID : ", font=fontsizeData)
entrySearchIdLabel.grid(row=1, column=0, pady=2)

entrySearchNameLabel = tk.Label(
    frame, text="Search by Name : ", font=fontsizeData)
entrySearchNameLabel.grid(row=2, column=0, pady=2)

entrySearchAddressLabel = tk.Label(
    frame, text="Search by Address : ", font=fontsizeData)
entrySearchAddressLabel.grid(row=3, column=0, pady=2)

entrySearchAgeLabel = tk.Label(
    frame, text="Search by Age : ", font=fontsizeData)
entrySearchAgeLabel.grid(row=4, column=0, pady=2)


# Adding entry form for data label
entrySearchId = tk.Entry(frame, width=50, font=fontsizeData)
entrySearchId.grid(row=1, column=1, pady=10, ipady=7)
entrySearchId.focus()

entrySearchName = tk.Entry(frame, width=50, font=fontsizeData)
entrySearchName.grid(row=2, column=1, pady=10, ipady=7)

entrySearchAddress = tk.Entry(frame, width=50, font=fontsizeData)
entrySearchAddress.grid(row=3, column=1, pady=10, ipady=7)

entrySearchAge = tk.Entry(frame, width=50, font=fontsizeData)
entrySearchAge.grid(row=4, column=1, pady=10, ipady=7)


# Create button for entry
entrySearchButton = tk.Button(frame, text="Search",
                              width=15, font=fontsizeData, command=searchQuery)
entrySearchButton.grid(row=5, column=1, ipady=5, pady=5)


root.mainloop()
