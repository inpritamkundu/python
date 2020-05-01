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

# Generate Certificate


def generateCertificate(courseName, numDays, date):
    print()
    # capitalizing the arguments
    courseName = string.capwords(courseName)
    courseDays = string.capwords(numDays)
    courseDate = date

    # adding cno to certificate number
    # certificateNum = 'C.No :- '+certificateNum

    path = os.path.join(os.getcwd(), 'src', 'excelSheet', 'project')

    # Font style and size
    fontName = ImageFont.truetype(
        r''+path+'\style\DancingScript.ttf', 130)

    fontCourse = ImageFont.truetype(
        r''+path+'\style\Asul-Regular.ttf', 75)

    fontDays = ImageFont.truetype(
        r''+path+'\style\Asul-Regular.ttf', 65)
    fontDate = ImageFont.truetype(
        r''+path+'\style\Asul-Regular.ttf', 70)

    # Looping for all certificate Generation
    for i in range(len(name)):

        # create Image object with the input image

        image = Image.open(
            r''+path+'\originalCertificate\originalCertificate.jpg')

        # initialise the drawing context with
        # the image object as background

        draw = ImageDraw.Draw(image)

        # desired size

        # fontCertificateNum = ImageFont.truetype(
        #     r''+path+'\style\Asul-Regular.ttf', 50)

        # starting position of the certificate number

        # (x, y) = (2500, 100)
        # nameColor = 'rgb(0, 0, 0)'  # black color

        # # draw the message on the background
        # w, h = draw.textsize(certificateNum, font=fontCertificateNum)

        # draw.text((x-(w/2), y), certificateNum,
        #           fill=nameColor, font=fontCertificateNum)

        # starting position of the name

        (x, y) = (1800, 990)
        nameColor = 'rgb(54, 127, 193)'  # black color

        # draw the message on the background
        w, h = draw.textsize(name[i], font=fontName)

        draw.text((x-(w/2), y), name[i], fill=nameColor, font=fontName)

        # starting position of the course name

        (x, y) = (1775, 1370)
        courseColor = 'rgb(0, 0, 0)'  # black color

        # draw the message on the background
        w, h = draw.textsize(courseName, font=fontCourse)

        draw.text((x-(w/2), y), courseName, fill=courseColor, font=fontCourse)

        # # starting position of the No. of Days

        (x, y) = (1595, 1582)
        courseColor = 'rgb(0, 0, 0)'  # black color

        # draw the message on the background
        w, h = draw.textsize(courseDays, font=fontDays)

        draw.text((x-(w/2), y), courseDays, fill=courseColor, font=fontDays)

        # starting position of the date

        (x, y) = (1800, 1850)
        courseColor = 'rgb(0, 0, 0)'  # black color

        # draw the message on the background
        w, h = draw.textsize(courseDate, font=fontDate)

        draw.text((x-(w/2), y), courseDate, fill=courseColor, font=fontDate)

        # save the edited image

        pdfPath = path+'\generatedCertificate\\'+name[i]+'.jpg'

        image.save(r''+pdfPath)

    tk.messagebox.showinfo(
        "Teckat", "Certificates generated successfully. do not close the window without pressing send email or else the data will be lost.")


def sendEmail():
    # attach image
    path = os.path.join(os.getcwd(), 'src', 'excelSheet', 'project')
    for i in range(len(name)):
        pdfPath = path+'\generatedCertificate\\'+name[i]+'.jpg'

        print(pdfPath)
        print(os.path.basename(pdfPath))

        fromaddr = "noreply@teckat.com"
        toaddr = email[i]
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Test Subject"
        body = ''' hello
        This is pritam
            CEO Teckat'''
        msg.attach(MIMEText(body, 'plain'))

        img_data = open(pdfPath, 'rb').read()
        image = MIMEImage(img_data, name=os.path.basename(pdfPath))
        msg.attach(image)
        server = smtplib.SMTP_SSL('smtp.zoho.in:465')
        server.login(fromaddr, "hic996nZYet5")

        server.sendmail(fromaddr, toaddr, msg.as_string())

        server.quit()

# main parent function


def mainFunction():
    firstRowIndex = int(entryFirstRowIndex.get())
    lastRowIndex = int(entryLastRowIndex.get())
    firstNameColumn = int(entryFirstNameIndex.get())
    lastNameColumn = int(entryLastNameIndex.get())
    emailColumn = int(entryEmailColumnIndex.get())
    courseName = entryCourseName.get()
    numDays = entryNumDays.get()
    date = entryDate.get()
    print(firstRowIndex, lastRowIndex, firstNameColumn,
          lastNameColumn, emailColumn, courseName, numDays, date, type(date), type(firstRowIndex))
    tk.messagebox.showinfo(
        "Teckat", "Data stored Successfully wait for certificate generation")

    getExcelData(firstRowIndex, lastRowIndex,
                 firstNameColumn, lastNameColumn, emailColumn)
    generateCertificate(courseName, numDays, date)


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

courseNameLabel = tk.Label(root, text="Course Name", font=fontsizeData)
courseNameLabel.grid(row=6, column=0, pady=10)

numDaysLabel = tk.Label(
    root, text="Number of Days (eg. 10 Days)", font=fontsizeData)
numDaysLabel.grid(row=7, column=0, pady=10)

dateLabel = tk.Label(root, text="Date (eg. 01/05/2020)", font=fontsizeData)
dateLabel.grid(row=8, column=0, pady=10)


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

entryCourseName = tk.Entry(root, width=30, font=fontsizeData)
entryCourseName.grid(row=6, column=1, padx=10, pady=10)

entryNumDays = tk.Entry(root, width=30, font=fontsizeData)
entryNumDays.grid(row=7, column=1, padx=10, pady=10)

entryDate = tk.Entry(root, width=30, font=fontsizeData)
entryDate.grid(row=8, column=1, padx=10, pady=10)

# Submit button
GenerateCertificateButton = tk.Button(root, text="Generate Certificate",
                                      width=20, font=fontsizeData, command=mainFunction)
GenerateCertificateButton.grid(row=9, column=1, pady=20)

sendEmailButton = tk.Button(root, text="Send Email",
                            width=15, font=fontsizeData, command=sendEmail)
sendEmailButton.grid(row=10, column=1, pady=20)

root.mainloop()
