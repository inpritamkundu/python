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

# Will Delete when submit entry is clicked

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


    # ======================================================   GUI   =============================================================
    # Adding frame
frame = tk.Frame(root)
frame.place(relx=0.2, rely=0.1, relwidth=0.8, relheight=0.8)

# Adding main label
DeleteDataLabel = tk.Label(frame, text="Delete Data",
                           font=fontSizeHeading)
DeleteDataLabel.grid(row=0, column=1)

# Adding data label
entryDeleteIdLabel = tk.Label(frame, text="Delete by ID : ", font=fontsizeData)
entryDeleteIdLabel.grid(row=1, column=0, pady=2)


# Adding entry form for data label
entryDeleteId = tk.Entry(frame, width=50, font=fontsizeData)
entryDeleteId.grid(row=1, column=1, pady=10, ipady=7)
entryDeleteId.focus()

# Create button for entry
entryDeleteButton = tk.Button(frame, text="Delete",
                              width=15, font=fontsizeData, command=DeleteQuery)
entryDeleteButton.grid(row=2, column=1, ipady=5, pady=5)


root.mainloop()
