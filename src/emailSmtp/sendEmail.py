# for tls use server.starttls() before login


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
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


# attach pdf


fromaddr = "noreply@teckat.com"
toaddr = "jiaarohi2512@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Test Subject"
with open(os.path.dirname(os.path.abspath(__file__))+'\\test.pdf') as f:
    attach = MIMEApplication(f.read(), _subtype="pdf")
server = smtplib.SMTP_SSL('smtp.zoho.in:465')
server.login(fromaddr, "hic996nZYet5")
attach.add_header('Content-Disposition', 'attachment',
                  filename=str(os.path.dirname(os.path.abspath(__file__)))+'\\test.pdf')
msg.attach(attach)
server.sendmail(fromaddr, toaddr, msg)
server.quit()
