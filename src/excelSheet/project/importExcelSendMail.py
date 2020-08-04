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
            time.sleep(300)

        fromaddr = "noreply@teckat.com"
        toaddr = email[i]
        msg = MIMEMultipart()
        msg['From'] = "Teckat Student Intern Partner <noreply@teckat.com>"
        msg['To'] = toaddr

        if(tsipStatus == 'T-SIP 2.0'):
            msg['Subject'] = "UPDATE REGARDING INCENTIVE EARNED IN FIRST BONUS WEEK"

        elif(tsipStatus == 'T-SIP 3.0'):
            if(mailStatus == 'Thank you for submitting application'):
                msg['Subject'] = "Thank you for submitting your application at “T-SIP 3.0”"
            elif(mailStatus == 'application under review'):
                msg['Subject'] = "YOUR APPLICATION IS UNDER REVIEW - YOU CAN MAIL US IF YOU ARE HAVING ANY INTERROGATION"
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
            <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                Dear {},
                <br>
            </span>
        </div>
        <div>
            <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                There are certain update that has been done on your payment link.&nbsp;
                <br>
            </span>
        </div>
        <div>
            <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                Your updated payment link has been attached in this mail itself.
                <br>
            </span>
        </div>
        <div>
            <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                Your previous enrollment details has been shifted to this link. You will soon receive a mail with your incentives you earned during bonus week-1.
                <br>
            </span>
        </div>
        <div>
            <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                <br>
            </span>
        </div>
        <div>
            <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                The previous link has been deactivated from now onward.&nbsp;
                <br>
            </span>
        </div>
        <div>
            <span class="font" style="font-family:georgia, &quot;times new roman&quot;, times, serif, sans-serif">
                So, kindly use the links attached below for further enrollment.
            </span>
            <br>
        </div>
        <div>
            <br>
        </div>
        <p style="line-height: 1.38;margin-top: 0.0pt;margin-bottom: 0.0pt;" dir="ltr">
            <span class="highlight" style="background-color:transparent">
                <span class="colour" style="color:rgb(0, 0, 0)">
                    <span class="font" style="font-family:Arial">
                        <span class="size" style="font-size:10.6667px">
                            1. Copy the content written below and send it to all your friends.
                        </span>
                    </span>
                </span>
            </span>
            <br>
        </p>
        <div dir="ltr">
            <span class="highlight" style="background-color:transparent">
                <span class="colour" style="color:rgb(0, 0, 0)">
                    <span class="font" style="font-family:Arial">
                        <span class="size" style="font-size:10.6667px">
                            ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                        </span>
                    </span>
                </span>
            </span>
            <span class="size" style="font-size:10.6667px">
                <br>
            </span>
        </div>
        <p style="line-height: 1.38;margin-top: 0.0pt;margin-bottom: 0.0pt;" dir="ltr">
            <span class="highlight" style="background-color:transparent">
                <span class="colour" style="color:rgb(0, 0, 0)">
                    <span class="font" style="font-family:Arial">
                        <span class="size" style="font-size:10.6667px">
                            TECKAT WEBINAR SERIES- 3.0 is ready to launch the most trending and demanding courses that will give you a right platform to learn and develop projects easily.
                        </span>
                    </span>
                </span>
            </span>
            <span class="size" style="font-size:10.6667px">
                <br>
            </span>
        </p>
        <p style="line-height: 1.38;margin-top: 0.0pt;margin-bottom: 0.0pt;" dir="ltr">
            <span class="highlight" style="background-color:transparent">
                <span class="colour" style="color:rgb(0, 0, 0)">
                    <span class="font" style="font-family:Arial">
                        <span class="size" style="font-size:10.6667px">
                            Enroll Now-
                        </span>
                    </span>
                </span>
            </span>
            <br>
        </p>
        <div dir="ltr">
            <span class="highlight" style="background-color:transparent">
                <span class="colour" style="color:rgb(0, 0, 0)">
                    <span class="font" style="font-family:Arial">
                        <span class="size" style="font-size:10.6667px">
                            <span class="highlight" style="background-color:transparent">
                                <span class="font" style="font-family:Arial">
                                    <span class="size" style="font-size:10.6667px">
                                        <span class="colour" style="color:rgb(0, 0, 0)">
                                            Link 1-&nbsp; {}
                                            <br>
                                            Link 2-&nbsp; {}
                                            <br>
                                            Link 3-&nbsp; {}
                                        </span>
                                    </span>
                                </span>
                            </span>
                        </span>
                    </span>
                </span>
            </span>
            <span class="size" style="font-size:10.6667px">
                <br>
            </span>
        </div>
        <p style="line-height: 1.38;margin-top: 0.0pt;margin-bottom: 0.0pt;" dir="ltr">
            <span class="highlight" style="background-color:transparent">
                <span class="colour" style="color:rgb(255, 0, 0)">
                    <b>
                        <span class="font" style="font-family:Arial">
                            <span class="size" style="font-size:10.6667px">
                                *USP’s you get-*
                            </span>
                        </span>
                    </b>
                </span>
            </span>
            <span class="size" style="font-size:10.6667px">
                <br>
            </span>
        </p>
        <p style="line-height: 1.38;margin-top: 0.0pt;margin-bottom: 0.0pt;" dir="ltr">
            <span class="highlight" style="background-color:transparent">
                <span class="font" style="font-family:Arial">
                    <span class="size" style="font-size:10.6667px">
                        <span class="colour" style="color:rgb(0, 0, 0)">
                            Affordable price, ISO certification, Regular doubt sessions, Recorded video links
                        </span>
                    </span>
                </span>
            </span>
            <span class="colour" style="color:rgb(0, 0, 0)">
                <br>
            </span>
        </p>
        <div dir="ltr">
            <br>
        </div>
        <div dir="ltr">
            <span class="highlight" style="background-color:transparent">
                <span class="font" style="font-family:Arial">
                    <span class="size" style="font-size:10.6667px">
                        <span class="colour" style="color:rgb(0, 0, 0)">
                            ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                        </span>
                    </span>
                </span>
            </span>
            <span class="colour" style="color:rgb(0, 0, 0)">
                <br>
            </span>
        </div>
        <div dir="ltr">
            <span class="colour" style="color:rgb(0, 0, 0)">
                <br>
            </span>
        </div>
        <div dir="ltr">
            <span class="size" style="font-size:10.6667px">
                <span class="colour" style="color:rgb(0, 0, 0)">
                    <br>
                </span>
            </span>
        </div>
        <p style="line-height: 1.38;margin-top: 0.0pt;margin-bottom: 0.0pt;" dir="ltr">
            <span class="highlight" style="background-color:transparent">
                <span class="font" style="font-family:Arial">
                    <span class="size" style="font-size:10.6667px">
                        <span class="colour" style="color:rgb(0, 0, 0)">
                            2. You can also share the same content directly on whatsapp by clicking on the button bellow-
                        </span>
                    </span>
                </span>
            </span>
            <br>
        </p>
        <div dir="ltr">
            <br>
        </div>
        <div>
            <a href="https://wa.me/?text=TECKAT%20WEBINAR%20SERIES-%203.0%20is%20ready%20to%20launch%20the%20most%20trending%20and%20demanding%20courses%20that%20will%20give%20you%20a%20right%20platform%20to%20learn%20and%20develop%20projects%20easily.%0A%0AEnroll%20Now-%0A%0ALink%201-%20{}%0ALink%202-%20{}%0ALink%203-%20{}%0A%0A%2AUSP%E2%80%99s%20you%20get-%2A%0AAffordable%20price%2C%20ISO%20certification%2C%20Regular%20doubt%20sessions%2C%20Recorded%20video%20links" style="background-color:#25d366;border:1px solid #128c7e;border-radius:4px;color:#ffffff;display:inline-block;font-family:sans-serif;font-size:13px;font-weight:bold;line-height:40px;text-align:center;text-decoration:none;width:200px;-webkit-text-size-adjust:none;mso-hide:all;">
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
                                                <a href="http://teckat.com/" target="_blank" style="box-sizing: border-box; background-color: transparent; color: rgb(51, 122, 183); text-decoration: none">
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
                                                <a href="https://www.facebook.com/in.teckat/" target="_blank" style="box-sizing: border-box; background-color: transparent; color: rgb(51, 122, 183); text-decoration: none">
                                                    <img height="19" border="0" width="19" alt="facebook icon" src="https://codetwocdn.azureedge.net/images/mail-signatures/generator-dm/bease-fox/fb.png" style="box-sizing: border-box; border: 0px; vertical-align: middle; height: 19px; width: 19px">
                                                </a>
                                                &nbsp;
                                                <a href="https://www.linkedin.com/company/teckat-service-pvt-ltd/?viewAsMember=true" target="_blank" style="box-sizing: border-box; background-color: transparent; color: rgb(51, 122, 183); text-decoration: none">
                                                    <img height="19" border="0" width="19" alt="linkedin icon" src="https://codetwocdn.azureedge.net/images/mail-signatures/generator-dm/bease-fox/ln.png" style="box-sizing: border-box; border: 0px; vertical-align: middle; height: 19px; width: 19px">
                                                </a>
                                                &nbsp;
                                                <a href="https://www.instagram.com/india.teckat/" target="_blank" style="box-sizing: border-box; background-color: transparent; color: rgb(51, 122, 183); text-decoration: none">
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

        '''.format(separate[0], strLink1, strLink2, strLink3, strLink1, strLink2, strLink3)

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
              'application under review'}
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
