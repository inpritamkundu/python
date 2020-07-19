# for tls use server.starttls() before login


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders
import os


# for plain mesage
# fromaddr = "noreply@teckat.com"
# toaddr = "jiaarohi2512@gmail.com"
# msg = MIMEMultipart()
# msg['From'] = fromaddr
# msg['To'] = toaddr
# msg['Subject'] = "Test Subject"
# body = "Write your message here"
# msg.attach(MIMEText(body, 'plain'))
# server = smtplib.SMTP_SSL('smtp.zoho.in:465')
# server.login(fromaddr, "hic996nZYet5")
# text = msg.as_string()
# server.sendmail(fromaddr, toaddr, text)
# server.quit()


# attach image
# path = os.path.join(os.getcwd(), 'src', 'emailSmtp', 'originalCertificate.jpg')
# print(path)
# print(os.path.basename(path))
# fromaddr = "noreply@teckat.com"
# toaddr = "jiaarohi2512@gmail.com"
# msg = MIMEMultipart()
# msg['From'] = fromaddr
# msg['To'] = toaddr
# msg['Subject'] = "Test Subject"
# img_data = open(path, 'rb').read()
# image = MIMEImage(img_data, name=os.path.basename(path))
# msg.attach(image)
# server = smtplib.SMTP_SSL('smtp.zoho.in:465')
# server.login(fromaddr, "hic996nZYet5")

# server.sendmail(fromaddr, toaddr, msg.as_string())
# server.quit()


# text + image
path = os.path.join(os.getcwd(), 'src', 'emailSmtp', 'workshop.xlsx')
print(path)
print(os.path.basename(path))
fromaddr = "noreply@teckat.com"
toaddr = "jiaarohi2512@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Test Subject"
body = ''' hello
This is pritam
    CEO Teckat'''
msg.attach(MIMEText(body, 'plain'))

# image attachment
# img_data = open(path, 'rb').read()
# image = MIMEImage(img_data, name=os.path.basename(path))
# msg.attach(image)


# pdf attachment

# open the file to be sent
filename = "test.xlsx"
attachment = open(path, "rb")

# instance of MIMEBase and named as p
p = MIMEBase('application', 'octet-stream')

# To change the payload into encoded form
p.set_payload((attachment).read())

# encode into base64
encoders.encode_base64(p)

p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

# attach the instance 'p' to instance 'msg'
msg.attach(p)


server = smtplib.SMTP_SSL('smtp.zoho.in:465')
server.login(fromaddr, "hic996nZYet5")

server.sendmail(fromaddr, toaddr, msg.as_string())
server.quit()
