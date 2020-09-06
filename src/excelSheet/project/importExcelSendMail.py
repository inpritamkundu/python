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
root.geometry("1536x1020")
width = root.winfo_screenwidth()

fontsizeData = font.Font(size=15)

name = []
email = []
link = []
path = []
tsipId = []
import_file_path = ""
tsipStatus = ""
generatePaymentLink = ""
mailStatus = ""
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


def getExcelData(firstRowIndex, lastRowIndex, firstNameColumn, lastNameColumn, emailColumn, linkColumn, idColumn):
    global import_file_path
    global name
    global email
    global link
    global tsipId

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
        if(idColumn != ''):
            tsipId.append(int(sheet.cell_value(i, idColumn-1)))

    print(name)
    print(email)
    print(link)
    print(path)
    print(tsipId)
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
    global tsipStatus
    global generatePaymentLink
    global mailStatus
    for i in range(len(name)):
        separate = name[i].split()
        if(i % 30 == 0 and i != 0):
            time.sleep(400)

        fromaddr = "noreply@teckat.com"
        toaddr = email[i]
        msg = MIMEMultipart()
        msg['From'] = "Teckat Student Intern Partner <noreply@teckat.com>"
        msg['To'] = toaddr

        if(tsipStatus == 'T-SIP 2.0'):
            msg['Subject'] = "HIP! HIP! HURRAY! - Here you go with the fourth contest in this Internship."

        elif(tsipStatus == 'T-SIP 3.0'):
            if(mailStatus == 'Thank you for submitting application'):
                msg['Subject'] = "Thank you for submitting your application at “T-SIP 3.0”"
            elif(mailStatus == 'application under review'):
                msg['Subject'] = "YOUR APPLICATION IS UNDER REVIEW - YOU CAN MAIL US IF YOU ARE HAVING ANY INTERROGATION"
            elif(mailStatus == 'Result Declaration'):
                msg['Subject'] = "Congratulations! You are Selected at T-SIP 3.0 - Go through the mail for further information."
            elif(mailStatus == 'Payment referral generate link'):
                msg['Subject'] = "READY! STEADY! AND GO! - Here you go with the first Incentive  earning Hours"
            elif(mailStatus == 'Bonus Hours'):
                msg['Subject'] = "FREE! FREE! FREE! - ASK YOUR FRIENDS AND COLLEAGUES TO REGISTER FOR THE EVENT (GET E-CERTIFICATION)"
#         body = '''

# Dear {},

# This is your first bonus week. So utilize the entire week wisely.

# This bonus week will be in terms of extra percentage that you receive on eacb payment.

# Dated from 16 July 2020 to  25 July 2020, the entire week is the bonus week.

# What to do ?
# You have to get as many successful enrollment of students in various workshops and Webinars only  to be conducted.

# What you get?
# You will get 20% , on each successful payment in any of the workshop course and 15% , on each successful payment in any of the  webinar course.

# Remember- This bonus week is only for successful payment coming in workshops and Webinars

# Count each day in your hands and grab the opportunity to add something good in your account.

# All the best.

#         '''.format(name[i])
#         msg.attach(MIMEText(body, 'plain'))

        if(tsipStatus == 'T-SIP 2.0'):
            print()

            # generate payment link
            if(generatePaymentLink == 1):
                print(separate)
                strLink1 = link[0][0]+'?referral=TSIP02' + \
                    separate[0][0:1]+separate[1][0:1]+str(tsipId[i])
                strLink2 = link[0][1]+'?referral=TSIP02' + \
                    separate[0][0:1]+separate[1][0:1]+str(tsipId[i])
                strLink3 = link[0][2]+'?referral=TSIP02' + \
                    separate[0][0:1]+separate[1][0:1]+str(tsipId[i])
                print(strLink1)
                print(strLink2)
                print(strLink3)

                # html

                html = '''

<html>
  <head></head>
  <body>


<div>
    <div style="font-family: Verdana, Arial, Helvetica, sans-serif;font-size: 10.0pt;">
        <div>
            <div style="font-family: Verdana, Arial, Helvetica, sans-serif;font-size: 10.0pt;">
                <div>
                    <div style="font-family: Verdana, Arial, Helvetica, sans-serif;font-size: 10.0pt;">
                        <div>
                            <div style="font-family: Verdana, Arial, Helvetica, sans-serif;font-size: 10.0pt;">
                                <div>
                                    <div style="font-family: Verdana, Arial, Helvetica, sans-serif;font-size: 10.0pt;">
                                        <div>
                                            <div style="font-family: Verdana, Arial, Helvetica, sans-serif;font-size: 10.0pt;">
                                                <div>
                                                    <div style="font-family: Verdana, Arial, Helvetica, sans-serif;font-size: 10.0pt;">
                                                        <div>
                                                            <div style="font-family: Verdana, Arial, Helvetica, sans-serif;font-size: 10.0pt;">
                                                                <div>
                                                                    <div style="font-family: Verdana, Arial, Helvetica, sans-serif;font-size: 10.0pt;">
                                                                        <div>
                                                                            <div style="font-family: Verdana, Arial, Helvetica, sans-serif;font-size: 10.0pt;">
                                                                                <div>
                                                                                    <div style="font-family: Verdana, Arial, Helvetica, sans-serif;font-size: 10.0pt;">
                                                                                        <div>
                                                                                            <div style="font-family: Verdana, Arial, Helvetica, sans-serif;font-size: 10.0pt;">
                                                                                                <div style="line-height: 1.5;">
                                                                                                    <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                                                                                                        Dear {},
                                                                                                    </span>
                                                                                                    <br>
                                                                                                </div>
                                                                                                <div style="line-height: 1.5;">
                                                                                                    <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                                                                                                        WELCOME TO TECKAT STUDENT INTERN PARTNER
                                                                                                        <span class="size" style="font-size:16px">
                                                                                                            &nbsp;2
                                                                                                        </span>
                                                                                                    </span>
                                                                                                    <span class="font" style="font-family:serif, sans-serif">
                                                                                                        <span class="size" style="font-size:16px">
                                                                                                            .0
                                                                                                        </span>
                                                                                                    </span>
                                                                                                    <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                                                                                                    </span>
                                                                                                    <br>
                                                                                                </div>
                                                                                                <div>
                                                                                                    <br>
                                                                                                </div>
                                                                                                <div style="line-height: 1.5;">
                                                                                                    <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                                                                                                        <span class="colour" style="color:rgb(0, 0, 153)">
                                                                                                            This time you have all the opportunities to earn huge incentives, rewards, Teckat t-shirts, special certifications and many more.
                                                                                                        </span>
                                                                                                    </span>
                                                                                                    <br>
                                                                                                </div>
                                                                                                <div style="line-height: 1.5;">
                                                                                                    <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                                                                                                        <span class="colour" style="color:rgb(0, 0, 153)">
                                                                                                            This is your second target that you have to achieve.
                                                                                                        </span>
                                                                                                    </span>
                                                                                                    <br>
                                                                                                </div>
                                                                                                <div style="line-height: 1.5;">
                                                                                                    <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                                                                                                        <span class="colour" style="color:rgb(0, 0, 153)">
                                                                                                            This is all about workshop contest organised by Teckat on various technologies and marketing fields.
                                                                                                        </span>
                                                                                                    </span>
                                                                                                    <br>
                                                                                                </div>
                                                                                                <div>
                                                                                                    <br>
                                                                                                </div>
                                                                                                <div>
                                                                                                    <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                                                                                                        <b>
                                                                                                            <span class="size" style="font-size:10.6667px">
                                                                                                                DURATION OF THE CONTEST&nbsp;
                                                                                                            </span>
                                                                                                            -&nbsp;
                                                                                                        </b>
                                                                                                        From
                                                                                                        <b>
                                                                                                            Today
                                                                                                        </b>
                                                                                                        till&nbsp;&nbsp;
                                                                                                    </span>
                                                                                                    <span class="size" style="font-size: 16px">
                                                                                                        <span class="font" style="font-family: serif, sans-serif;">
                                                                                                            <b>
                                                                                                                21&nbsp;st
                                                                                                            </b>
                                                                                                        </span>
                                                                                                    </span>
                                                                                                    <b>
                                                                                                        <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                                                                                                            &nbsp;August,
                                                                                                            <span class="size" style="font-size:16px">
                                                                                                                2020
                                                                                                            </span>
                                                                                                            (
                                                                                                        </span>
                                                                                                        <span class="font" style="font-family:serif, sans-serif">
                                                                                                            <span class="size" style="font-size:16px">
                                                                                                                12
                                                                                                            </span>
                                                                                                        </span>
                                                                                                        <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                                                                                                            Midnight)
                                                                                                        </span>
                                                                                                    </b>
                                                                                                    <br>
                                                                                                </div>
                                                                                                <div>
                                                                                                    <br>
                                                                                                </div>
                                                                                                <div>
                                                                                                    <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                                                                                                        <b>
                                                                                                            <span class="size" style="font-size:16px">
                                                                                                                <span class="colour" style="color:rgb(0, 0, 153)">
                                                                                                                    <u>
                                                                                                                        What shall you do?
                                                                                                                    </u>
                                                                                                                </span>
                                                                                                            </span>
                                                                                                        </b>
                                                                                                    </span>
                                                                                                    <br>
                                                                                                </div>
                                                                                                <ul dir="ltr">
                                                                                                    <li>
                                                                                                        <span>
                                                                                                            <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                                                                                                                <span class="colour" style="color:rgb(204, 0, 0)">
                                                                                                                    You simply have to circulate it among your friends and colleagues through WhatsApp, Facebook, Instagram, to various groups, etc….
                                                                                                                </span>
                                                                                                            </span>
                                                                                                        </span>
                                                                                                        <br>
                                                                                                    </li>
                                                                                                </ul>
                                                                                                <div>
                                                                                                    <br>
                                                                                                </div>
                                                                                                <div>
                                                                                                    <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                                                                                                        <b>
                                                                                                            <span class="size" style="font-size:16px">
                                                                                                                <span class="colour" style="color:rgb(0, 0, 153)">
                                                                                                                    <u>
                                                                                                                        What will you get ?
                                                                                                                    </u>
                                                                                                                </span>
                                                                                                            </span>
                                                                                                        </b>
                                                                                                    </span>
                                                                                                    <br>
                                                                                                </div>
                                                                                                <ul dir="ltr">
                                                                                                    <li>
                                                                                                        <span>
                                                                                                            <span class="colour" style="color:rgb(204, 0, 0)">
                                                                                                                <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                                                                                                                    Every time your friend registers for any of the courses- you will add an incentive of
                                                                                                                </span>
                                                                                                                <span class="font" style="font-family:serif, sans-serif">
                                                                                                                    15%
                                                                                                                </span>
                                                                                                                <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                                                                                                                    &nbsp;on each successful enrollment.
                                                                                                                </span>
                                                                                                            </span>
                                                                                                            <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                                                                                                            </span>
                                                                                                        </span>
                                                                                                        <br>
                                                                                                    </li>
                                                                                                </ul>
                                                                                                <div>
                                                                                                    <br>
                                                                                                </div>
                                                                                                <div>
                                                                                                    <span class="font" style="font-family:serif, sans-serif">
                                                                                                        <b>
                                                                                                            1
                                                                                                        </b>
                                                                                                    </span>
                                                                                                    <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                                                                                                        <b>
                                                                                                            .
                                                                                                        </b>
                                                                                                        You can share the content below (
                                                                                                        <b>
                                                                                                            just copy and paste the share part
                                                                                                        </b>
                                                                                                        ) to your friends and colleagues through WhatsApp, Facebook and other mediums. Encourage them to enroll in the courses they want to.
                                                                                                    </span>
                                                                                                    <br>
                                                                                                </div>
                                                                                                <div>
                                                                                                    <br>
                                                                                                </div>
                                                                                                <div>
                                                                                                    <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                                                                                                        <b>
                                                                                                            Share (Copy and Paste )
                                                                                                        </b>
                                                                                                    </span>
                                                                                                    <br>
                                                                                                </div>
                                                                                                <div>
                                                                                                    ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                                    <br>
                                                                                                </div>
                                                                                                <div style="line-height: 1.5;">
                                                                                                    <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                                                                                                        *Lock down can be useful and Skillful for Learners and Achievers, grab the opportunity to learn in the live sessions for anything you enroll for-*&nbsp;
                                                                                                    </span>
                                                                                                    <br>
                                                                                                </div>
                                                                                                <div style="line-height: 1.5;">
                                                                                                    <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                                                                                                        Enroll yourself in different *WORKSHOPS*, *WEBINARS* and *INTERNSHIP* at Teckat in the field of *ENGINEERING*, *TECHNOLOGY*, *MARKETING*, *DESIGNING*, *DEVELOPMENT* at Teckat Webinar Series-
                                                                                                    </span>
                                                                                                    <span class="font" style="font-family:serif, sans-serif">
                                                                                                        3.0.
                                                                                                    </span>
                                                                                                    <br>
                                                                                                </div>
                                                                                                <div style="line-height: 1.5;">
                                                                                                    *What You Get?*
                                                                                                    <br>
                                                                                                </div>
                                                                                                <div style="line-height: 1.5;">
                                                                                                    1. Live Session throughout the Webinar
                                                                                                    <br>
                                                                                                </div>
                                                                                                <div style="line-height: 1.5;">
                                                                                                    2. Recorded link of each session- lifetime access
                                                                                                    <br>
                                                                                                </div>
                                                                                                <div style="line-height: 1.5;">
                                                                                                    3. ISO Certification- Get ISO Certification
                                                                                                    <br>
                                                                                                </div>
                                                                                                <div style="line-height: 1.5;">
                                                                                                    4. Doubt Sessions- 15 minutes before each session and in mid of the session.
                                                                                                    <br>
                                                                                                </div>
                                                                                                <div style="line-height: 1.5;">
                                                                                                    5. Live projects implementation - Complete guidance from Scratch.
                                                                                                    <br>
                                                                                                </div>
                                                                                                <div style="line-height: 1.5;">
                                                                                                    *Just at Rs 149/-*
                                                                                                    <br>
                                                                                                </div>
                                                                                                <div style="line-height: 1.5;">
                                                                                                    <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                                                                                                        HERE IS THE LINK TO REGISTER IN ANY OF THE WEBINAR YOU WANT TO -
                                                                                                    </span>
                                                                                                    <br>
                                                                                                </div>
                                                                                                <div style="line-height: 1.5;">
                                                                                                    <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                                                                                                        *Link to Register*- {}
                                                                                                    </span>
                                                                                                    <br>
                                                                                                </div>
                                                                                                <div>
                                                                                                    <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                                                                                                        -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                                    </span>
                                                                                                    <br>
                                                                                                </div>
                                                                                                <div>
                                                                                                    <br>
                                                                                                </div>
                                                                                                <div>
                                                                                                    <br>
                                                                                                </div>
                                                                                                <div>
                                                                                                    <span class="font" style="font-family:serif, sans-serif">
                                                                                                        <b>
                                                                                                            2
                                                                                                        </b>
                                                                                                    </span>
                                                                                                    <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                                                                                                        <b>
                                                                                                            .
                                                                                                        </b>
                                                                                                        &nbsp; You can also share the details directly on WhatsApp
                                                                                                    </span>
                                                                                                    <br>
                                                                                                </div>
                                                                                                <div>
                                                                                                    <div>
                                                                                                        <br>
                                                                                                    </div>
                                                                                                    <div>
                                                                                                        &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
                                                                                                        <a style="background-color: rgb(37,211,102);border: 1.0px solid rgb(18,140,126);border-radius: 4.0px;color: rgb(255,255,255);display: inline-block;font-family: sans-serif;font-size: 13.0px;font-weight: bold;line-height: 40.0px;text-align: center;text-decoration: none;width: 200.0px;" href="https://wa.me/?text=%2ALock%20down%20can%20be%20useful%20and%20Skillful%20for%20Learners%20and%20Achievers%2C%20grab%20the%20opportunity%20to%20learn%20in%20the%20live%20sessions%20for%20anything%20you%20enroll%20for-%2A%C2%A0%0A%0AEnroll%20yourself%20in%20different%20%2AWORKSHOPS%2A%2C%20%2AWEBINARS%2A%20and%20%2AINTERNSHIP%2A%20at%20Teckat%20in%20the%20field%20of%20%2AENGINEERING%2A%2C%20%2ATECHNOLOGY%2A%2C%20%2AMARKETING%2A%2C%20%2ADESIGNING%2A%2C%20%2ADEVELOPMENT%2A%20at%20Teckat%20Webinar%20Series-%203.0.%0A%0A%2AWhat%20You%20Get%3F%2A%0A%0A1.%20Live%20Session%20throughout%20the%20Webinar%0A%0A2.%20Recorded%20link%20of%20each%20session-%20lifetime%20access%0A%0A3.%20ISO%20Certification-%20Get%20ISO%20Certification%0A%0A4.%20Doubt%20Sessions-%2015%20minutes%20before%20each%20session%20and%20in%20mid%20of%20the%20session.%0A%0A5.%20Live%20projects%20implementation%20-%20Complete%20guidance%20from%20Scratch.%0A%0A%2AJust%20at%20Rs%20149%2F-%2A%0A%0AHERE%20IS%20THE%20LINK%20TO%20REGISTER%20IN%20ANY%20OF%20THE%20WEBINAR%20YOU%20WANT%20TO%20-%0A%0A%2ALink%20to%20Register%2A-%C2%A0%C2%A0{}%0A" target="_blank">
                                                                                                            Share on WhatsApp
                                                                                                        </a>
                                                                                                        <br>
                                                                                                    </div>
                                                                                                </div>
                                                                                                <div>
                                                                                                    &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
                                                                                                    <br>
                                                                                                </div>
                                                                                                <div>
                                                                                                    <br>
                                                                                                </div>
                                                                                                <div>
                                                                                                    <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                                                                                                        We will intimate you with the incentives earned by you in the end of contest through mail.
                                                                                                    </span>
                                                                                                    <br>
                                                                                                </div>
                                                                                                <div>
                                                                                                    <br>
                                                                                                </div>
                                                                                            </div>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div>
                                        <br>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div>
        <div>
            <table cellpadding="0" cellspacing="0" class="ng-scope" style="box-sizing: border-box; border-spacing: 0px; border-collapse: collapse; background-color: rgb(255, 255, 255); color: rgb(68, 68, 68); font-style: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; width: 525px; font-size: 11pt; font-family: Arial, sans-serif">
                <tbody style="box-sizing: border-box">
                    <tr style="box-sizing: border-box">
                        <td width="125" valign="top" rowspan="6" class="ng-scope" style="box-sizing: border-box; padding: 0px 10px 0px 0px; font-size: 10pt; font-family: Arial, sans-serif; border-right: 1px solid rgb(251, 99, 3); width: 125px; vertical-align: top">
                            <br>
                        </td>
                        <td style="box-sizing: border-box; padding: 0px 0px 0px 10px">
                            <table cellpadding="0" cellspacing="0" style="box-sizing: border-box; border-spacing: 0px; border-collapse: collapse; background-color: transparent">
                                <tbody style="box-sizing: border-box">
                                    <tr style="box-sizing: border-box">
                                        <td valign="top" style="box-sizing: border-box; padding: 0px 0px 5px 10px; font-size: 10pt; color: rgb(0, 121, 172); font-family: Arial, sans-serif; width: 400px; vertical-align: top">
                                            THANKS &amp; REGARDS
                                            <br>
                                        </td>
                                    </tr>
                                    <tr style="box-sizing: border-box">
                                        <td valign="top" style="box-sizing: border-box; padding: 5px 0px 5px 10px; font-size: 10pt; color: rgb(68, 68, 68); font-family: Arial, sans-serif; vertical-align: top; line-height: 17px">
                                            <span class="ng-scope" style="box-sizing: border-box">
                                                <span style="color: rgb(251, 99, 3); box-sizing: border-box;" class="colour">
                                                    <b>
                                                        a:
                                                        <span>
                                                            &nbsp;
                                                        </span>
                                                    </b>
                                                </span>
                                                <span style="color:rgb(0, 0, 0)" class="colour">
                                                    <span style="font-family:Arial, sans-serif" class="font">
                                                        <span style="font-size: 10pt; box-sizing: border-box;" class="size">
                                                            Teckat Services Private Limited
                                                        </span>
                                                    </span>
                                                </span>
                                                <span>
                                                    &nbsp;
                                                </span>
                                                <span style="color:rgb(0, 0, 0)" class="colour">
                                                    <span style="font-family:Arial, sans-serif" class="font">
                                                        <span style="font-size: 10pt; box-sizing: border-box;" class="size">
                                                            <span class="ng-scope" style="box-sizing: border-box">
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
                                                <span style="color:rgb(0, 0, 0)" class="colour">
                                                    <span style="font-family:Arial, sans-serif" class="font">
                                                        <span style="font-size: 10pt; box-sizing: border-box;" class="size">
                                                            <span class="ng-scope" style="box-sizing: border-box">
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
                                                <span style="color: rgb(251, 99, 3); box-sizing: border-box;" class="colour">
                                                    <b>
                                                        e:
                                                    </b>
                                                </span>
                                                <span style="color:rgb(0, 0, 0)" class="colour">
                                                    <span style="font-family:Arial, sans-serif" class="font">
                                                        <span style="font-size: 10pt; box-sizing: border-box;" class="size">
                                                            <span>
                                                                &nbsp;
                                                            </span>
                                                            <a href="mailto:support@teckat.com" target="_blank">
                                                                support@teckat.com
                                                            </a>
                                                        </span>
                                                    </span>
                                                </span>
                                            </span>
                                            <span>
                                                &nbsp;
                                            </span>
                                            <span class="ng-scope" style="box-sizing: border-box">
                                                <span class="ng-scope" style="box-sizing: border-box">
                                                    |
                                                    <span>
                                                        &nbsp;
                                                    </span>
                                                </span>
                                                <span style="color: rgb(251, 99, 3); box-sizing: border-box;" class="colour">
                                                    <b>
                                                        w:
                                                    </b>
                                                </span>
                                                <a style="box-sizing: border-box; background-color: transparent; color: rgb(51, 122, 183); text-decoration: none" href="http://teckat.com/" target="_blank">
                                                    <span style="color:rgb(0, 0, 0)" class="colour">
                                                        <span style="font-family:Arial, sans-serif" class="font">
                                                            <span style="font-size: 10pt; box-sizing: border-box;" class="size">
                                                                <span>
                                                                    &nbsp;
                                                                </span>
                                                                teckat.com
                                                            </span>
                                                        </span>
                                                    </span>
                                                </a>
                                                <br style="box-sizing: border-box">
                                                <span style="color: rgb(251, 99, 3); box-sizing: border-box;" class="colour">
                                                    <b>
                                                        m:
                                                    </b>
                                                </span>
                                                <span style="color:rgb(0, 0, 0)" class="colour">
                                                    <span style="font-family:Arial, sans-serif" class="font">
                                                        <span style="font-size: 10pt; box-sizing: border-box;" class="size">
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
                                    <tr class="ng-scope" style="box-sizing: border-box">
                                        <td valign="bottom" style="box-sizing: border-box; padding: 5px 0px 0px 10px; font-size: 10pt; font-family: Arial, sans-serif; vertical-align: bottom">
                                            <span class="ng-scope" style="box-sizing: border-box">
                                                <a style="box-sizing: border-box; background-color: transparent; color: rgb(51, 122, 183); text-decoration: none" href="https://www.facebook.com/in.teckat/" target="_blank">
                                                    <img height="19" border="0" width="19" alt="facebook icon" src="https://codetwocdn.azureedge.net/images/mail-signatures/generator-dm/bease-fox/fb.png" style="box-sizing: border-box; border: 0px; vertical-align: middle; height: 19px; width: 19px">
                                                </a>
                                                &nbsp;
                                                <a style="box-sizing: border-box; background-color: transparent; color: rgb(51, 122, 183); text-decoration: none" href="https://www.linkedin.com/company/teckat-service-pvt-ltd/?viewAsMember=true" target="_blank">
                                                    <img height="19" border="0" width="19" alt="linkedin icon" src="https://codetwocdn.azureedge.net/images/mail-signatures/generator-dm/bease-fox/ln.png" style="box-sizing: border-box; border: 0px; vertical-align: middle; height: 19px; width: 19px">
                                                </a>
                                                &nbsp;
                                                <a style="box-sizing: border-box; background-color: transparent; color: rgb(51, 122, 183); text-decoration: none" href="https://www.instagram.com/india.teckat/" target="_blank">
                                                    <img height="19" border="0" width="19" alt="instagram icon" src="https://codetwocdn.azureedge.net/images/mail-signatures/generator-dm/bease-fox/it.png" style="box-sizing: border-box; border: 0px; vertical-align: middle; height: 19px; width: 19px">
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
    <div style="font-family: Verdana, Arial, Helvetica, sans-serif;font-size: 10.0pt;">
        <div>
            <div style="font-family: Verdana, Arial, Helvetica, sans-serif;font-size: 10.0pt;">
                <div>
                    <div style="font-family: Verdana, Arial, Helvetica, sans-serif;font-size: 10.0pt;">
                        <div>
                            <div style="font-family: Verdana, Arial, Helvetica, sans-serif;font-size: 10.0pt;">
                                <div id="x_1542524513Zm-_Id_-Sgn">
                                    <div style="font-family: Verdana, Arial, Helvetica, sans-serif;font-size: 10.0pt;">
                                        <div>
                                            <div style="font-family: Verdana, Arial, Helvetica, sans-serif;font-size: 10.0pt;">
                                                <div>
                                                    <div style="font-family: Verdana, Arial, Helvetica, sans-serif;font-size: 10.0pt;">
                                                        <div>
                                                            <div style="font-family: Verdana, Arial, Helvetica, sans-serif;font-size: 10.0pt;">
                                                                <div>
                                                                    <div style="font-family: Verdana, Arial, Helvetica, sans-serif;font-size: 10.0pt;">
                                                                        <div>
                                                                            <div style="font-family: Verdana, Arial, Helvetica, sans-serif;font-size: 10.0pt;">
                                                                                <div>
                                                                                    <div style="font-family: Verdana, Arial, Helvetica, sans-serif;font-size: 10.0pt;">
                                                                                        <div>
                                                                                            <div>
                                                                                                <br>
                                                                                            </div>
                                                                                        </div>
                                                                                        <div>
                                                                                            <br>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                                <div>
                                                                                    <br>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                        <div>
                                                                            <br>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div>
                                                                    <br>
                                                                </div>
                                                            </div>
                                                        </div>
                                                        <div>
                                                            <br>
                                                        </div>
                                                    </div>
                                                </div>
                                                <div>
                                                    <br>
                                                </div>
                                            </div>
                                        </div>
                                        <div>
                                            <br>
                                        </div>
                                    </div>
                                </div>
                                <div>
                                    <br>
                                </div>
                            </div>
                        </div>
                        <div>
                            <br>
                        </div>
                    </div>
                </div>
                <div>
                    <br>
                </div>
            </div>
        </div>
        <div>
            <br>
        </div>
    </div>
</div>
<div>
    <br>
</div>



  </body>
</html>

        '''.format(separate[0], strLink2, strLink2)

            elif(generatePaymentLink == 0):

                # html

                html = '''

<html>
  <head></head>
  <body>



<div>
    <div style="font-family: Verdana, Arial, Helvetica, sans-serif;font-size: 10.0pt;">
        <div>
            Dear {},
            <br>
        </div>
        <div>
            We would like to intimate you about your incentive amount which is not up to the mark.
            <br>
        </div>
        <div>
            Therefore, we would like to help you regarding ways to earn amount.
            <br>
        </div>
        <div>
            Your incentive seems to be Rs 0/- in the first bonus week.
            <br>
        </div>
        <div>
            Kindly take the chance to earn incentive and get certified to for this Internship.
            <br>
        </div>
        <div>
            <br>
        </div>
        <div>
            You can take the opportunity in the upcoming bonus week/hour/days and get in the count of Top-10.
            <br>
        </div>
        <div>
            It would be great to see you in the counting.
            <br>
        </div>
        <div>
            <br>
        </div>
        <div>
            All the best!
            <br>
        </div>
        <div>
            You may mail us for any queries at
            <a href="mailto:support@teckat.com" target="_blank">
                support@teckat.com
            </a>
            <br>
        </div>
        <div>
            <br>
        </div>
        <div id="x_549683166Zm-_Id_-Sgn">
            <div>
                <br>
            </div>
        </div>
    </div>
</div>
<div>
    <br>
</div>
<div id="Zm-_Id_-Sgn" data-zbluepencil-ignore="true">
    <div>
        <div>
            <table cellpadding="0" cellspacing="0" class="ng-scope" style="box-sizing: border-box; border-spacing: 0px; border-collapse: collapse; background-color: rgb(255, 255, 255); color: rgb(68, 68, 68); font-style: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; width: 525px; font-size: 11pt; font-family: Arial, sans-serif">
                <tbody style="box-sizing: border-box">
                    <tr style="box-sizing: border-box">
                        <td width="125" valign="top" rowspan="6" class="ng-scope" style="box-sizing: border-box; padding: 0px 10px 0px 0px; font-size: 10pt; font-family: Arial, sans-serif; border-right: 1px solid rgb(251, 99, 3); width: 125px; vertical-align: top">
                            <br>
                        </td>
                        <td style="box-sizing: border-box; padding: 0px 0px 0px 10px">
                            <table cellpadding="0" cellspacing="0" style="box-sizing: border-box; border-spacing: 0px; border-collapse: collapse; background-color: transparent">
                                <tbody style="box-sizing: border-box">
                                    <tr style="box-sizing: border-box">
                                        <td valign="top" style="box-sizing: border-box; padding: 0px 0px 5px 10px; font-size: 10pt; color: rgb(0, 121, 172); font-family: Arial, sans-serif; width: 400px; vertical-align: top">
                                            THANKS &amp; REGARDS
                                            <br>
                                        </td>
                                    </tr>
                                    <tr style="box-sizing: border-box">
                                        <td valign="top" style="box-sizing: border-box; padding: 5px 0px 5px 10px; font-size: 10pt; color: rgb(68, 68, 68); font-family: Arial, sans-serif; vertical-align: top; line-height: 17px">
                                            <span class="ng-scope" style="box-sizing: border-box">
                                                <span style="color: rgb(251, 99, 3); box-sizing: border-box;" class="colour">
                                                    <b>
                                                        a:
                                                        <span>
                                                            &nbsp;
                                                        </span>
                                                    </b>
                                                </span>
                                                <span style="color:rgb(0, 0, 0)" class="colour">
                                                    <span style="font-family:Arial, sans-serif" class="font">
                                                        <span style="font-size: 10pt; box-sizing: border-box;" class="size">
                                                            Teckat Services Private Limited
                                                        </span>
                                                    </span>
                                                </span>
                                                <span>
                                                    &nbsp;
                                                </span>
                                                <span style="color:rgb(0, 0, 0)" class="colour">
                                                    <span style="font-family:Arial, sans-serif" class="font">
                                                        <span style="font-size: 10pt; box-sizing: border-box;" class="size">
                                                            <span class="ng-scope" style="box-sizing: border-box">
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
                                                <span style="color:rgb(0, 0, 0)" class="colour">
                                                    <span style="font-family:Arial, sans-serif" class="font">
                                                        <span style="font-size: 10pt; box-sizing: border-box;" class="size">
                                                            <span class="ng-scope" style="box-sizing: border-box">
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
                                                <span style="color: rgb(251, 99, 3); box-sizing: border-box;" class="colour">
                                                    <b>
                                                        e:
                                                    </b>
                                                </span>
                                                <span style="color:rgb(0, 0, 0)" class="colour">
                                                    <span style="font-family:Arial, sans-serif" class="font">
                                                        <span style="font-size: 10pt; box-sizing: border-box;" class="size">
                                                            <span>
                                                                &nbsp;
                                                            </span>
                                                            <a href="mailto:support@teckat.com" target="_blank">
                                                                support@teckat.com
                                                            </a>
                                                        </span>
                                                    </span>
                                                </span>
                                            </span>
                                            <span>
                                                &nbsp;
                                            </span>
                                            <span class="ng-scope" style="box-sizing: border-box">
                                                <span class="ng-scope" style="box-sizing: border-box">
                                                    |
                                                    <span>
                                                        &nbsp;
                                                    </span>
                                                </span>
                                                <span style="color: rgb(251, 99, 3); box-sizing: border-box;" class="colour">
                                                    <b>
                                                        w:
                                                    </b>
                                                </span>
                                                <a style="box-sizing: border-box; background-color: transparent; color: rgb(51, 122, 183); text-decoration: none" href="http://teckat.com/" target="_blank">
                                                    <span style="color:rgb(0, 0, 0)" class="colour">
                                                        <span style="font-family:Arial, sans-serif" class="font">
                                                            <span style="font-size: 10pt; box-sizing: border-box;" class="size">
                                                                <span>
                                                                    &nbsp;
                                                                </span>
                                                                teckat.com
                                                            </span>
                                                        </span>
                                                    </span>
                                                </a>
                                                <br style="box-sizing: border-box">
                                                <span style="color: rgb(251, 99, 3); box-sizing: border-box;" class="colour">
                                                    <b>
                                                        m:
                                                    </b>
                                                </span>
                                                <span style="color:rgb(0, 0, 0)" class="colour">
                                                    <span style="font-family:Arial, sans-serif" class="font">
                                                        <span style="font-size: 10pt; box-sizing: border-box;" class="size">
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
                                    <tr class="ng-scope" style="box-sizing: border-box">
                                        <td valign="bottom" style="box-sizing: border-box; padding: 5px 0px 0px 10px; font-size: 10pt; font-family: Arial, sans-serif; vertical-align: bottom">
                                            <span class="ng-scope" style="box-sizing: border-box">
                                                <a style="box-sizing: border-box; background-color: transparent; color: rgb(51, 122, 183); text-decoration: none" href="https://www.facebook.com/in.teckat/" target="_blank">
                                                    <img height="19" border="0" width="19" alt="facebook icon" src="https://codetwocdn.azureedge.net/images/mail-signatures/generator-dm/bease-fox/fb.png" style="box-sizing: border-box; border: 0px; vertical-align: middle; height: 19px; width: 19px">
                                                </a>
                                                &nbsp;
                                                <a style="box-sizing: border-box; background-color: transparent; color: rgb(51, 122, 183); text-decoration: none" href="https://www.linkedin.com/company/teckat-service-pvt-ltd/?viewAsMember=true" target="_blank">
                                                    <img height="19" border="0" width="19" alt="linkedin icon" src="https://codetwocdn.azureedge.net/images/mail-signatures/generator-dm/bease-fox/ln.png" style="box-sizing: border-box; border: 0px; vertical-align: middle; height: 19px; width: 19px">
                                                </a>
                                                &nbsp;
                                                <a style="box-sizing: border-box; background-color: transparent; color: rgb(51, 122, 183); text-decoration: none" href="https://www.instagram.com/india.teckat/" target="_blank">
                                                    <img height="19" border="0" width="19" alt="instagram icon" src="https://codetwocdn.azureedge.net/images/mail-signatures/generator-dm/bease-fox/it.png" style="box-sizing: border-box; border: 0px; vertical-align: middle; height: 19px; width: 19px">
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
        <div>
            <br>
        </div>
        <div>
            <br>
        </div>
    </div>
</div>
<div>
    <br>
</div>



  </body>
</html>

        '''.format(separate[0])

        if(tsipStatus == 'T-SIP 3.0'):

            if(generatePaymentLink == 1):
                print(separate)
                strLink1 = link[0][0]+'?referral=TSIP03' + \
                    separate[0][0:1]+separate[1][0:1]+str(tsipId[i])
                strLink2 = link[0][1]+'?referral=TSIP03' + \
                    separate[0][0:1]+separate[1][0:1]+str(tsipId[i])
                strLink3 = link[0][2]+'?referral=TSIP03' + \
                    separate[0][0:1]+separate[1][0:1]+str(tsipId[i])
                print(strLink1)
                print(strLink2)
                print(strLink3)

            #  mail status check
            if(mailStatus == 'Thank you for submitting application'):
                html = '''

<html>
  <head></head>
  <body>



<div>
    <div style="font-family: Verdana, Arial, Helvetica, sans-serif;font-size: 10.0pt;">
        <p style="line-height: 1.38;margin-top: 0.0pt;margin-bottom: 0.0pt;" dir="ltr">
            <span class="size" style="font-size:13.3333px">
                <br>
            </span>
        </p>
        <div dir="ltr">
            <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                <span class="size" style="font-size:13.3333px">
                    Dear {}
                    <br>
                </span>
            </span>
        </div>
        <div dir="ltr">
            <span class="highlight" style="background-color:transparent">
                <span class="colour" style="color:rgb(0, 0, 0)">
                    <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                        <span class="size" style="font-size:13.3333px">
                            We hereby notify about your successful submission of application form at “
                        </span>
                    </span>
                </span>
                <span class="highlight" style="background-color:rgb(255, 255, 255)">
                    <b>
                        <span class="colour" style="color:rgb(0, 0, 0)">
                            <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                                <span class="size" style="font-size:13.3333px">
                                    TECKAT STUDENT INTERN PARTNER- 3.
                                </span>
                            </span>
                        </span>
                    </b>
                </span>
            </span>
            <b>
                <span class="highlight" style="background-color:rgb(255, 255, 255)">
                    <span class="colour" style="color:rgb(0, 0, 0)">
                        <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                            <span class="size" style="font-size:13.3333px">
                                0
                            </span>
                        </span>
                    </span>
                </span>
            </b>
            <span class="colour" style="color:rgb(0, 0, 0)">
                <span class="highlight" style="background-color:transparent">
                    <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                        <span class="size" style="font-size:13.3333px">
                            ”.
                        </span>
                    </span>
                </span>
            </span>
            <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                <span class="size" style="font-size:13.3333px">
                    <br>
                </span>
            </span>
        </div>
        <p style="line-height: 1.38;margin-top: 0.0pt;margin-bottom: 0.0pt;" dir="ltr">
            <span class="highlight" style="background-color:transparent">
                <span class="colour" style="color:rgb(0, 0, 0)">
                    <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                        <span class="size" style="font-size:13.3333px">
                            We will update you soon with the results.
                        </span>
                    </span>
                </span>
            </span>
            <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                <span class="size" style="font-size:13.3333px">
                    <br>
                </span>
            </span>
        </p>
        <div>
            <span class="size" style="font-size:13.3333px">
                <br>
            </span>
        </div>
        <div>
            <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                <span class="size" style="font-size:13.3333px">
                    <br>
                </span>
            </span>
        </div>
        <p style="line-height: 1.38;margin-top: 0.0pt;margin-bottom: 0.0pt;" dir="ltr">
            <span class="highlight" style="background-color:transparent">
                <span class="colour" style="color:rgb(255, 0, 0)">
                    <b>
                        <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                            <span class="size" style="font-size:13.3333px">
                                IMPORTANT
                            </span>
                        </span>
                    </b>
                </span>
                <span class="colour" style="color:rgb(204, 0, 0)">
                    <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                        <span class="size" style="font-size:13.3333px">
                            -
                        </span>
                    </span>
                </span>
                <span class="colour" style="color:rgb(0, 0, 0)">
                    <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                        <span class="size" style="font-size:13.3333px">
                            Your chances to be an intern at T-SIP increases if you enroll 10 participants to T-SIP 3.0 through your referral code.
                        </span>
                    </span>
                </span>
            </span>
            <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                <span class="size" style="font-size:13.3333px">
                    <br>
                </span>
            </span>
        </p>
        <p style="line-height: 1.38;margin-top: 0.0pt;margin-bottom: 0.0pt;" dir="ltr">
            <span class="highlight" style="background-color:transparent">
                <span class="colour" style="color:rgb(0, 0, 0)">
                    <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                        <span class="size" style="font-size:13.3333px">
                            Win the challenge and this will get more ease during your internship.
                        </span>
                    </span>
                </span>
            </span>
            <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                <span class="size" style="font-size:13.3333px">
                    <br>
                </span>
            </span>
        </p>
        <div dir="ltr">
            <span class="size" style="font-size:13.3333px">
                <br>
            </span>
        </div>
        <div dir="ltr">
            <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                <span class="size" style="font-size:13.3333px">
                    <br>
                </span>
            </span>
        </div>
        <p style="line-height: 1.38;margin-top: 0.0pt;margin-bottom: 0.0pt;" dir="ltr">
            <span class="highlight" style="background-color:transparent">
                <b>
                    <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                        <span class="size" style="font-size:13.3333px">
                            <span class="colour" style="color:rgb(0, 0, 0)">
                                For any further queries- refer
                            </span>
                            <a href="https://teckat.com/faq" target="_blank">
                                <span class="colour" style="color:#0065cc">
                                    FAQ's
                                </span>
                            </a>
                            <span class="colour" style="color:rgb(0, 0, 0)">
                                or mail us at
                            </span>
                        </span>
                        <span class="colour" style="color:rgb(0, 0, 0)">
                        </span>
                    </span>
                    <span class="colour" style="color:rgb(0, 0, 0)">
                    </span>
                </b>
                <span class="colour" style="color:rgb(0, 0, 0)">
                </span>
                <span class="colour" style="color:rgb(204, 0, 0)">
                    <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                        <span class="size" style="font-size:13.3333px">
                            &nbsp;
                        </span>
                    </span>
                </span>
                <span class="colour" style="color:rgb(0, 0, 0)">
                </span>
                <a target="_blank" href="mailto:support@teckat.com">
                    <span class="colour" style="color:rgb(0, 0, 0)">
                    </span>
                    <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                        <span class="colour" style="color:rgb(0, 0, 0)">
                        </span>
                        <span class="size" style="font-size:13.3333px">
                            <span class="colour" style="color:rgb(0, 0, 0)">
                            </span>
                            <span class="colour" style="color:#0065cc">
                                support@teckat.com
                            </span>
                            <span class="colour" style="color:rgb(0, 0, 0)">
                            </span>
                        </span>
                        <span class="colour" style="color:rgb(0, 0, 0)">
                        </span>
                    </span>
                    <span class="colour" style="color:rgb(0, 0, 0)">
                    </span>
                </a>
                <span class="colour" style="color:rgb(0, 0, 0)">
                </span>
            </span>
            <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                <span class="size" style="font-size:13.3333px">
                    <br>
                </span>
            </span>
        </p>
        <div dir="ltr">
            <span class="size" style="font-size:13.3333px">
                <br>
            </span>
        </div>
        <div dir="ltr">
            <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                <span class="size" style="font-size:13.3333px">
                    <br>
                </span>
            </span>
        </div>
        <p style="line-height: 1.38;margin-top: 0.0pt;margin-bottom: 0.0pt;" dir="ltr">
            <span class="highlight" style="background-color:transparent">
                <b>
                    <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                        <span class="size" style="font-size:13.3333px">
                            <span class="colour" style="color:rgb(0, 0, 102)">
                                HIGHLIGHTS THAT WILL HELP YOU?
                            </span>
                        </span>
                    </span>
                </b>
            </span>
            <span class="size" style="font-size:14.6667px">
                <br>
            </span>
        </p>
        <div dir="ltr">
            <span class="highlight" style="background-color:transparent">
                <b>
                    <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                    </span>
                </b>
            </span>
            <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                <span class="size" style="font-size:14.6667px">
                    <br>
                </span>
            </span>
        </div>
        <div dir="ltr">
            <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                <span class="size" style="font-size:14.6667px">
                    1.&nbsp; Download the attachment below and do share it along with the content.
                </span>
            </span>
            <br>
        </div>
        <div dir="ltr">
            <span class="colour" style="color:rgb(0, 0, 0)">
                <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                    <span class="size" style="font-size:13.3333px">
                        <br>
                    </span>
                </span>
            </span>
            <span class="highlight" style="background-color:transparent">
                <span class="colour" style="color:rgb(0, 0, 0)">
                    <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                        <span class="size" style="font-size:14.6667px">
                            2.&nbsp; You can share your referral code and use the content below to share among&nbsp; your friends for helping to register.
                        </span>
                    </span>
                </span>
            </span>
            <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                <span class="size" style="font-size:13.3333px">
                    <br>
                </span>
            </span>
        </div>
        <p style="line-height: 1.38;margin-top: 0.0pt;margin-bottom: 0.0pt;" dir="ltr">
            <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                <span class="size" style="font-size:13.3333px">
                    <br>
                </span>
            </span>
        </p>
        <div dir="ltr">
            <b>
                <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                    <span class="size" style="font-size:13.3333px">
                        &nbsp;
                    </span>
                </span>
            </b>
            <br>
        </div>
        <div dir="ltr">
            <b>
                <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                    <span class="size" style="font-size:13.3333px">
                        [COPY AND PASTE THE CONTENT BELOW]
                    </span>
                </span>
            </b>
            <span class="size" style="font-size:13.3333px">
                <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                    <br>
                </span>
            </span>
        </div>
        <div dir="ltr">
            <br>
        </div>
        <div dir="ltr">
            !-------------------------------------------------------------------------------------------------------!
            <br>
        </div>
        <div dir="ltr">
            <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                <span class="size" style="font-size:13.3333px">
                    <br>
                </span>
                <span class="size" style="font-size:12px">
                    Hey, I have just got an internship at TECKAT.
                    <br>
                </span>
            </span>
        </div>
    </div>
    <div>
        <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
            <span class="size" style="font-size:12px">
                The chance to be the face of your campus as a *"Campus Ambassador"* and earn stipend from day 1.
                <br>
            </span>
        </span>
    </div>
</div>
<div>
    <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
        <span class="size" style="font-size:12px">
            *ARE YOU READY TO EXPERIENCE. EXPLORE. EXECUTE* with me? Let's Go
        </span>
        <span class="size" style="font-size:12px">
            <br>
        </span>
    </span>
</div>
<div>
    <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
        <span class="size" style="font-size:12px">
            Enroll yourself to be the part of this super exciting internship.
            <br>
        </span>
    </span>
</div>
<div>
    <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
        <span class="size" style="font-size:12px">
            *Apply Now*. Use my referral code and increase your chance to get selected.
            <br>
        </span>
    </span>
</div>
<div>
    <div style="font-family: Verdana, Arial, Helvetica, sans-serif;font-size: 10.0pt;">
        <div dir="ltr">
            <span class="highlight" style="background-color:transparent">
                <span class="colour" style="color:rgb(0, 0, 0)">
                    <b>
                        <a href="https://teckat.com/tsip-details" target="_blank">
                            <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                                <span class="size" style="font-size:12px">
                                    https://teckat.com/tsip-details
                                </span>
                            </span>
                        </a>
                    </b>
                </span>
            </span>
            <span class="size" style="font-size:12px">
                <br>
            </span>
        </div>
        <div dir="ltr">
            <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                    <span class="size" style="font-size:12px">
                        *REFERRAL CODE:* {}
                    </span>
                    <b>
                        <span class="size" style="font-size:12px">
                            &nbsp;
                        </span>
                    </b>
                    <span class="size" style="font-size:12px">
                    </span>
                </span>
                <span class="size" style="font-size:12px">
                </span>
                <span class="size" style="font-size:12px">
                    <br>
                </span>
            </span>
        </div>
        <div dir="ltr">
            <br>
        </div>
        <div dir="ltr">
            !--------------------------------------------------------------------------------------------------------!
            <br>
        </div>
        <div dir="ltr">
            <div>
                <div>
                    <span class="colour" style="color:rgb(0, 0, 0)">
                        <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                            <span class="size" style="font-size:13.3333px">
                                <br>
                            </span>
                        </span>
                    </span>
                    <span class="highlight" style="background-color:transparent">
                        <span class="colour" style="color:rgb(0, 0, 0)">
                            <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                                <span class="size" style="font-size:14.6667px">
                                    3. Either, you can click on the button below to share the link in whats app.
                                </span>
                                <span class="size" style="font-size:13.3333px">
                                    &nbsp;
                                </span>
                            </span>
                        </span>
                    </span>
                </div>
                <div>
                    <br>
                </div>
                <div>
                    <br>
                </div>
                <div>
                    <a href="https://wa.me/?text=Hey%2C%20I%20have%20just%20got%20an%20internship%20at%20TECKAT.%20%0AThe%20chance%20to%20be%20the%20face%20of%20your%20campus%20as%20a%20%2A%22Campus%20Ambassador%22%2A%20and%20earn%20stipend%20from%20day%201.%0A%2AARE%20YOU%20READY%20TO%20EXPERIENCE.%20EXPLORE.%20EXECUTE%2A%20with%20me%3F%20Let%27s%20Go%0AEnroll%20yourself%20to%20be%20the%20part%20of%20this%20super%20exciting%20internship.%0A%0A%2AApply%20Now%2A.%20Use%20my%20referral%20code%20and%20increase%20your%20chance%20to%20get%20selected.%0Ahttps%3A%2F%2Fteckat.com%2Ftsip-details%0A%0A%2AREFERRAL%20CODE%3A%2A%20{}%0A" style="background-color:#25d366;border:1px solid #128c7e;border-radius:4px;color:#ffffff;display:inline-block;font-family:sans-serif;font-size:13px;font-weight:bold;line-height:40px;text-align:center;text-decoration:none;width:200px;-webkit-text-size-adjust:none;mso-hide:all;">
                        Share on WhatsApp
                    </a>
                    <br>
                </div>
                <div>
                    <br>
                </div>
                <div>
                    <br>
                </div>
            </div>
        </div>
        <p style="line-height: 1.38;margin-top: 0.0pt;margin-bottom: 0.0pt;" dir="ltr">
            <span class="highlight" style="background-color:transparent">
                <span class="colour" style="color:rgb(0, 0, 0)">
                    <b>
                        <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                            <span class="size" style="font-size:13.3333px">
                                Don’t forget to send your referral code in both the ways
                            </span>
                        </span>
                    </b>
                    <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                        <span class="size" style="font-size:13.3333px">
                            .
                        </span>
                    </span>
                </span>
            </span>
            <span class="colour" style="color:rgb(0, 0, 0)">
                <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                    <span class="size" style="font-size:13.3333px">
                        <br>
                    </span>
                </span>
            </span>
        </p>
        <div>
            <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                <span class="size" style="font-size:13.3333px">
                    <br>
                </span>
            </span>
        </div>
        <p style="line-height: 1.38;margin-top: 0.0pt;margin-bottom: 0.0pt;" dir="ltr">
            <span class="highlight" style="background-color:transparent">
                <b>
                    <span class="colour" style="color:rgb(0, 0, 0)">
                        <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                            <span class="size" style="font-size:13.3333px">
                                Wish you all the best!
                            </span>
                        </span>
                    </span>
                </b>
            </span>
            <span class="font" style="font-family:verdana, sans-serif">
                <br>
            </span>
        </p>
        <div>
            <br>
        </div>
        <div>
            <br>
        </div>
        <div>
            <br>
        </div>
    </div>
    <div>
        <table style="box-sizing: border-box; border-spacing: 0px; border-collapse: collapse; background-color: rgb(255, 255, 255); color: rgb(68, 68, 68); font-style: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; width: 525px; font-size: 11pt; font-family: Arial, sans-serif" class="ng-scope" cellspacing="0" cellpadding="0">
            <tbody style="box-sizing: border-box">
                <tr style="box-sizing: border-box">
                    <td style="box-sizing: border-box; padding: 0px 10px 0px 0px; font-size: 10pt; font-family: Arial, sans-serif; border-right: 1px solid rgb(251, 99, 3); width: 125px; vertical-align: top" class="ng-scope" rowspan="6" valign="top" width="125">
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
    </div>
    <div style="font-family: Verdana, Arial, Helvetica, sans-serif;font-size: 10.0pt;">
        <div id="x_-731305221Zm-_Id_-Sgn">
            <div>
                <table style="box-sizing: border-box;border-spacing: 0.0px;border-collapse: collapse;background-color: rgb(255,255,255);color: rgb(68,68,68);font-style: normal;font-weight: 400;letter-spacing: normal;orphans: 2;text-indent: 0.0px;text-transform: none;white-space: normal;widows: 2;word-spacing: 0.0px;width: 525.0px;font-size: 11.0pt;font-family: Arial, sans-serif;" class="x_-731305221ng-scope" cellspacing="0" cellpadding="0">
                    <tbody style="box-sizing: border-box;">
                        <tr style="box-sizing: border-box;">
                            <td style="box-sizing: border-box;padding: 0.0px 0.0px 0.0px 10.0px;">
                                <table style="box-sizing: border-box;border-spacing: 0.0px;border-collapse: collapse;background-color: transparent;" cellspacing="0" cellpadding="0">
                                    <tbody style="box-sizing: border-box;">
                                        <tr style="box-sizing: border-box;" class="x_-731305221ng-scope">
                                            <td style="box-sizing: border-box;padding: 5.0px 0.0px 0.0px 10.0px;font-size: 10.0pt;font-family: Arial, sans-serif;vertical-align: bottom;" valign="bottom">
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
        <div>
            <br>
        </div>
        <div>
            <br>
        </div>
    </div>
    <div>
        <br>
    </div>
</div>
<div>
    <br>
</div>



  </body>
</html>

            '''.format(separate[0], separate[0], separate[0])

            elif(mailStatus == 'application under review'):

                html = '''
<html>
  <head></head>
  <body>


<div>
    <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
        <span class="size" style="font-size: 13.333333333333332px">
            Dear {},
        </span>
        <span class="size" style="font-size: 13.333333333333332px">
            <br>
        </span>
    </span>
</div>
<div>
    <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
        <span class="size" style="font-size: 13.333333333333332px">
            <br>
        </span>
    </span>
</div>
<div>
    <span class="size" style="font-size: 13.333333333333332px">
        <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
            We would like to notify you about the awaited moment of the T-SIP
        </span>
        <span class="font" style="font-family: serif, sans-serif;">
            3.0
        </span>
        <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
            (
        </span>
    </span>
    <span class="colour" style="color:#990000">
        <b>
            <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
                <span class="size" style="font-size: 13.333333333333332px">
                    Results announcement
                </span>
            </span>
        </b>
    </span>
    <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
        <span class="size" style="font-size: 13.333333333333332px">
            )
            <br>
        </span>
    </span>
</div>
<div>
    <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
        <span class="size" style="font-size: 13.333333333333332px">
            <br>
        </span>
    </span>
</div>
<div>
    <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
        <span class="size" style="font-size: 13.333333333333332px">
            Your application is in the review process.
        </span>
        <span class="size" style="font-size: 13.333333333333332px">
            <br>
        </span>
    </span>
</div>
<div>
    <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
        <span class="size" style="font-size: 13.333333333333332px">
            <br>
        </span>
    </span>
</div>
<div>
    <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
        <span class="size" style="font-size: 13.333333333333332px">
            We will declare the results on
        </span>
    </span>
    <b>
        <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
            <span class="size" style="font-size: 13.333333333333332px">
                07 August 2020
            </span>
        </span>
    </b>
    <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
        <span class="size" style="font-size: 13.333333333333332px">
            .
        </span>
        <span class="size" style="font-size: 13.333333333333332px">
            <br>
        </span>
    </span>
</div>
<div>
    <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
        <span class="size" style="font-size: 13.333333333333332px">
            <br>
        </span>
    </span>
</div>
<div>
    <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
        <span class="size" style="font-size: 13.333333333333332px">
            In between, if you find yourself with any such queries refer
        </span>
    </span>
    <b>
        <a href="https://teckat.com/faq" target="_blank">
            <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
                <span class="size" style="font-size: 13.333333333333332px">
                    <span class="colour" style="color:#000066">
                        FAQs
                    </span>
                </span>
            </span>
        </a>
    </b>
    <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
        <span class="size" style="font-size: 13.333333333333332px">
            or mail us at
        </span>
    </span>
    <a target="_blank" href="mailto:support@teckat.com">
        <span class="colour" style="color:#000066">
            <b>
                <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
                    <span class="size" style="font-size: 13.333333333333332px">
                        support@teckat.com
                    </span>
                </span>
            </b>
        </span>
    </a>
    <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
        <span class="size" style="font-size: 13.333333333333332px">
            <br>
        </span>
    </span>
</div>
<div>
    <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
        <span class="size" style="font-size: 13.333333333333332px">
            <br>
        </span>
    </span>
</div>
<div>
    <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
        <span class="size" style="font-size: 13.333333333333332px">
            <br>
        </span>
    </span>
</div>
<div>
    <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
        <span class="size" style="font-size: 13.333333333333332px">
            We wish you a good luck for your results.
        </span>
        <span class="size" style="font-size: 13.333333333333332px">
            <br>
        </span>
    </span>
</div>
<div>
    <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
        <span class="size" style="font-size: 13.333333333333332px">
            <br>
        </span>
    </span>
</div>
<div>
    <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
        <span class="size" style="font-size: 13.333333333333332px">
            All the best!
        </span>
    </span>
</div>
<div>
    <br>
</div>
<div data-zbluepencil-ignore="true" id="Zm-_Id_-Sgn">
    <div>
        <br>
        <br>
        <div>
            <table style="box-sizing: border-box; border-spacing: 0px; border-collapse: collapse; background-color: rgb(255, 255, 255); color: rgb(68, 68, 68); font-style: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; width: 525px; font-size: 11pt; font-family: Arial, sans-serif" class="ng-scope" cellspacing="0" cellpadding="0">
                <tbody style="box-sizing: border-box">
                    <tr style="box-sizing: border-box">
                        <td style="box-sizing: border-box; padding: 0px 10px 0px 0px; font-size: 10pt; font-family: Arial, sans-serif; border-right: 1px solid rgb(251, 99, 3); width: 125px; vertical-align: top" class="ng-scope" rowspan="6" valign="top" width="125">
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
    <div>
        <br>
    </div>
</div>
<br>
<div>
    <br>
</div>


  </body>
</html>
                '''.format(separate[0], separate[0], separate[0])

            elif(mailStatus == 'Result Declaration'):

                html = '''
<html>
  <head></head>
  <body>


<div>
    <div style="font-family: Verdana, Arial, Helvetica, sans-serif;font-size: 10.0pt;">
        <div>
            <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                Dear {},
                <br>
            </span>
        </div>
        <div>
            <span class="colour" style="color:rgb(0, 0, 153)">
                <b>
                    <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                        CONGRATULATIONS! You are selected for T-SIP
                    </span>
                    <span class="font" style="font-family:serif, sans-serif">
                        3.0
                    </span>
                    <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                        Internship.
                    </span>
                </b>
            </span>
            <br>
        </div>
        <div>
            <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                <br>
            </span>
        </div>
        <div>
            <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                We welcome you to Teckat family. Hurray!
            </span>
            <br>
        </div>
        <div>
            <br>
        </div>
        <div>
            <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                GET READY FOR
            </span>
            <span class="font" style="font-family:serif, sans-serif">
                45
            </span>
            <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                DAYS INTERNSHIP AT TECKAT
            </span>
            <br>
        </div>
        <div>
            <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                "
                <span class="colour" style="color:rgb(204, 0, 0)">
                    <b>
                        BE THE FACE OF CAMPUS AND HELP YOUR FRIENDS TO GET THE RIGHT KNOWLEDGE AND SKILLS
                    </b>
                    &nbsp;
                </span>
                "
            </span>
            <br>
        </div>
        <div>
            <br>
        </div>
        <div>
            <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                <b>
                    <u>
                        WHAT YOU GET ONCE YOUR INTERNSHIP IS COMPLETED?
                    </u>
                </b>
            </span>
            <br>
        </div>
        <div>
            <br>
        </div>
        <div>
            <span class="font" style="font-family:serif, sans-serif">
                1.
            </span>
            <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                Incentives (
                <span class="colour" style="color:rgb(0, 0, 102)">
                    Stipend Based
                </span>
                )
            </span>
            <br>
        </div>
        <div>
            <span class="font" style="font-family:serif, sans-serif">
                2
            </span>
            <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                . Special Certifications (
                <span class="colour" style="color:rgb(0, 0, 102)">
                    Performance Based
                </span>
                )
            </span>
            <br>
        </div>
        <div>
            <span class="font" style="font-family:serif, sans-serif">
                3
            </span>
            <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                . Internship Certificate
            </span>
            <br>
        </div>
        <div>
            <span class="font" style="font-family:serif, sans-serif">
                4
            </span>
            <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                . Rewards (
                <span class="colour" style="color:rgb(0, 0, 102)">
                    Performance Based
                </span>
                )
            </span>
            <br>
        </div>
        <div>
            <span class="font" style="font-family:serif, sans-serif">
                5
            </span>
            <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                . Teckat T-Shirt (
                <span class="colour" style="color:rgb(0, 0, 102)">
                    Performance Based
                </span>
                )
            </span>
            <br>
        </div>
        <div>
            <br>
        </div>
        <div>
            <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                <b>
                    INTERNSHIP DURATION:-&nbsp;
                </b>
            </span>
            <span class="font" style="font-family:serif, sans-serif">
                <b>
                    <span class="size" style="font-size:16px">
                        07/08/2020 - 20/09/2020
                    </span>
                </b>
            </span>
            <br>
        </div>
        <div>
            It's time to join us with high motivation and dedication to work and achieve success at high heights.
            <br>
        </div>
        <div>
            <br>
        </div>
        <div>
            You can read the guidelines
            <span class="colour" style="color:rgb(0, 0, 153)">
                <b>
                    <u>
                        <a href="https://rethink.software/api/v2/connectedApps.requestObject/7df2a8d8-781c-4e00-9e2b-1db00dfdbe01?connectedAppsId=65398&amp;key=uploads%2Fpritam-kundu%2Fdrive-personal-sfDQd9d%2Fguidelines-for-t-sip-3.0.pdf-CLQu5cq%2FGuidelines%2520For%2520T-SIP%25203.0.pdf&amp;itemsOriginalId=24e89c9e-978c-4268-a3cb-48a4b765d500" target="_blank">
                            here
                        </a>
                    </u>
                </b>
            </span>
            for further queries on what comes to your mind.
            <br>
        </div>
        <div>
            We will intimate you soon with an exciting start of the Internship at Teckat Student Intern Partner- 3.0
            <br>
        </div>
        <div>
            <br>
        </div>
        <div>
            All the best!
            <br>
        </div>
        <div>
            Stay Updated. Stay focused.
            <br>
        </div>
        <div>
            <br>
        </div>
        <div>
            <br>
        </div>
    </div>
    <div>
        <div>
            <table cellpadding="0" cellspacing="0" class="ng-scope" style="box-sizing: border-box; border-spacing: 0px; border-collapse: collapse; background-color: rgb(255, 255, 255); color: rgb(68, 68, 68); font-style: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; width: 525px; font-size: 11pt; font-family: Arial, sans-serif">
                <tbody style="box-sizing: border-box">
                    <tr style="box-sizing: border-box">
                        <td width="125" valign="top" rowspan="6" class="ng-scope" style="box-sizing: border-box; padding: 0px 10px 0px 0px; font-size: 10pt; font-family: Arial, sans-serif; border-right: 1px solid rgb(251, 99, 3); width: 125px; vertical-align: top">
                            <br>
                        </td>
                        <td style="box-sizing: border-box; padding: 0px 0px 0px 10px">
                            <table cellpadding="0" cellspacing="0" style="box-sizing: border-box; border-spacing: 0px; border-collapse: collapse; background-color: transparent">
                                <tbody style="box-sizing: border-box">
                                    <tr style="box-sizing: border-box">
                                        <td valign="top" style="box-sizing: border-box; padding: 0px 0px 5px 10px; font-size: 10pt; color: rgb(0, 121, 172); font-family: Arial, sans-serif; width: 400px; vertical-align: top">
                                            THANKS &amp; REGARDS
                                            <br>
                                        </td>
                                    </tr>
                                    <tr style="box-sizing: border-box">
                                        <td valign="top" style="box-sizing: border-box; padding: 5px 0px 5px 10px; font-size: 10pt; color: rgb(68, 68, 68); font-family: Arial, sans-serif; vertical-align: top; line-height: 17px">
                                            <span class="ng-scope" style="box-sizing: border-box">
                                                <span style="color: rgb(251, 99, 3); box-sizing: border-box;" class="colour">
                                                    <b>
                                                        a:
                                                        <span>
                                                            &nbsp;
                                                        </span>
                                                    </b>
                                                </span>
                                                <span style="color:rgb(0, 0, 0)" class="colour">
                                                    <span style="font-family:Arial, sans-serif" class="font">
                                                        <span style="font-size: 10pt; box-sizing: border-box;" class="size">
                                                            Teckat Services Private Limited
                                                        </span>
                                                    </span>
                                                </span>
                                                <span>
                                                    &nbsp;
                                                </span>
                                                <span style="color:rgb(0, 0, 0)" class="colour">
                                                    <span style="font-family:Arial, sans-serif" class="font">
                                                        <span style="font-size: 10pt; box-sizing: border-box;" class="size">
                                                            <span class="ng-scope" style="box-sizing: border-box">
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
                                                <span style="color:rgb(0, 0, 0)" class="colour">
                                                    <span style="font-family:Arial, sans-serif" class="font">
                                                        <span style="font-size: 10pt; box-sizing: border-box;" class="size">
                                                            <span class="ng-scope" style="box-sizing: border-box">
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
                                                <span style="color: rgb(251, 99, 3); box-sizing: border-box;" class="colour">
                                                    <b>
                                                        e:
                                                    </b>
                                                </span>
                                                <span style="color:rgb(0, 0, 0)" class="colour">
                                                    <span style="font-family:Arial, sans-serif" class="font">
                                                        <span style="font-size: 10pt; box-sizing: border-box;" class="size">
                                                            <span>
                                                                &nbsp;
                                                            </span>
                                                            <a href="mailto:support@teckat.com" target="_blank">
                                                                support@teckat.com
                                                            </a>
                                                        </span>
                                                    </span>
                                                </span>
                                            </span>
                                            <span>
                                                &nbsp;
                                            </span>
                                            <span class="ng-scope" style="box-sizing: border-box">
                                                <span class="ng-scope" style="box-sizing: border-box">
                                                    |
                                                    <span>
                                                        &nbsp;
                                                    </span>
                                                </span>
                                                <span style="color: rgb(251, 99, 3); box-sizing: border-box;" class="colour">
                                                    <b>
                                                        w:
                                                    </b>
                                                </span>
                                                <a style="box-sizing: border-box; background-color: transparent; color: rgb(51, 122, 183); text-decoration: none" href="http://teckat.com/" target="_blank">
                                                    <span style="color:rgb(0, 0, 0)" class="colour">
                                                        <span style="font-family:Arial, sans-serif" class="font">
                                                            <span style="font-size: 10pt; box-sizing: border-box;" class="size">
                                                                <span>
                                                                    &nbsp;
                                                                </span>
                                                                teckat.com
                                                            </span>
                                                        </span>
                                                    </span>
                                                </a>
                                                <br style="box-sizing: border-box">
                                                <span style="color: rgb(251, 99, 3); box-sizing: border-box;" class="colour">
                                                    <b>
                                                        m:
                                                    </b>
                                                </span>
                                                <span style="color:rgb(0, 0, 0)" class="colour">
                                                    <span style="font-family:Arial, sans-serif" class="font">
                                                        <span style="font-size: 10pt; box-sizing: border-box;" class="size">
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
                                    <tr class="ng-scope" style="box-sizing: border-box">
                                        <td valign="bottom" style="box-sizing: border-box; padding: 5px 0px 0px 10px; font-size: 10pt; font-family: Arial, sans-serif; vertical-align: bottom">
                                            <span class="ng-scope" style="box-sizing: border-box">
                                                <a style="box-sizing: border-box; background-color: transparent; color: rgb(51, 122, 183); text-decoration: none" href="https://www.facebook.com/in.teckat/" target="_blank">
                                                    <img height="19" border="0" width="19" alt="facebook icon" src="https://codetwocdn.azureedge.net/images/mail-signatures/generator-dm/bease-fox/fb.png" style="box-sizing: border-box; border: 0px; vertical-align: middle; height: 19px; width: 19px">
                                                </a>
                                                &nbsp;
                                                <a style="box-sizing: border-box; background-color: transparent; color: rgb(51, 122, 183); text-decoration: none" href="https://www.linkedin.com/company/teckat-service-pvt-ltd/?viewAsMember=true" target="_blank">
                                                    <img height="19" border="0" width="19" alt="linkedin icon" src="https://codetwocdn.azureedge.net/images/mail-signatures/generator-dm/bease-fox/ln.png" style="box-sizing: border-box; border: 0px; vertical-align: middle; height: 19px; width: 19px">
                                                </a>
                                                &nbsp;
                                                <a style="box-sizing: border-box; background-color: transparent; color: rgb(51, 122, 183); text-decoration: none" href="https://www.instagram.com/india.teckat/" target="_blank">
                                                    <img height="19" border="0" width="19" alt="instagram icon" src="https://codetwocdn.azureedge.net/images/mail-signatures/generator-dm/bease-fox/it.png" style="box-sizing: border-box; border: 0px; vertical-align: middle; height: 19px; width: 19px">
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
        </div>
    </div>
    <div style="font-family: Verdana, Arial, Helvetica, sans-serif;font-size: 10.0pt;">
        <div id="x_-158763297Zm-_Id_-Sgn">
            <div>
                <div>
                    <table style="box-sizing: border-box;border-spacing: 0.0px;border-collapse: collapse;background-color: rgb(255,255,255);color: rgb(68,68,68);font-style: normal;font-weight: 400;letter-spacing: normal;orphans: 2;text-indent: 0.0px;text-transform: none;white-space: normal;widows: 2;word-spacing: 0.0px;width: 525.0px;font-size: 11.0pt;font-family: Arial, sans-serif;" class="x_-158763297ng-scope" cellspacing="0" cellpadding="0">
                        <tbody style="box-sizing: border-box;">
                            <tr style="box-sizing: border-box;">
                                <td style="box-sizing: border-box;padding: 0.0px 0.0px 0.0px 10.0px;">
                                    <table style="box-sizing: border-box;border-spacing: 0.0px;border-collapse: collapse;background-color: transparent;" cellspacing="0" cellpadding="0">
                                        <tbody style="box-sizing: border-box;">
                                            <tr style="box-sizing: border-box;" class="x_-158763297ng-scope">
                                                <td style="box-sizing: border-box;padding: 5.0px 0.0px 0.0px 10.0px;font-size: 10.0pt;font-family: Arial, sans-serif;vertical-align: bottom;" valign="bottom">
                                                    <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                                                        <br>
                                                    </span>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <div>
                        <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                            <br>
                        </span>
                    </div>
                </div>
            </div>
            <div>
                <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                    <br>
                </span>
            </div>
        </div>
        <div>
            <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                <br>
            </span>
        </div>
        <div>
            <br>
        </div>
    </div>
</div>
<div>
    <br>
</div>



  </body>
</html>

                '''.format(separate[0])

            elif(mailStatus == 'Payment referral generate link'):

                html = '''
<html>
  <head></head>
  <body>


<div>
    <div style="font-family: Verdana, Arial, Helvetica, sans-serif;font-size: 10.0pt;">
        <div>
            <div style="font-family: Verdana, Arial, Helvetica, sans-serif;font-size: 10.0pt;">
                <div>
                    <div style="font-family: Verdana, Arial, Helvetica, sans-serif;font-size: 10.0pt;">
                        <div>
                            <div style="font-family: Verdana, Arial, Helvetica, sans-serif;font-size: 10.0pt;">
                                <div style="line-height: 1.5;">
                                    <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                                        Dear {},
                                    </span>
                                    <br>
                                </div>
                                <div style="line-height: 1.5;">
                                    <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                                        WELCOME TO TECKAT STUDENT INTERN PARTNER
                                    </span>
                                    <span class="font" style="font-family:serif, sans-serif">
                                        3.0
                                    </span>
                                    <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                                    </span>
                                    <br>
                                </div>
                                <div>
                                    <br>
                                </div>
                                <div style="line-height: 1.5;">
                                    <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                                        <span class="colour" style="color:rgb(0, 0, 153)">
                                            This time you have all the opportunities to earn huge incentives, rewards, Teckat t-shirts, special certifications and many more.
                                        </span>
                                    </span>
                                    <br>
                                </div>
                                <div style="line-height: 1.5;">
                                    <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                                        <span class="colour" style="color:rgb(0, 0, 153)">
                                            This is your first target that you have to achieve.
                                        </span>
                                    </span>
                                    <br>
                                </div>
                                <div style="line-height: 1.5;">
                                    <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                                        <span class="colour" style="color:rgb(0, 0, 153)">
                                            This is all about a training contest organised by Teckat on various technologies and marketing fields.
                                        </span>
                                    </span>
                                    <br>
                                </div>
                                <div>
                                    <br>
                                </div>
                                <div>
                                    <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                                        <b>
                                            <span class="size" style="font-size:10.6667px">
                                                DURATION OF THE CONTEST&nbsp;
                                            </span>
                                            -&nbsp;
                                        </b>
                                        From
                                        <b>
                                            Today
                                        </b>
                                        till
                                        <b>
                                            9th August, 2020 (12 Midnight)
                                        </b>
                                    </span>
                                    <br>
                                </div>
                                <div>
                                    <br>
                                </div>
                                <div>
                                    <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                                        <b>
                                            <span class="size" style="font-size:16px">
                                                <span class="colour" style="color:rgb(0, 0, 153)">
                                                    <u>
                                                        What shall you do?
                                                    </u>
                                                </span>
                                            </span>
                                        </b>
                                    </span>
                                    <br>
                                </div>
                                <ul dir="ltr">
                                    <li>
                                        <span>
                                            <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                                                <span class="colour" style="color:rgb(204, 0, 0)">
                                                    You simply have to circulate it among your friends and colleagues through WhatsApp, Facebook, Instagram, to various groups, etc….
                                                </span>
                                            </span>
                                        </span>
                                        <br>
                                    </li>
                                </ul>
                                <div>
                                    <br>
                                </div>
                                <div>
                                    <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                                        <b>
                                            <span class="size" style="font-size:16px">
                                                <span class="colour" style="color:rgb(0, 0, 153)">
                                                    <u>
                                                        What will you get ?
                                                    </u>
                                                </span>
                                            </span>
                                        </b>
                                    </span>
                                    <br>
                                </div>
                                <ul dir="ltr">
                                    <li>
                                        <span>
                                            <span class="colour" style="color:rgb(204, 0, 0)">
                                                <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                                                    Every time your friend registers for any of the courses- you will add an incentive of Rs
                                                </span>
                                                <span class="font" style="font-family:serif, sans-serif">
                                                    120/-
                                                </span>
                                                <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                                                    on each successful enrollment.
                                                </span>
                                            </span>
                                            <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                                            </span>
                                        </span>
                                        <br>
                                    </li>
                                </ul>
                                <div>
                                    <br>
                                </div>
                                <div>
                                    <span class="font" style="font-family:serif, sans-serif">
                                        <b>
                                            1
                                        </b>
                                    </span>
                                    <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                                        <b>
                                            .
                                        </b>
                                        You can share the content below (
                                        <b>
                                            just copy and paste the share part
                                        </b>
                                        ) to your friends and colleagues through WhatsApp, Facebook and other mediums. Encourage them to enroll in the courses they want to.
                                    </span>
                                    <br>
                                </div>
                                <div>
                                    <br>
                                </div>
                                <div>
                                    <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                                        <b>
                                            Share (Copy and Paste )
                                        </b>
                                    </span>
                                    <br>
                                </div>
                                <div>
                                    ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                    <br>
                                </div>
                                <div style="line-height: 1.5;">
                                    <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                                        *Lock down can be useful and Skillful for Learners and Achievers, grab the opportunity to learn in the live sessions for anything you enroll for-*&nbsp;
                                    </span>
                                    <br>
                                </div>
                                <div style="line-height: 1.5;">
                                    <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                                        Enroll yourself in different *WORKSHOPS*, *WEBINARS* and *INTERNSHIP* at Teckat in the field of *ENGINEERING*, *TECHNOLOGY*, *MARKETING*, *DESIGNING*, *DEVELOPMENT* at Teckat Webinar Series-
                                    </span>
                                    <span class="font" style="font-family:serif, sans-serif">
                                        3.0.
                                    </span>
                                    <br>
                                </div>
                                <div style="line-height: 1.5;">
                                    *What You Get?*
                                    <br>
                                </div>
                                <div style="line-height: 1.5;">
                                    1. Live Session throughout the course Internship
                                    <br>
                                </div>
                                <div style="line-height: 1.5;">
                                    2. Recorded link of each session- lifetime access
                                    <br>
                                </div>
                                <div style="line-height: 1.5;">
                                    3. ISO Certification- Get Course Internship Certification
                                    <br>
                                </div>
                                <div style="line-height: 1.5;">
                                    4. Doubt Sessions- 15 minutes before each session and in mid of the session.
                                    <br>
                                </div>
                                <div style="line-height: 1.5;">
                                    5. Live projects implementation - Complete guidance from Scratch.
                                    <br>
                                </div>
                                <div style="line-height: 1.5;">
                                    <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                                        HERE IS THE LINK TO REGISTER IN ANY OF THE COURSE YOU WANT TO-
                                    </span>
                                    <br>
                                </div>
                                <div style="line-height: 1.5;">
                                    <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                                        *Link to Register*-&nbsp; &nbsp;{}
                                    </span>
                                    <br>
                                </div>
                                <div>
                                    <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                                        -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                    </span>
                                    <br>
                                </div>
                                <div>
                                    <br>
                                </div>
                                <div>
                                    <br>
                                </div>
                                <div>
                                    <span class="font" style="font-family:serif, sans-serif">
                                        <b>
                                            2
                                        </b>
                                    </span>
                                    <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                                        <b>
                                            .
                                        </b>
                                        &nbsp; You can also share the details directly on WhatsApp
                                    </span>
                                    <br>
                                </div>
                                <div>
                                    <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                                        <br>
                                    </span>
                                </div>
                                <div>
                                    &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
                                    <a style="background-color:#25d366;border:1px solid #128c7e;border-radius:4px;color:#ffffff;display:inline-block;font-family:sans-serif;font-size:13px;font-weight:bold;line-height:40px;text-align:center;text-decoration:none;width:200px;-webkit-text-size-adjust:none;mso-hide:all;" href="https://wa.me/?text=%2ALock%20down%20can%20be%20useful%20and%20Skillful%20for%20Learners%20and%20Achievers%2C%20grab%20the%20opportunity%20to%20learn%20in%20the%20live%20sessions%20for%20anything%20you%20enroll%20for-%2A%C2%A0%0A%0AEnroll%20yourself%20in%20different%20%2AWORKSHOPS%2A%2C%20%2AWEBINARS%2A%20and%20%2AINTERNSHIP%2A%20at%20Teckat%20in%20the%20field%20of%20%2AENGINEERING%2A%2C%20%2ATECHNOLOGY%2A%2C%20%2AMARKETING%2A%2C%20%2ADESIGNING%2A%2C%20%2ADEVELOPMENT%2A%20at%20Teckat%20Webinar%20Series-%203.0.%0A%0A%2AWhat%20You%20Get%3F%2A%0A%0A1.%20Live%20Session%20throughout%20the%20course%20Internship%0A%0A2.%20Recorded%20link%20of%20each%20session-%20lifetime%20access%0A%0A3.%20ISO%20Certification-%20Get%20Course%20Internship%20Certification%0A%0A4.%20Doubt%20Sessions-%2015%20minutes%20before%20each%20session%20and%20in%20mid%20of%20the%20session.%0A%0A5.%20Live%20projects%20implementation%20-%20Complete%20guidance%20from%20Scratch.%0A%0AHERE%20IS%20THE%20LINK%20TO%20REGISTER%20IN%20ANY%20OF%20THE%20COURSE%20YOU%20WANT%20TO-%0A%0A%2ALink%20to%20Register%2A-%C2%A0{}" target="_blank">
                                        Share on WhatsApp
                                    </a>
                                    <br>
                                </div>
                                <div>
                                    <br>
                                </div>
                                <div>
                                    <br>
                                </div>
                                <div>
                                    <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                                        We will intimate you with the incentives earned by you in the end of contest through mail.
                                    </span>
                                    <br>
                                </div>
                                <div>
                                    <br>
                                </div>
                                <div>
                                    <br>
                                </div>
                                <div>
                                    <br>
                                </div>
                                <div id="x_-1779381906Zm-_Id_-Sgn">
                                    <div>
                                        <div>
                                            <table style="box-sizing: border-box;border-spacing: 0.0px;border-collapse: collapse;background-color: rgb(255,255,255);color: rgb(68,68,68);font-style: normal;font-weight: 400;letter-spacing: normal;orphans: 2;text-indent: 0.0px;text-transform: none;white-space: normal;widows: 2;word-spacing: 0.0px;width: 525.0px;font-size: 11.0pt;font-family: Arial, sans-serif;" class="x_-1779381906ng-scope" cellspacing="0" cellpadding="0">
                                                <tbody style="box-sizing: border-box;">
                                                    <tr style="box-sizing: border-box;">
                                                        <td style="box-sizing: border-box;padding: 0.0px 0.0px 0.0px 10.0px;">
                                                            <table style="box-sizing: border-box;border-spacing: 0.0px;border-collapse: collapse;background-color: transparent;" cellspacing="0" cellpadding="0">
                                                                <tbody style="box-sizing: border-box;">
                                                                    <tr style="box-sizing: border-box;" class="x_-1779381906ng-scope">
                                                                        <td style="box-sizing: border-box;padding: 5.0px 0.0px 0.0px 10.0px;font-size: 10.0pt;font-family: Arial, sans-serif;vertical-align: bottom;" valign="bottom">
                                                                            <div id="Zm-_Id_-Sgn" data-zbluepencil-ignore="true">
                                                                                <div>
                                                                                    <div>
                                                                                        <table cellpadding="0" cellspacing="0" class="ng-scope" style="box-sizing: border-box; border-spacing: 0px; border-collapse: collapse; background-color: rgb(255, 255, 255); color: rgb(68, 68, 68); font-style: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; width: 525px; font-size: 11pt; font-family: Arial, sans-serif">
                                                                                            <tbody style="box-sizing: border-box">
                                                                                                <tr style="box-sizing: border-box">
                                                                                                    <td width="125" valign="top" rowspan="6" class="ng-scope" style="box-sizing: border-box; padding: 0px 10px 0px 0px; font-size: 10pt; font-family: Arial, sans-serif; border-right: 1px solid rgb(251, 99, 3); width: 125px; vertical-align: top">
                                                                                                        <br>
                                                                                                    </td>
                                                                                                    <td style="box-sizing: border-box; padding: 0px 0px 0px 10px">
                                                                                                        <table cellpadding="0" cellspacing="0" style="box-sizing: border-box; border-spacing: 0px; border-collapse: collapse; background-color: transparent">
                                                                                                            <tbody style="box-sizing: border-box">
                                                                                                                <tr style="box-sizing: border-box">
                                                                                                                    <td valign="top" style="box-sizing: border-box; padding: 0px 0px 5px 10px; font-size: 10pt; color: rgb(0, 121, 172); font-family: Arial, sans-serif; width: 400px; vertical-align: top">
                                                                                                                        THANKS &amp; REGARDS
                                                                                                                        <br>
                                                                                                                    </td>
                                                                                                                </tr>
                                                                                                                <tr style="box-sizing: border-box">
                                                                                                                    <td valign="top" style="box-sizing: border-box; padding: 5px 0px 5px 10px; font-size: 10pt; color: rgb(68, 68, 68); font-family: Arial, sans-serif; vertical-align: top; line-height: 17px">
                                                                                                                        <span class="ng-scope" style="box-sizing: border-box">
                                                                                                                            <span style="color: rgb(251, 99, 3); box-sizing: border-box;" class="colour">
                                                                                                                                <b>
                                                                                                                                    a:
                                                                                                                                    <span>
                                                                                                                                        &nbsp;
                                                                                                                                    </span>
                                                                                                                                </b>
                                                                                                                            </span>
                                                                                                                            <span style="color:rgb(0, 0, 0)" class="colour">
                                                                                                                                <span style="font-family:Arial, sans-serif" class="font">
                                                                                                                                    <span style="font-size: 10pt; box-sizing: border-box;" class="size">
                                                                                                                                        Teckat Services Private Limited
                                                                                                                                    </span>
                                                                                                                                </span>
                                                                                                                            </span>
                                                                                                                            <span>
                                                                                                                                &nbsp;
                                                                                                                            </span>
                                                                                                                            <span style="color:rgb(0, 0, 0)" class="colour">
                                                                                                                                <span style="font-family:Arial, sans-serif" class="font">
                                                                                                                                    <span style="font-size: 10pt; box-sizing: border-box;" class="size">
                                                                                                                                        <span class="ng-scope" style="box-sizing: border-box">
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
                                                                                                                            <span style="color:rgb(0, 0, 0)" class="colour">
                                                                                                                                <span style="font-family:Arial, sans-serif" class="font">
                                                                                                                                    <span style="font-size: 10pt; box-sizing: border-box;" class="size">
                                                                                                                                        <span class="ng-scope" style="box-sizing: border-box">
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
                                                                                                                            <span style="color: rgb(251, 99, 3); box-sizing: border-box;" class="colour">
                                                                                                                                <b>
                                                                                                                                    e:
                                                                                                                                </b>
                                                                                                                            </span>
                                                                                                                            <span style="color:rgb(0, 0, 0)" class="colour">
                                                                                                                                <span style="font-family:Arial, sans-serif" class="font">
                                                                                                                                    <span style="font-size: 10pt; box-sizing: border-box;" class="size">
                                                                                                                                        <span>
                                                                                                                                            &nbsp;
                                                                                                                                        </span>
                                                                                                                                        <a href="mailto:support@teckat.com" target="_blank">
                                                                                                                                            support@teckat.com
                                                                                                                                        </a>
                                                                                                                                    </span>
                                                                                                                                </span>
                                                                                                                            </span>
                                                                                                                        </span>
                                                                                                                        <span>
                                                                                                                            &nbsp;
                                                                                                                        </span>
                                                                                                                        <span class="ng-scope" style="box-sizing: border-box">
                                                                                                                            <span class="ng-scope" style="box-sizing: border-box">
                                                                                                                                |
                                                                                                                                <span>
                                                                                                                                    &nbsp;
                                                                                                                                </span>
                                                                                                                            </span>
                                                                                                                            <span style="color: rgb(251, 99, 3); box-sizing: border-box;" class="colour">
                                                                                                                                <b>
                                                                                                                                    w:
                                                                                                                                </b>
                                                                                                                            </span>
                                                                                                                            <a style="box-sizing: border-box; background-color: transparent; color: rgb(51, 122, 183); text-decoration: none" href="http://teckat.com/" target="_blank">
                                                                                                                                <span style="color:rgb(0, 0, 0)" class="colour">
                                                                                                                                    <span style="font-family:Arial, sans-serif" class="font">
                                                                                                                                        <span style="font-size: 10pt; box-sizing: border-box;" class="size">
                                                                                                                                            <span>
                                                                                                                                                &nbsp;
                                                                                                                                            </span>
                                                                                                                                            teckat.com
                                                                                                                                        </span>
                                                                                                                                    </span>
                                                                                                                                </span>
                                                                                                                            </a>
                                                                                                                            <br style="box-sizing: border-box">
                                                                                                                            <span style="color: rgb(251, 99, 3); box-sizing: border-box;" class="colour">
                                                                                                                                <b>
                                                                                                                                    m:
                                                                                                                                </b>
                                                                                                                            </span>
                                                                                                                            <span style="color:rgb(0, 0, 0)" class="colour">
                                                                                                                                <span style="font-family:Arial, sans-serif" class="font">
                                                                                                                                    <span style="font-size: 10pt; box-sizing: border-box;" class="size">
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
                                                                                                                <tr class="ng-scope" style="box-sizing: border-box">
                                                                                                                    <td valign="bottom" style="box-sizing: border-box; padding: 5px 0px 0px 10px; font-size: 10pt; font-family: Arial, sans-serif; vertical-align: bottom">
                                                                                                                        <span class="ng-scope" style="box-sizing: border-box">
                                                                                                                            <a style="box-sizing: border-box; background-color: transparent; color: rgb(51, 122, 183); text-decoration: none" href="https://www.facebook.com/in.teckat/" target="_blank">
                                                                                                                                <img height="19" border="0" width="19" alt="facebook icon" src="https://codetwocdn.azureedge.net/images/mail-signatures/generator-dm/bease-fox/fb.png" style="box-sizing: border-box; border: 0px; vertical-align: middle; height: 19px; width: 19px">
                                                                                                                            </a>
                                                                                                                            &nbsp;
                                                                                                                            <a style="box-sizing: border-box; background-color: transparent; color: rgb(51, 122, 183); text-decoration: none" href="https://www.linkedin.com/company/teckat-service-pvt-ltd/?viewAsMember=true" target="_blank">
                                                                                                                                <img height="19" border="0" width="19" alt="linkedin icon" src="https://codetwocdn.azureedge.net/images/mail-signatures/generator-dm/bease-fox/ln.png" style="box-sizing: border-box; border: 0px; vertical-align: middle; height: 19px; width: 19px">
                                                                                                                            </a>
                                                                                                                            &nbsp;
                                                                                                                            <a style="box-sizing: border-box; background-color: transparent; color: rgb(51, 122, 183); text-decoration: none" href="https://www.instagram.com/india.teckat/" target="_blank">
                                                                                                                                <img height="19" border="0" width="19" alt="instagram icon" src="https://codetwocdn.azureedge.net/images/mail-signatures/generator-dm/bease-fox/it.png" style="box-sizing: border-box; border: 0px; vertical-align: middle; height: 19px; width: 19px">
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
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </td>
                                                                    </tr>
                                                                </tbody>
                                                            </table>
                                                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </div>
                                    </div>
                                    <div>
                                        <br>
                                    </div>
                                </div>
                                <div>
                                    <br>
                                </div>
                                <div>
                                    <br>
                                </div>
                            </div>
                            <div>
                                <br>
                            </div>
                        </div>
                        <div>
                            <br>
                        </div>
                    </div>
                </div>
                <div>
                    <br>
                </div>
            </div>
        </div>
        <div>
            <br>
        </div>
    </div>
</div>
<div>
    <br>
</div>



  </body>
</html>

                '''.format(separate[0], strLink3, strLink3)
            elif(mailStatus == 'Bonus Hours'):

                html = '''
<html>
  <head></head>
  <body>



<div>
    <div style="font-family: Verdana, Arial, Helvetica, sans-serif;font-size: 10.0pt;">
        <div>
            <div style="font-family: Verdana, Arial, Helvetica, sans-serif;font-size: 10.0pt;">
                <div>
                    <div style="font-family: Verdana, Arial, Helvetica, sans-serif;font-size: 10.0pt;">
                        <div>
                            <div style="font-family: Verdana, Arial, Helvetica, sans-serif;font-size: 10.0pt;">
                                <div>
                                    <div style="font-family: Verdana, Arial, Helvetica, sans-serif;font-size: 10.0pt;">
                                        <div style="font-family: Verdana, Arial, Helvetica, sans-serif;font-size: 10.0pt;">
                                            <div>
                                                <br>
                                            </div>
                                            <div>
                                                <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
                                                    Dear {},
                                                </span>
                                                <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
                                                </span>
                                                <br>
                                            </div>
                                            <div>
                                                <br>
                                            </div>
                                            <div>
                                                <b>
                                                    <span class="size" style="font-size:16px">
                                                        <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
                                                            This is the best opportunity you can take and win a special certification on "Marketing Management".
                                                        </span>
                                                    </span>
                                                </b>
                                                <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
                                                </span>
                                                <br>
                                            </div>
                                            <div>
                                                <span class="size" style="font-size:16px">
                                                    <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
                                                        You just have to share the details to as
                                                    </span>
                                                    <b>
                                                        <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
                                                            &nbsp;
                                                        </span>
                                                    </b>
                                                    <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
                                                        many contacts through Whatsapp, Facebook or Instagram,etc........
                                                    </span>
                                                </span>
                                                <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
                                                </span>
                                                <br>
                                            </div>
                                            <div>
                                                <br>
                                            </div>
                                            <div>
                                                <span class="size" style="font-size:16px">
                                                    <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
                                                        Share the details below along with the Attachment and get as many enrollments...
                                                    </span>
                                                </span>
                                                <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
                                                </span>
                                                <br>
                                            </div>
                                            <div>
                                                <span class="size" style="font-size:16px">
                                                    <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
                                                        Remember, this is completely free of cost live session.
                                                    </span>
                                                </span>
                                                <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
                                                </span>
                                                <br>
                                            </div>
                                            <div>
                                                <br>
                                            </div>
                                            <div>
                                                <br>
                                            </div>
                                            <div>
                                                <span class="size" style="font-size:16px">
                                                    <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
                                                        1.
                                                    </span>
                                                </span>
                                                <b>
                                                    <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
                                                        <span class="size" style="font-size: 14.666666666666666px">
                                                            Share (Copy and Paste)
                                                        </span>
                                                    </span>
                                                </b>
                                                <br>
                                            </div>
                                            <div>
                                                <br>
                                            </div>
                                            <div>
                                                <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
                                                    -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                </span>
                                                <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
                                                </span>
                                                <br>
                                            </div>
                                            <div>
                                                <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
                                                    *Skills are only thing that takes you through all the good and bad experiences and you come ahead winning all those....*
                                                </span>
                                                <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
                                                </span>
                                                <br>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div>
                <br>
            </div>
        </div>
        <div>
            <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
                A man who is an inspiration and a skilled personality who can help you reach all your target in life......
            </span>
            <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
            </span>
            <br>
        </div>
        <div>
            <br>
        </div>
        <div>
            <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
                *One of the top CA with experience of around 11 years in various field of expertise. Connecting young minds and helping their start-up and innovative ideas grow at right time.*
            </span>
            <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
            </span>
            <br>
        </div>
        <div>
            <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
                *CA. YASH MODI*
            </span>
            <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
            </span>
            <br>
        </div>
        <div>
            <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
                *FOUNDER- YASH MODI AND ASSOCIATES.*
            </span>
            <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
            </span>
            <br>
        </div>
        <div>
            <br>
        </div>
        <div>
            <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
                An initiative to bring such opportunities to your door and help you find the way to success....
            </span>
            <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
            </span>
            <br>
        </div>
        <div>
            <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
                Live Session to be held on 3rd September 2020 at 3pm.
            </span>
            <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
            </span>
            <br>
        </div>
        <div>
            <br>
        </div>
        <div>
            <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
                Connect with him Live on YouTube and find the best ever EXPERIENCE of knowledge and understanding.
            </span>
            <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
            </span>
            <br>
        </div>
        <div>
            <br>
        </div>
        <div>
            <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
                *Register yourself and get ready to achieve the best.*
            </span>
            <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
            </span>
            <br>
        </div>
        <div>
            <div style="font-family: Verdana, Arial, Helvetica, sans-serif;font-size: 10.0pt;">
                <div>
                    <div style="font-family: Verdana, Arial, Helvetica, sans-serif;font-size: 10.0pt;">
                        <div>
                            <div style="font-family: Verdana, Arial, Helvetica, sans-serif;font-size: 10.0pt;">
                                <div>
                                    <div style="font-family: Verdana, Arial, Helvetica, sans-serif;font-size: 10.0pt;">
                                        <div style="font-family: Verdana, Arial, Helvetica, sans-serif;font-size: 10.0pt;">
                                            <div>
                                                <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
                                                    Link-
                                                </span>
                                                <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
                                                    &nbsp;{}
                                                </span>
                                                <br>
                                            </div>
                                            <div>
                                                <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
                                                    Use Referral - {}
                                                </span>
                                                <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
                                                </span>
                                                <br>
                                            </div>
                                            <div>
                                                <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
                                                    -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                </span>
                                                <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
                                                </span>
                                                <br>
                                            </div>
                                            <div>
                                                <br>
                                            </div>
                                            <div>
                                                <br>
                                            </div>
                                            <div>
                                                <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
                                                    2.
                                                    <b>
                                                        You can also share on WhatsApp
                                                    </b>
                                                </span>
                                                <br>
                                            </div>
                                            <div>
                                                <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
                                                    <b>
                                                        ​
                                                    </b>
                                                </span>
                                                <br>
                                            </div>
                                            <div>
                                                &nbsp; &nbsp;&nbsp;
                                                <a style="background-color:#25d366;border:1px solid #128c7e;border-radius:4px;color:#ffffff;display:inline-block;font-family:sans-serif;font-size:13px;font-weight:bold;line-height:40px;text-align:center;text-decoration:none;width:200px;-webkit-text-size-adjust:none;mso-hide:all;" href="https://wa.me/?text=%2ASkills%20are%20only%20thing%20that%20takes%20you%20through%20all%20the%20good%20and%20bad%20experiences%20and%20you%20come%20ahead%20winning%20all%20those....%2A%0A%0AA%20man%20who%20is%20an%20inspiration%20and%20a%20skilled%20personality%20who%20can%20help%20you%20reach%20all%20your%20target%20in%20life......%0A%0A%2AOne%20of%20the%20top%20CA%20with%20experience%20of%20around%2011%20years%20in%20various%20field%20of%20expertise.%20Connecting%20young%20minds%20and%20helping%20their%20start-up%20and%20innovative%20ideas%20grow%20at%20right%20time.%2A%0A%0A%2ACA.%20YASH%20MODI%2A%0A%2AFOUNDER-%20YASH%20MODI%20AND%20ASSOCIATES.%2A%0A%0AAn%20initiative%20to%20bring%20such%20opportunities%20to%20your%20door%20and%20help%20you%20find%20the%20way%20to%20success....%0ALive%20Session%20to%20be%20held%20on%203rd%20September%202020%20at%203pm.%0A%0AConnect%20with%20him%20Live%20on%20YouTube%20and%20find%20the%20best%20ever%20EXPERIENCE%20of%20knowledge%20and%20understanding.%0A%0A%2ARegister%20yourself%20and%20get%20ready%20to%20achieve%20the%20best.%2A%0ALink-%20%C2%A0{}%0AUse%20Referral%20-%20%20{}" target="_blank">
                                                    WhatsApp
                                                </a>
                                                <br>
                                            </div>
                                            <div>
                                                <br>
                                            </div>
                                            <div>
                                                &nbsp;
                                                <br>
                                            </div>
                                            <div>
                                                <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
                                                    &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
                                                </span>
                                                <span class="font" style="font-family: georgia, &quot;times new roman&quot;, times, serif, sans-serif;">
                                                </span>
                                                <br>
                                            </div>
                                            <div>
                                                <br>
                                            </div>
                                            <div>
                                                <br>
                                            </div>
                                        </div>
                                    </div>
                                    <div>
                                        <div>
                                            <table cellpadding="0" cellspacing="0" class="x_1563714547ng-scope" style="box-sizing: border-box;border-spacing: 0.0px;border-collapse: collapse;background-color: rgb(255,255,255);color: rgb(68,68,68);font-style: normal;font-weight: 400;letter-spacing: normal;orphans: 2;text-indent: 0.0px;text-transform: none;white-space: normal;widows: 2;word-spacing: 0.0px;width: 525.0px;font-size: 11.0pt;font-family: Arial, sans-serif;">
                                                <tbody style="box-sizing: border-box;">
                                                    <tr style="box-sizing: border-box;">
                                                        <td style="box-sizing: border-box;padding: 0.0px 0.0px 0.0px 10.0px;">
                                                            <table cellpadding="0" cellspacing="0" style="box-sizing: border-box;border-spacing: 0.0px;border-collapse: collapse;background-color: transparent;">
                                                                <tbody style="box-sizing: border-box;">
                                                                    <tr class="x_1563714547ng-scope" style="box-sizing: border-box;">
                                                                        <td valign="bottom" style="box-sizing: border-box;padding: 5.0px 0.0px 0.0px 10.0px;font-size: 10.0pt;font-family: Arial, sans-serif;vertical-align: bottom;">
                                                                            <div id="x_1587367836Zm-_Id_-Sgn">
                                                                                <div>
                                                                                    <div>
                                                                                        <table cellpadding="0" cellspacing="0" class="x_1587367836ng-scope" style="box-sizing: border-box;border-spacing: 0.0px;border-collapse: collapse;background-color: rgb(255,255,255);color: rgb(68,68,68);font-style: normal;font-weight: 400;letter-spacing: normal;orphans: 2;text-indent: 0.0px;text-transform: none;white-space: normal;widows: 2;word-spacing: 0.0px;width: 525.0px;font-size: 11.0pt;font-family: Arial, sans-serif;">
                                                                                            <tbody style="box-sizing: border-box;">
                                                                                                <tr style="box-sizing: border-box;">
                                                                                                    <td style="box-sizing: border-box;padding: 0.0px 0.0px 0.0px 10.0px;">
                                                                                                        <table cellpadding="0" cellspacing="0" style="box-sizing: border-box;border-spacing: 0.0px;border-collapse: collapse;background-color: transparent;">
                                                                                                            <tbody style="box-sizing: border-box;">
                                                                                                                <tr class="x_1587367836ng-scope" style="box-sizing: border-box;">
                                                                                                                    <td valign="bottom" style="box-sizing: border-box;padding: 5.0px 0.0px 0.0px 10.0px;font-size: 10.0pt;font-family: Arial, sans-serif;vertical-align: bottom;">
                                                                                                                        <div id="Zm-_Id_-Sgn" data-zbluepencil-ignore="true">
                                                                                                                            <div>
                                                                                                                                <div>
                                                                                                                                    <table cellpadding="0" cellspacing="0" class="ng-scope" style="box-sizing: border-box; border-spacing: 0px; border-collapse: collapse; background-color: rgb(255, 255, 255); color: rgb(68, 68, 68); font-style: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; width: 525px; font-size: 11pt; font-family: Arial, sans-serif">
                                                                                                                                        <tbody style="box-sizing: border-box">
                                                                                                                                            <tr style="box-sizing: border-box">
                                                                                                                                                <td width="125" valign="top" rowspan="6" class="ng-scope" style="box-sizing: border-box; padding: 0px 10px 0px 0px; font-size: 10pt; font-family: Arial, sans-serif; border-right: 1px solid rgb(251, 99, 3); width: 125px; vertical-align: top">
                                                                                                                                                    <br>
                                                                                                                                                </td>
                                                                                                                                                <td style="box-sizing: border-box; padding: 0px 0px 0px 10px">
                                                                                                                                                    <table cellpadding="0" cellspacing="0" style="box-sizing: border-box; border-spacing: 0px; border-collapse: collapse; background-color: transparent">
                                                                                                                                                        <tbody style="box-sizing: border-box">
                                                                                                                                                            <tr style="box-sizing: border-box">
                                                                                                                                                                <td valign="top" style="box-sizing: border-box; padding: 0px 0px 5px 10px; font-size: 10pt; color: rgb(0, 121, 172); font-family: Arial, sans-serif; width: 400px; vertical-align: top">
                                                                                                                                                                    THANKS &amp; REGARDS
                                                                                                                                                                    <br>
                                                                                                                                                                </td>
                                                                                                                                                            </tr>
                                                                                                                                                            <tr style="box-sizing: border-box">
                                                                                                                                                                <td valign="top" style="box-sizing: border-box; padding: 5px 0px 5px 10px; font-size: 10pt; color: rgb(68, 68, 68); font-family: Arial, sans-serif; vertical-align: top; line-height: 17px">
                                                                                                                                                                    <span class="ng-scope" style="box-sizing: border-box">
                                                                                                                                                                        <span style="color: rgb(251, 99, 3); box-sizing: border-box;" class="colour">
                                                                                                                                                                            <b>
                                                                                                                                                                                a:
                                                                                                                                                                                <span>
                                                                                                                                                                                    &nbsp;
                                                                                                                                                                                </span>
                                                                                                                                                                            </b>
                                                                                                                                                                        </span>
                                                                                                                                                                        <span style="color:rgb(0, 0, 0)" class="colour">
                                                                                                                                                                            <span style="font-family:Arial, sans-serif" class="font">
                                                                                                                                                                                <span style="font-size: 10pt; box-sizing: border-box;" class="size">
                                                                                                                                                                                    Teckat Services Private Limited
                                                                                                                                                                                </span>
                                                                                                                                                                            </span>
                                                                                                                                                                        </span>
                                                                                                                                                                        <span>
                                                                                                                                                                            &nbsp;
                                                                                                                                                                        </span>
                                                                                                                                                                        <span style="color:rgb(0, 0, 0)" class="colour">
                                                                                                                                                                            <span style="font-family:Arial, sans-serif" class="font">
                                                                                                                                                                                <span style="font-size: 10pt; box-sizing: border-box;" class="size">
                                                                                                                                                                                    <span class="ng-scope" style="box-sizing: border-box">
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
                                                                                                                                                                        <span style="color:rgb(0, 0, 0)" class="colour">
                                                                                                                                                                            <span style="font-family:Arial, sans-serif" class="font">
                                                                                                                                                                                <span style="font-size: 10pt; box-sizing: border-box;" class="size">
                                                                                                                                                                                    <span class="ng-scope" style="box-sizing: border-box">
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
                                                                                                                                                                        <span style="color: rgb(251, 99, 3); box-sizing: border-box;" class="colour">
                                                                                                                                                                            <b>
                                                                                                                                                                                e:
                                                                                                                                                                            </b>
                                                                                                                                                                        </span>
                                                                                                                                                                        <span style="color:rgb(0, 0, 0)" class="colour">
                                                                                                                                                                            <span style="font-family:Arial, sans-serif" class="font">
                                                                                                                                                                                <span style="font-size: 10pt; box-sizing: border-box;" class="size">
                                                                                                                                                                                    <span>
                                                                                                                                                                                        &nbsp;
                                                                                                                                                                                    </span>
                                                                                                                                                                                    <a href="mailto:support@teckat.com" target="_blank">
                                                                                                                                                                                        support@teckat.com
                                                                                                                                                                                    </a>
                                                                                                                                                                                </span>
                                                                                                                                                                            </span>
                                                                                                                                                                        </span>
                                                                                                                                                                    </span>
                                                                                                                                                                    <span>
                                                                                                                                                                        &nbsp;
                                                                                                                                                                    </span>
                                                                                                                                                                    <span class="ng-scope" style="box-sizing: border-box">
                                                                                                                                                                        <span class="ng-scope" style="box-sizing: border-box">
                                                                                                                                                                            |
                                                                                                                                                                            <span>
                                                                                                                                                                                &nbsp;
                                                                                                                                                                            </span>
                                                                                                                                                                        </span>
                                                                                                                                                                        <span style="color: rgb(251, 99, 3); box-sizing: border-box;" class="colour">
                                                                                                                                                                            <b>
                                                                                                                                                                                w:
                                                                                                                                                                            </b>
                                                                                                                                                                        </span>
                                                                                                                                                                        <a style="box-sizing: border-box; background-color: transparent; color: rgb(51, 122, 183); text-decoration: none" href="http://teckat.com/" target="_blank">
                                                                                                                                                                            <span style="color:rgb(0, 0, 0)" class="colour">
                                                                                                                                                                                <span style="font-family:Arial, sans-serif" class="font">
                                                                                                                                                                                    <span style="font-size: 10pt; box-sizing: border-box;" class="size">
                                                                                                                                                                                        <span>
                                                                                                                                                                                            &nbsp;
                                                                                                                                                                                        </span>
                                                                                                                                                                                        teckat.com
                                                                                                                                                                                    </span>
                                                                                                                                                                                </span>
                                                                                                                                                                            </span>
                                                                                                                                                                        </a>
                                                                                                                                                                        <br style="box-sizing: border-box">
                                                                                                                                                                        <span style="color: rgb(251, 99, 3); box-sizing: border-box;" class="colour">
                                                                                                                                                                            <b>
                                                                                                                                                                                m:
                                                                                                                                                                            </b>
                                                                                                                                                                        </span>
                                                                                                                                                                        <span style="color:rgb(0, 0, 0)" class="colour">
                                                                                                                                                                            <span style="font-family:Arial, sans-serif" class="font">
                                                                                                                                                                                <span style="font-size: 10pt; box-sizing: border-box;" class="size">
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
                                                                                                                                                            <tr class="ng-scope" style="box-sizing: border-box">
                                                                                                                                                                <td valign="bottom" style="box-sizing: border-box; padding: 5px 0px 0px 10px; font-size: 10pt; font-family: Arial, sans-serif; vertical-align: bottom">
                                                                                                                                                                    <span class="ng-scope" style="box-sizing: border-box">
                                                                                                                                                                        <a style="box-sizing: border-box; background-color: transparent; color: rgb(51, 122, 183); text-decoration: none" href="https://www.facebook.com/in.teckat/" target="_blank">
                                                                                                                                                                            <img height="19" border="0" width="19" alt="facebook icon" src="https://codetwocdn.azureedge.net/images/mail-signatures/generator-dm/bease-fox/fb.png" style="box-sizing: border-box; border: 0px; vertical-align: middle; height: 19px; width: 19px">
                                                                                                                                                                        </a>
                                                                                                                                                                        &nbsp;
                                                                                                                                                                        <a style="box-sizing: border-box; background-color: transparent; color: rgb(51, 122, 183); text-decoration: none" href="https://www.linkedin.com/company/teckat-service-pvt-ltd/?viewAsMember=true" target="_blank">
                                                                                                                                                                            <img height="19" border="0" width="19" alt="linkedin icon" src="https://codetwocdn.azureedge.net/images/mail-signatures/generator-dm/bease-fox/ln.png" style="box-sizing: border-box; border: 0px; vertical-align: middle; height: 19px; width: 19px">
                                                                                                                                                                        </a>
                                                                                                                                                                        &nbsp;
                                                                                                                                                                        <a style="box-sizing: border-box; background-color: transparent; color: rgb(51, 122, 183); text-decoration: none" href="https://www.instagram.com/india.teckat/" target="_blank">
                                                                                                                                                                            <img height="19" border="0" width="19" alt="instagram icon" src="https://codetwocdn.azureedge.net/images/mail-signatures/generator-dm/bease-fox/it.png" style="box-sizing: border-box; border: 0px; vertical-align: middle; height: 19px; width: 19px">
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
                                                                                                                        </div>
                                                                                                                    </td>
                                                                                                                </tr>
                                                                                                            </tbody>
                                                                                                        </table>
                                                                                                    </td>
                                                                                                </tr>
                                                                                            </tbody>
                                                                                        </table>
                                                                                    </div>
                                                                                </div>
                                                                                <div>
                                                                                    <br>
                                                                                </div>
                                                                            </div>
                                                                        </td>
                                                                    </tr>
                                                                </tbody>
                                                            </table>
                                                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </div>
                                    </div>
                                    <div style="font-family: Verdana, Arial, Helvetica, sans-serif;font-size: 10.0pt;">
                                        <div>
                                            <div style="font-family: Verdana, Arial, Helvetica, sans-serif;font-size: 10.0pt;">
                                                <div>
                                                    <br>
                                                </div>
                                                <div>
                                                    <br>
                                                </div>
                                            </div>
                                        </div>
                                        <div>
                                            <br>
                                        </div>
                                    </div>
                                </div>
                                <div>
                                    <br>
                                </div>
                            </div>
                        </div>
                        <div>
                            <br>
                        </div>
                    </div>
                </div>
                <div>
                    <br>
                </div>
            </div>
        </div>
        <div>
            <br>
        </div>
    </div>
</div>
<div>
    <br>
</div>


  </body>
</html>

                '''.format(separate[0], link[0][0], separate[0], link[0][0], separate[0])

        msg.attach(MIMEText(html, 'html'))

        # attach attachments if present

        if(len(path)):
            for j in range(len(path)):

                # Generating File name
                emailFileName = path[j].split('/')
                print(emailFileName)
                # open the file to be sent
                filename = emailFileName[-1]
                attachment = open(path[j], "rb")

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

    global name
    global email
    global link
    global path
    global tsipId
    # clear arrays

    name.clear()
    email.clear()
    link.clear()
    path.clear()
    tsipId.clear()
    print(name, email, link, path, tsipId)
    tk.messagebox.showinfo(
        "Teckat", "Data Cleared successfully.")
    # main parent function


def mainFunction():
    global tsipStatus
    global generatePaymentLink
    global mailStatus
    firstRowIndex = int(entryFirstRowIndex.get())
    lastRowIndex = int(entryLastRowIndex.get())
    firstNameColumn = int(entryFirstNameIndex.get())
    lastNameColumn = int(entryLastNameIndex.get())
    emailColumn = int(entryEmailColumnIndex.get())
    idStatus = int(idVar.get())
    tsipStatus = tsipVar.get()
    linkStatus = int(linkVar.get())
    generatePaymentLink = int(generatePaymentVar.get())

    if (tsipStatus == 'T-SIP 3.0'):
        mailStatus = mailVar.get()
    if(linkStatus == 1 or generatePaymentLink == 1):

        linkColumn = int(entryLinkColumnIndex.get())
    else:
        linkColumn = ""

    if(idStatus == 1):
        idColumn = int(entryidColumnIndex.get())
    else:
        idColumn = ""
    print(firstRowIndex, lastRowIndex, firstNameColumn,
          lastNameColumn, emailColumn, linkColumn)
    tk.messagebox.showinfo(
        "Teckat", "Data stored Successfully wait for data generation")

    getExcelData(firstRowIndex, lastRowIndex,
                 firstNameColumn, lastNameColumn, emailColumn, linkColumn, idColumn)


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

idColumnLabel = tk.Label(
    root, text="TSIP ID Column No.", font=fontsizeData)
idColumnLabel.grid(row=7, column=0, pady=10)


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

entryidColumnIndex = tk.Entry(root, width=30, font=fontsizeData)
entryidColumnIndex.grid(row=7, column=1, padx=10, pady=10)

linkVar = tk.IntVar()

tk.Checkbutton(root, text="Do you want to attach Link",
               variable=linkVar, font=fontsizeData).grid(row=6, column=2)

generatePaymentVar = tk.IntVar()

tk.Checkbutton(root, text="Do you want to generate payment Link",
               variable=generatePaymentVar, font=fontsizeData).grid(row=6, column=3)


idVar = tk.IntVar()

tk.Checkbutton(root, text="attach T-SIP ID ( Its compulsory if you generate payment link)",
               variable=idVar, font=fontsizeData).grid(row=7, column=2, padx=5, pady=5)

# Drop down labels and entry

tsipTypeLabel = tk.Label(
    root, text="Tsip Type", font=fontsizeData)
tsipTypeLabel.grid(row=8, column=0, pady=10)

mailTypeLabel = tk.Label(
    root, text="Mail Type(Applicable from tsip 3.0)", font=fontsizeData)
mailTypeLabel.grid(row=9, column=0, pady=10)


# =========== tsip type ======================
# Create a Tkinter variable
tsipVar = tk.StringVar(root)

# Dictionary with options
tsipChoices = {'T-SIP 2.0', 'T-SIP 3.0'}
tsipVar.set('T-SIP 2.0')  # set the default option

tsipMenu = tk.OptionMenu(root, tsipVar, *tsipChoices)
tsipMenu.grid(row=8, column=1, padx=30, pady=10)


# ============= mail type ====================
# Create a Tkinter variable
mailVar = tk.StringVar(root)

# Dictionary with options
mailChoice = {'Thank you for submitting application',
              'application under review', 'Result Declaration', 'Payment referral generate link', 'Bonus Hours'}
mailVar.set('Thank you for submitting application')  # set the default option

mailMenu = tk.OptionMenu(root, mailVar, *mailChoice)
mailMenu.grid(row=9, column=1, padx=30, pady=10)


# attachment button
# excel button
browseButton_Excel = tk.Button(root, text='Attach files one by one', command=getAttachmentPath,
                               bg='green', fg='white', height=2, width=30, font=('helvetica', 12, 'bold'))
browseButton_Excel.grid(row=10, column=1, pady=30)


# Submit button

generatedataButton = tk.Button(root, text="Generate Data",
                               width=15, font=fontsizeData, command=mainFunction)
generatedataButton.grid(row=11, column=0, pady=20)

sendEmailButton = tk.Button(root, text="Send Email",
                            width=15, font=fontsizeData, command=sendEmail)
sendEmailButton.grid(row=11, column=1, pady=20)

clearDataButton = tk.Button(root, text="Clear Data",
                            width=15, font=fontsizeData, command=clearData)
clearDataButton.grid(row=11, column=2, pady=20)

root.mainloop()
