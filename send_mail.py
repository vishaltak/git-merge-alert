#!/usr/bin/python

#This code was copied from https://ubuntuforums.org/showthread.php?t=1472520

import os, re
import sys
import smtplib
 
#from email.mime.image import MIMEImage
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.MIMEText import MIMEText

 
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

 
sender = 'myemail@gmail.com'
password = "mypass"
recipient = sys.argv[1]
subject = ''
message = sys.argv[3]
 
def main():
    msg = MIMEMultipart()
    msg['Subject'] = sys.argv[2]
    msg['To'] = recipient
    msg['From'] = sender
    
    
    part = MIMEText('text', "plain")
    part.set_payload(message)
    msg.attach(part)
    
    session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
 
    session.ehlo()
    session.starttls()
    session.ehlo
    
    session.login(sender, password)

    # Now send or store the message
    qwertyuiop = msg.as_string()

    session.sendmail(sender, recipient, qwertyuiop)
    
    session.quit()
    os.system('notify-send "Email sent"')
 
if __name__ == '__main__':
    main()