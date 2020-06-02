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
certiNumVal = ""
import_file_path = ""
numDays = ""
certificationType = ""
courseType = ""
priceStatus = ""
certifiedAt = ""
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


def generateCertificate(courseName, numDays, date, certiNumValue, priceStatus):

    # capitalizing the arguments
    courseName = string.capwords(courseName)
    courseDays = string.capwords(numDays)
    courseDate = date
    certiNum = "TKWB2020-"
    # adding cno to certificate number
    certificateNum = 'C.No :- '+certiNum

    path = os.path.join(os.getcwd(), 'src', 'excelSheet', 'project')

    # Font style and size
    fontName = ImageFont.truetype(
        r''+path+'\style\Losttimoh.ttf', 180)

    fontCourse = ImageFont.truetype(
        r''+path+'\style\\701BoldBT.ttf', 75)

    fontDays = ImageFont.truetype(
        r''+path+'\style\\701BoldBT.ttf', 65)
    fontDate = ImageFont.truetype(
        r''+path+'\style\Asul-Regular.ttf', 70)

    # Looping for all certificate Generation
    for i in range(len(name)):
      # free session

        if(priceStatus == 'UNPAID'):
            # create Image object with the input image

            # free session content
            image = Image.open(
                r''+path+'\originalCertificate\\freeSession\originalCertificate.jpg')

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

            draw.text((x-(w/2), y), courseName,
                      fill=courseColor, font=fontCourse)

            # # starting position of the No. of Days

            (x, y) = (1595, 1582)
            courseColor = 'rgb(0, 0, 0)'  # black color

            # draw the message on the background
            w, h = draw.textsize(courseDays, font=fontDays)

            draw.text((x-(w/2), y), courseDays,
                      fill=courseColor, font=fontDays)

            # starting position of the date

            (x, y) = (1800, 1850)
            courseColor = 'rgb(0, 0, 0)'  # black color

            # draw the message on the background
            w, h = draw.textsize(courseDate, font=fontDate)

            draw.text((x-(w/2), y), courseDate,
                      fill=courseColor, font=fontDate)

            # save the edited image

            pdfPath = path+'\generatedCertificate\\freeSession\\' + \
                name[i]+'.jpg'

            image.save(r''+pdfPath)

            #
            #
            #
            # paid session
        elif(priceStatus == 'PAID'):
            image = Image.open(
                r''+path+'\originalCertificate\\paidSession\originalCertificate.jpg')

            # initialise the drawing context with
            # the image object as background

            draw = ImageDraw.Draw(image)

            # desired size

            fontCertificateNum = ImageFont.truetype(
                r''+path+'\style\Asul-Regular.ttf', 60)

            # starting position of the certificate number

            (x, y) = (2000, 100)
            nameColor = 'rgb(0, 0, 0)'  # black color

            # draw the message on the background
            w, h = draw.textsize(
                certificateNum+str(int(certiNumValue)+i), font=fontCertificateNum)

            draw.text((x-(w/2), y), certificateNum+str(int(certiNumValue)+i),
                      fill=nameColor, font=fontCertificateNum)

            # starting position of the name

            (x, y) = (1400, 890)
            nameColor = 'rgb(0,136,131)'  # black color

            # draw the message on the background
            w, h = draw.textsize(name[i], font=fontName)

            draw.text((x-(w/2), y), name[i], fill=nameColor, font=fontName)

            # starting position of the course name

            (x, y) = (1400, 1320)
            courseColor = 'rgb(0,136,131)'   # black color

            # draw the message on the background
            w, h = draw.textsize(courseName, font=fontCourse)

            draw.text((x-(w/2), y), courseName,
                      fill=courseColor, font=fontCourse)

            # # starting position of the No. of Days

            (x, y) = (1100, 1575)
            courseColor = 'rgb(0,136,131)'   # black color

            # draw the message on the background
            w, h = draw.textsize(courseDays, font=fontDays)

            draw.text((x-(w/2), y), courseDays,
                      fill=courseColor, font=fontDays)

            # starting position of the date

            (x, y) = (1500, 1930)
            courseColor = 'rgb(0, 0, 0)'  # black color

            # draw the message on the background
            w, h = draw.textsize(courseDate, font=fontDate)

            draw.text((x-(w/2), y), courseDate,
                      fill=courseColor, font=fontDate)

            # save the edited image

            pdfPath = path+'\generatedCertificate\paidSession\\' + \
                certiNum+str(int(certiNumValue)+i)+" "+name[i]+'.jpg'

            image.save(r''+pdfPath)

    tk.messagebox.showinfo(
        "Teckat", "Certificates generated successfully. do not close the window without pressing send email or else the data will be lost.")


def sendEmail():
    global certiNumVal
    global courseType
    global certificationType
    global certifiedAt
    # attach image
    path = os.path.join(os.getcwd(), 'src', 'excelSheet', 'project')
    certiNum = "TKWB2020-"
    for i in range(len(name)):
        if(i % 30 == 0 and i != 0):
            time.sleep(120)
        if(priceStatus == 'UNPAID'):
            pdfPath = path+'\generatedCertificate\\freeSession\\' + \
                name[i]+'.jpg'
        elif(priceStatus == 'PAID'):
            pdfPath = path+'\generatedCertificate\paidSession\\' + \
                certiNum+str(int(certiNumVal)+i)+" "+name[i]+'.jpg'
        print(pdfPath)
        print(os.path.basename(pdfPath))

        fromaddr = "noreply@teckat.com"
        toaddr = email[i]
        msg = MIMEMultipart()
        msg['From'] = "TECKAT <noreply@teckat.com>"
        msg['To'] = toaddr
        msg['Subject'] = "Certification for completion of {} {} successfully at Teckat {}".format(
            numDays, courseType, certifiedAt)
        body = '''
Dear {},

We hereby congratulate you for the completion of {} {} successfully.

We hereby certify you with {} for completion of course.

We wish to see you in further sessions.

Wishing you a good health.
Stay Home and Utilitize your lockdown period to achieve more.


Your review is highly essential.

https://www.google.com/search?q=teckat&rlz=1C1CHZL_enIN833IN833&oq=tec&aqs=chrome.1.69i60j69i59j69i57j69i60l2j69i65l3.2242j0j7&sourceid=chrome&ie=UTF-8#lrd=0x39f5e33bc994d481:0x2c77144bed77f5df,3,,,


Contact us at:

Instagram- https://www.instagram.com/india.teckat/

Facebook- https://www.facebook.com/in.teckat/

LinkedIn- https://www.linkedin.com/company/teckat-service-pvt-ltd/?viewAsMember=true


Thanks and Regards
Teckat Services Private Limited
Jamshedpur, Jharkhand
https://teckat.com


        '''.format(name[i], numDays, courseType, certificationType)
        msg.attach(MIMEText(body, 'plain'))

        img_data = open(pdfPath, 'rb').read()
        image = MIMEImage(img_data, name=os.path.basename(pdfPath))
        msg.attach(image)
        server = smtplib.SMTP_SSL('smtp.zoho.in:465')
        server.login(fromaddr, "hic996nZYet5")

        server.sendmail(fromaddr, toaddr, msg.as_string())
        server.quit()
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
    global certiNumVal
    global numDays
    global courseType
    global certificationType
    global priceStatus
    global certifiedAt
    firstRowIndex = int(entryFirstRowIndex.get())
    lastRowIndex = int(entryLastRowIndex.get())
    firstNameColumn = int(entryFirstNameIndex.get())
    lastNameColumn = int(entryLastNameIndex.get())
    emailColumn = int(entryEmailColumnIndex.get())
    courseName = entryCourseName.get()
    numDays = entryNumDays.get()
    numDays = numDays.lower()
    date = entryDate.get()
    certiNumVal = entryCertiNum.get()
    courseType = courseTypeVar.get()
    certificationType = certiTypeVar.get()
    priceStatus = priceStatusVar.get()
    certifiedAt = certifiedAtVar.get()
    print(firstRowIndex, lastRowIndex, firstNameColumn,
          lastNameColumn, emailColumn, courseName, numDays, date, type(date), type(firstRowIndex))
    tk.messagebox.showinfo(
        "Teckat", "Data stored Successfully wait for certificate generation")

    getExcelData(firstRowIndex, lastRowIndex,
                 firstNameColumn, lastNameColumn, emailColumn)
    generateCertificate(courseName, numDays, date, certiNumVal, priceStatus)


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

startCertiNumLabel = tk.Label(
    root, text="Starting Certi Number", font=fontsizeData)
startCertiNumLabel.grid(row=9, column=0, pady=10)


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

entryCertiNum = tk.Entry(root, width=30, font=fontsizeData)
entryCertiNum.grid(row=9, column=1, padx=10, pady=10)


# Drop down labels and entry

priceStatusLabel = tk.Label(
    root, text="Course Type", font=fontsizeData)
priceStatusLabel.grid(row=1, column=2, pady=10)

courseTypeLabel = tk.Label(
    root, text="Course Type", font=fontsizeData)
courseTypeLabel.grid(row=2, column=2, pady=10)

certificationTypeLabel = tk.Label(
    root, text="Certification Type", font=fontsizeData)
certificationTypeLabel.grid(row=3, column=2, pady=10)

CertifiedAtLabel = tk.Label(
    root, text="Certified At", font=fontsizeData)
CertifiedAtLabel.grid(row=4, column=2, pady=10)
# =========== price status ======================
# Create a Tkinter variable
priceStatusVar = tk.StringVar(root)

# Dictionary with options
priceStatusChoices = {'PAID', 'UNPAID'}
priceStatusVar.set('PAID')  # set the default option

priceStatusMenu = tk.OptionMenu(root, priceStatusVar, *priceStatusChoices)
priceStatusMenu.grid(row=1, column=3, padx=10, pady=10)

# ========== certificate type =========================
# Create a Tkinter variable
certiTypeVar = tk.StringVar(root)

# Dictionary with options
certificateChoices = {'ISO CERTIFICATION', 'CERTIFICATION'}
certiTypeVar.set('CERTIFICATION')  # set the default option

certiMenu = tk.OptionMenu(root, certiTypeVar, *certificateChoices)
certiMenu.grid(row=3, column=3, padx=10, pady=10)


# ======================= course type ==================

# Create a Tkinter variable
courseTypeVar = tk.StringVar(root)

# Dictionary with options
courseChoices = {'Webinar Session', 'Internship', 'Workshop'}
courseTypeVar.set('Webinar Session')  # set the default option

courseMenu = tk.OptionMenu(root, courseTypeVar, *courseChoices)
courseMenu.grid(row=2, column=3, padx=10, pady=10)


# ======================= Certified At ==================

# Create a Tkinter variable
certifiedAtVar = tk.StringVar(root)

# Dictionary with options
certifiedAtChoices = {'webinar series 1.0', 'webinar series 2.0'}
certifiedAtVar.set('webinar series 2.0')  # set the default option

certifiedAtMenu = tk.OptionMenu(root, certifiedAtVar, *certifiedAtChoices)
certifiedAtMenu.grid(row=4, column=3, padx=10, pady=10)


# Submit button
GenerateCertificateButton = tk.Button(root, text="Generate Certificate",
                                      width=20, font=fontsizeData, command=mainFunction)
GenerateCertificateButton.grid(row=10, column=1, pady=20)

sendEmailButton = tk.Button(root, text="Send Email",
                            width=15, font=fontsizeData, command=sendEmail)
sendEmailButton.grid(row=11, column=1, pady=20)

clearDataButton = tk.Button(root, text="Clear Data",
                            width=15, font=fontsizeData, command=clearData)
clearDataButton.grid(row=11, column=0, pady=20)

root.mainloop()
