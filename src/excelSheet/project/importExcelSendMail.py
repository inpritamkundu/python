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
from email.mime.base import MIMEBase
from email import encoders
import time


root = tk.Tk()
root.geometry("1536x720")
width = root.winfo_screenwidth()

fontsizeData = font.Font(size=15)

name = []
email = []
link = []
path = []
import_file_path = ""
# ============================ functions ==============================================

# Get excel path


def getExcelPath():
    global import_file_path
    import_file_path = filedialog.askopenfilename()
    print(import_file_path, type(import_file_path))


# Get attachment path
def getAttachmentPath():
    import_file_path = filedialog.askopenfilename()
    path.append(import_file_path)
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
        if(linkColumn != ''):
            link.append(sheet.cell_value(i, linkColumn-1).split(','))
    print(name)
    print(email)
    print(link)
    print(path)
    tk.messagebox.showinfo(
        "Teckat", "Data generated successfully.")


def sendEmail():
    # attach image
    # path = os.path.join(os.getcwd(), 'src', 'excelSheet', 'project')
    # certiNum = "TKWB2020-"
    global name
    global link
    global email
    global path

    for i in range(len(name)):
        if(i % 30 == 0 and i != 0):
            time.sleep(300)

        fromaddr = "noreply@teckat.com"
        toaddr = email[i]
        msg = MIMEMultipart()
        msg['From'] = "Teckat Student Intern Partner <noreply@teckat.com>"
        msg['To'] = toaddr
        msg['Subject'] = "FIRST BONUS WEEK AT T-SIP 2.O"
        body = '''

Dear {},

This is your first bonus week. So utilize the entire week wisely.

This bonus week will be in terms of extra percentage that you receive on eacb payment.

Dated from 16 July 2020 to  25 July 2020, the entire week is the bonus week.

What to do ?
You have to get as many successful enrollment of students in various workshops and Webinars only  to be conducted.

What you get?
You will get 20% , on each successful payment in any of the workshop course and 15% , on each successful payment in any of the  webinar course.

Remember- This bonus week is only for successful payment coming in workshops and Webinars

Count each day in your hands and grab the opportunity to add something good in your account.

All the best.

        '''.format(name[i])
        msg.attach(MIMEText(body, 'plain'))

        html = '''
        
<html>
  <head></head>
  <body>

<div><!--[if mso]>
  <v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="http://teckat.com" style="height:40px;v-text-anchor:middle;width:200px;" arcsize="10%" strokecolor="#1e3650" fillcolor="#556270">
    <w:anchorlock/>
    <center style="color:#ffffff;font-family:sans-serif;font-size:13px;font-weight:bold;">Show me the button!</center>
  </v:roundrect>
<![endif]--><a href="http://teckat.com"
style="background-color:#556270;border:1px solid #1e3650;border-radius:4px;color:#ffffff;display:inline-block;font-family:sans-serif;font-size:13px;font-weight:bold;line-height:40px;text-align:center;text-decoration:none;width:200px;-webkit-text-size-adjust:none;mso-hide:all;">Show me the button!</a></div>
    
<div>
    <br>
</div>
<div data-zbluepencil-ignore="true" id="Zm-_Id_-Sgn">
    <div>
        <table style="box-sizing: border-box; border-spacing: 0px; border-collapse: collapse; background-color: rgb(255, 255, 255); color: rgb(68, 68, 68); font-style: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; width: 525px; font-size: 11pt; font-family: Arial, sans-serif" class="ng-scope" cellspacing="0" cellpadding="0">
            <tbody style="box-sizing: border-box">
                <tr style="box-sizing: border-box">
                    <td style="box-sizing: border-box; padding: 0px 10px 0px 0px; font-size: 10pt; font-family: Arial, sans-serif; border-right: 1px solid rgb(251, 99, 3); width: 125px; vertical-align: top" class="ng-scope" rowspan="6" valign="top" width="125">
                        <a style="box-sizing: border-box; background-color: transparent; color: rgb(51, 122, 183); text-decoration: none" class="ng-scope" target="_blank" href="https://teckat.com/">
                            <img style="box-sizing: border-box; border: 0px; vertical-align: middle; width: 105px; height: auto" src="https://teckat.com/images/icons/icon-72x72.png" width="105" alt="Logo" border="0" height="auto">
                        </a>
                        <br>
                    </td>
                    <td style="box-sizing: border-box; padding: 0px 0px 0px 10px">
                        <table style="box-sizing: border-box; border-spacing: 0px; border-collapse: collapse; background-color: transparent" cellspacing="0" cellpadding="0">
                            <tbody style="box-sizing: border-box">
                                <tr style="box-sizing: border-box">
                                    <td style="box-sizing: border-box; padding: 0px 0px 5px 10px; font-size: 10pt; color: rgb(0, 121, 172); font-family: Arial, sans-serif; width: 400px; vertical-align: top" valign="top">
                                        THANKS &amp; REGARDS
                                        <br>
                                    </td>
                                </tr>
                                <tr style="box-sizing: border-box">
                                    <td style="box-sizing: border-box; padding: 5px 0px 5px 10px; font-size: 10pt; color: rgb(68, 68, 68); font-family: Arial, sans-serif; vertical-align: top; line-height: 17px" valign="top">
                                        <span style="box-sizing: border-box" class="ng-scope">
                                            <span class="colour" style="color: rgb(251, 99, 3); box-sizing: border-box;">
                                                <b>
                                                    a:
                                                    <span>
                                                        &nbsp;
                                                    </span>
                                                </b>
                                            </span>
                                            <span class="colour" style="color:rgb(0, 0, 0)">
                                                <span class="font" style="font-family:Arial, sans-serif">
                                                    <span class="size" style="font-size: 10pt; box-sizing: border-box;">
                                                        Teckat Services Private Limited
                                                    </span>
                                                </span>
                                            </span>
                                            <span>
                                                &nbsp;
                                            </span>
                                            <span class="colour" style="color:rgb(0, 0, 0)">
                                                <span class="font" style="font-family:Arial, sans-serif">
                                                    <span class="size" style="font-size: 10pt; box-sizing: border-box;">
                                                        <span style="box-sizing: border-box" class="ng-scope">
                                                            |
                                                            <span>
                                                                &nbsp;
                                                            </span>
                                                        </span>
                                                        14, Sidhgora Main Market, Sidhgora, Jamshedpur, Jharkhand
                                                    </span>
                                                </span>
                                            </span>
                                            <span>
                                                &nbsp;
                                            </span>
                                            <span class="colour" style="color:rgb(0, 0, 0)">
                                                <span class="font" style="font-family:Arial, sans-serif">
                                                    <span class="size" style="font-size: 10pt; box-sizing: border-box;">
                                                        <span style="box-sizing: border-box" class="ng-scope">
                                                            |
                                                            <span>
                                                                &nbsp;
                                                            </span>
                                                        </span>
                                                        831009
                                                    </span>
                                                </span>
                                            </span>
                                            <br style="box-sizing: border-box">
                                            <span class="colour" style="color: rgb(251, 99, 3); box-sizing: border-box;">
                                                <b>
                                                    e:
                                                </b>
                                            </span>
                                            <span class="colour" style="color:rgb(0, 0, 0)">
                                                <span class="font" style="font-family:Arial, sans-serif">
                                                    <span class="size" style="font-size: 10pt; box-sizing: border-box;">
                                                        <span>
                                                            &nbsp;
                                                        </span>
                                                        <a target="_blank" href="mailto:support@teckat.com">
                                                            support@teckat.com
                                                        </a>
                                                    </span>
                                                </span>
                                            </span>
                                        </span>
                                        <span>
                                            &nbsp;
                                        </span>
                                        <span style="box-sizing: border-box" class="ng-scope">
                                            <span style="box-sizing: border-box" class="ng-scope">
                                                |
                                                <span>
                                                    &nbsp;
                                                </span>
                                            </span>
                                            <span class="colour" style="color: rgb(251, 99, 3); box-sizing: border-box;">
                                                <b>
                                                    w:
                                                </b>
                                            </span>
                                            <a style="box-sizing: border-box; background-color: transparent; color: rgb(51, 122, 183); text-decoration: none" target="_blank" href="http://teckat.com/">
                                                <span class="colour" style="color:rgb(0, 0, 0)">
                                                    <span class="font" style="font-family:Arial, sans-serif">
                                                        <span class="size" style="font-size: 10pt; box-sizing: border-box;">
                                                            <span>
                                                                &nbsp;
                                                            </span>
                                                            teckat.com
                                                        </span>
                                                    </span>
                                                </span>
                                            </a>
                                            <br style="box-sizing: border-box">
                                            <span class="colour" style="color: rgb(251, 99, 3); box-sizing: border-box;">
                                                <b>
                                                    m:
                                                </b>
                                            </span>
                                            <span class="colour" style="color:rgb(0, 0, 0)">
                                                <span class="font" style="font-family:Arial, sans-serif">
                                                    <span class="size" style="font-size: 10pt; box-sizing: border-box;">
                                                        <span>
                                                            &nbsp;
                                                        </span>
                                                        9337704495
                                                    </span>
                                                </span>
                                            </span>
                                        </span>
                                    </td>
                                </tr>
                                <tr style="box-sizing: border-box" class="ng-scope">
                                    <td style="box-sizing: border-box; padding: 5px 0px 0px 10px; font-size: 10pt; font-family: Arial, sans-serif; vertical-align: bottom" valign="bottom">
                                        <span style="box-sizing: border-box" class="ng-scope">
                                            <a style="box-sizing: border-box; background-color: transparent; color: rgb(51, 122, 183); text-decoration: none" target="_blank" href="https://www.facebook.com/in.teckat/">
                                                <img style="box-sizing: border-box; border: 0px; vertical-align: middle; height: 19px; width: 19px" src="https://codetwocdn.azureedge.net/images/mail-signatures/generator-dm/bease-fox/fb.png" alt="facebook icon" width="19" border="0" height="19">
                                            </a>
                                            &nbsp;
                                            <a style="box-sizing: border-box; background-color: transparent; color: rgb(51, 122, 183); text-decoration: none" target="_blank" href="https://www.linkedin.com/company/teckat-service-pvt-ltd/?viewAsMember=true">
                                                <img style="box-sizing: border-box; border: 0px; vertical-align: middle; height: 19px; width: 19px" src="https://codetwocdn.azureedge.net/images/mail-signatures/generator-dm/bease-fox/ln.png" alt="linkedin icon" width="19" border="0" height="19">
                                            </a>
                                            &nbsp;
                                            <a style="box-sizing: border-box; background-color: transparent; color: rgb(51, 122, 183); text-decoration: none" target="_blank" href="https://www.instagram.com/india.teckat/">
                                                <img style="box-sizing: border-box; border: 0px; vertical-align: middle; height: 19px; width: 19px" src="https://codetwocdn.azureedge.net/images/mail-signatures/generator-dm/bease-fox/it.png" alt="instagram icon" width="19" border="0" height="19">
                                            </a>
                                            &nbsp;
                                        </span>
                                        <br>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </td>
                </tr>
            </tbody>
        </table>
        <div>
            <br>
        </div>
    </div>
</div>
<br>
<br>

  </body>
</html>

        '''
        msg.attach(MIMEText(html, 'html'))

        # attach attachments if present

        if(len(path)):
            for j in range(len(path)):

                # Generating File name
                emailFileName = path[j].split('/')
                print(emailFileName)
                # open the file to be sent
                filename = emailFileName[-1]
                attachment = open(path[i], "rb")

                # instance of MIMEBase and named as p
                p = MIMEBase('application', 'octet-stream')

                # To change the payload into encoded form
                p.set_payload((attachment).read())

                # encode into base64
                encoders.encode_base64(p)

                p.add_header('Content-Disposition',
                             "attachment; filename= %s" % filename)

                # attach the instance 'p' to instance 'msg'
                msg.attach(p)

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
    path.clear()
    print(name, email, link, path)
    tk.messagebox.showinfo(
        "Teckat", "Data Cleared successfully.")
    # main parent function


def mainFunction():
    firstRowIndex = int(entryFirstRowIndex.get())
    lastRowIndex = int(entryLastRowIndex.get())
    firstNameColumn = int(entryFirstNameIndex.get())
    lastNameColumn = int(entryLastNameIndex.get())
    emailColumn = int(entryEmailColumnIndex.get())
    linkStatus = int(linkVar.get())
    if(linkStatus == 1):

        linkColumn = int(entryLinkColumnIndex.get())
    else:
        linkColumn = ""
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

linkVar = tk.IntVar()

tk.Checkbutton(root, text="Do you want to attach Link",
               variable=linkVar, font=fontsizeData).grid(row=6, column=2, padx=5, pady=5)

# attachment button
# excel button
browseButton_Excel = tk.Button(root, text='Attach files one by one', command=getAttachmentPath,
                               bg='green', fg='white', height=2, width=30, font=('helvetica', 12, 'bold'))
browseButton_Excel.grid(row=7, column=1, pady=30)


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
