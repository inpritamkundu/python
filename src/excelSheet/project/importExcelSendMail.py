import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox
import tkinter.font as font
import xlrd
from PIL import Image, ImageDraw, ImageFont
import os
import string
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import time


root = tk.Tk()
root.geometry("1536x720")
width = root.winfo_screenwidth()

fontsizeData = font.Font(size=15)

name = []
email = []
link = []
import_file_path = ""
# ============================ functions ==============================================

# Get excel path


def getExcelPath():
    global import_file_path
    import_file_path = filedialog.askopenfilename()
    print(import_file_path, type(import_file_path))

# Get excel Data


def getExcelData(firstRowIndex, lastRowIndex, firstNameColumn, lastNameColumn, emailColumn, linkColumn):
    global import_file_path
    global name
    global email
    global link

    print()

    loc = (r''+import_file_path)

    # To open Workbook
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)

    # loop for name and mail
    for i in range(firstRowIndex-1, lastRowIndex):
        name.append(string.capwords(sheet.cell_value(i, firstNameColumn-1) + " " +
                                    sheet.cell_value(i, lastNameColumn-1)))
        email.append(sheet.cell_value(i, emailColumn-1))
        link.append(sheet.cell_value(i, linkColumn-1).split(','))
    print(name)
    print(email)
    print(link)
    tk.messagebox.showinfo(
        "Teckat", "Data generated successfully.")


def sendEmail():
    # attach image
    # path = os.path.join(os.getcwd(), 'src', 'excelSheet', 'project')
    # certiNum = "TKWB2020-"
    global name
    global link
    global email
    for i in range(len(name)):
        if(i % 30 == 0 and i != 0):
            time.sleep(300)

        fromaddr = "noreply@teckat.com"
        toaddr = email[i]
        msg = MIMEMultipart()
        msg['From'] = "Teckat Student Intern Partner <noreply@teckat.com>"
        msg['To'] = toaddr
        msg['Subject'] = "T-SIP 2.O : RESULT TIME"
        body = '''

Dear {},

We regret to inform you that you have not qualified the written round held on 12 July 2020.
We hope to see you in the next internship program. 
Somewhere your answers were not satisfying in the written round.
We are thankful to you for your valuable time you spent with us during selection procedure.

Keep upgrading yourself and wish you good luck for the future.
Thank you.

link 50/-   -> {}
link 149/-  -> {}
link 1189/- -> {}

Contact us at:

Instagram-  https://www.instagram.com/india.teckat/
            https://www.instagram.com/in.teckat/

Facebook- https://www.facebook.com/in.teckat/

LinkedIn- https://www.linkedin.com/company/teckat-service-pvt-ltd/?viewAsMember=true

For any further queries you may mail us at support@teckat.com

Thanks and Regards
Teckat Services Private Limited
Jamshedpur, Jharkhand
https://teckat.com


        '''.format(name[i], link[i][0], link[i][1], link[i][2])
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP_SSL('smtp.zoho.in:465')
        server.login(fromaddr, "hic996nZYet5")

        server.sendmail(fromaddr, toaddr, msg.as_string())
        server.quit()
        print(name[i])
        print(" email sent")
    tk.messagebox.showinfo(
        "Teckat", "Emails sent successfully.")


def clearData():
    # clear arrays
    name.clear()
    email.clear()
    link.clear()
    print(name, email, link)
    tk.messagebox.showinfo(
        "Teckat", "Data Cleared successfully.")
    # main parent function


def mainFunction():
    firstRowIndex = int(entryFirstRowIndex.get())
    lastRowIndex = int(entryLastRowIndex.get())
    firstNameColumn = int(entryFirstNameIndex.get())
    lastNameColumn = int(entryLastNameIndex.get())
    emailColumn = int(entryEmailColumnIndex.get())
    linkColumn = int(entryLinkColumnIndex.get())
    print(firstRowIndex, lastRowIndex, firstNameColumn,
          lastNameColumn, emailColumn, linkColumn)
    tk.messagebox.showinfo(
        "Teckat", "Data stored Successfully wait for data generation")

    getExcelData(firstRowIndex, lastRowIndex,
                 firstNameColumn, lastNameColumn, emailColumn, linkColumn)


# ================================================ GUI ===============================================================
    # excel button
browseButton_Excel = tk.Button(root, text='Import Excel File', command=getExcelPath,
                               bg='green', fg='white', height=2, width=30, font=('helvetica', 12, 'bold'))
browseButton_Excel.grid(row=0, column=1, pady=30)

# labels
firstRowIndexLabel = tk.Label(
    root, text="Starting Row No.", font=fontsizeData)
firstRowIndexLabel.grid(row=1, column=0, pady=10)

lastRowIndexLabel = tk.Label(
    root, text="Ending Row No.", font=fontsizeData)
lastRowIndexLabel.grid(row=2, column=0, pady=10)

firstNameColumnLabel = tk.Label(
    root, text="First Name Column No.", font=fontsizeData)
firstNameColumnLabel.grid(row=3, column=0, pady=10)

lastNameColumnLabel = tk.Label(
    root, text="Last Name Coloumn No.", font=fontsizeData)
lastNameColumnLabel.grid(row=4, column=0, pady=10)

emailColumnLabel = tk.Label(
    root, text="Email Column No.", font=fontsizeData)
emailColumnLabel.grid(row=5, column=0, pady=10)

linkColumnLabel = tk.Label(
    root, text="Link Column No.", font=fontsizeData)
linkColumnLabel.grid(row=6, column=0, pady=10)


# Input fields
entryFirstRowIndex = tk.Entry(root, width=30, font=fontsizeData)
entryFirstRowIndex.grid(row=1, column=1, padx=10, pady=10)

entryLastRowIndex = tk.Entry(root, width=30, font=fontsizeData)
entryLastRowIndex.grid(row=2, column=1, padx=10, pady=10)

entryFirstNameIndex = tk.Entry(root, width=30, font=fontsizeData)
entryFirstNameIndex.grid(row=3, column=1, padx=10, pady=10)

entryLastNameIndex = tk.Entry(root, width=30, font=fontsizeData)
entryLastNameIndex.grid(row=4, column=1, padx=10, pady=10)

entryEmailColumnIndex = tk.Entry(root, width=30, font=fontsizeData)
entryEmailColumnIndex.grid(row=5, column=1, padx=10, pady=10)

entryLinkColumnIndex = tk.Entry(root, width=30, font=fontsizeData)
entryLinkColumnIndex.grid(row=6, column=1, padx=10, pady=10)

# Submit button

generatedataButton = tk.Button(root, text="Generate Data",
                               width=15, font=fontsizeData, command=mainFunction)
generatedataButton.grid(row=10, column=0, pady=20)

sendEmailButton = tk.Button(root, text="Send Email",
                            width=15, font=fontsizeData, command=sendEmail)
sendEmailButton.grid(row=10, column=1, pady=20)

clearDataButton = tk.Button(root, text="Clear Data",
                            width=15, font=fontsizeData, command=clearData)
clearDataButton.grid(row=10, column=2, pady=20)

root.mainloop()
