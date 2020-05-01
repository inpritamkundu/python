# for tls use server.starttls() before login


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
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
path = os.path.join(os.getcwd(), 'src', 'emailSmtp', 'originalCertificate.jpg')
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
img_data = open(path, 'rb').read()
image = MIMEImage(img_data, name=os.path.basename(path))
msg.attach(image)
server = smtplib.SMTP_SSL('smtp.zoho.in:465')
server.login(fromaddr, "hic996nZYet5")

server.sendmail(fromaddr, toaddr, msg.as_string())
server.quit()
