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
import_file_path = ""
# ============================ functions ==============================================

# Get excel path


def getExcelPath():
    global import_file_path
    import_file_path = filedialog.askopenfilename()
    print(import_file_path, type(import_file_path))

# Get excel Data


def getExcelData(firstRowIndex, lastRowIndex, firstNameColumn, lastNameColumn, emailColumn):
    global import_file_path
    global name
    global email

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
    print(name)
    print(email)


def sendEmail():
    # attach image
    path = os.path.join(os.getcwd(), 'src', 'excelSheet', 'project')
    certiNum = "TKWB2020-"
    for i in range(len(name)):
        if(i % 30 == 0 and i != 0):
            time.sleep(120)

        fromaddr = "noreply@teckat.com"
        toaddr = email[i]
        msg = MIMEMultipart()
        msg['From'] = "TECKAT <noreply@teckat.com>"
        msg['To'] = toaddr
        msg['Subject'] = "Mail regarding Internship work details."
        body = '''

Dear {},
We hereby notify you with your work during the internship period.

1. 2 day workshop shall reach the target of 10 participants in each workshop. 
2. 10 days paid Webinar Series shall reach the target of 10 participants.
3. 30 days and 45 days summer internship shall reach the target of 10 participants.


Note:
Below is the attachment of all the above 3 description.
You may use it for your Promotion.

You have been given details of incentive throughout the internship. Keep it safe for your reference.


Important note:
*You will recieve your incentive at once after the completion of internship
*You will be certified for the internship after the completion of internship.
*Any bonus added to your incentive will be released together after the completion of internship.
* You will be sent 3 different link on your whatsapp for getting participants registered.

Contact us at:

Instagram- https://www.instagram.com/india.teckat/

Facebook- https://www.facebook.com/in.teckat/

LinkedIn- https://www.linkedin.com/company/teckat-service-pvt-ltd/?viewAsMember=true

Mail : support@teckat.com

Thanks and Regards
Teckat Services Private Limited
Jamshedpur, Jharkhand
https://teckat.com


        '''.format(name[i])
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
    print(name, email)
    tk.messagebox.showinfo(
        "Teckat", "Data Cleared successfully.")
    # main parent function


def mainFunction():
    firstRowIndex = int(entryFirstRowIndex.get())
    lastRowIndex = int(entryLastRowIndex.get())
    firstNameColumn = int(entryFirstNameIndex.get())
    lastNameColumn = int(entryLastNameIndex.get())
    emailColumn = int(entryEmailColumnIndex.get())
    print(firstRowIndex, lastRowIndex, firstNameColumn,
          lastNameColumn, emailColumn)
    tk.messagebox.showinfo(
        "Teckat", "Data stored Successfully wait for certificate generation")

    getExcelData(firstRowIndex, lastRowIndex,
                 firstNameColumn, lastNameColumn, emailColumn)


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
