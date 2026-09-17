smtplib module:
---------------
--> This module is used to send a mail without using mail or outlook by running the python Code 
-->here by using this mail 'smtp.gmail.com'and this port '587'
------------------------------------------------------
Sending Mail using Python:
--------------------------
import smtplib

sender_email ='garaprasad116@gmail.com'
sender_app_password ='ycjo nzuv mkhk ktuk'
receiver_email = 'garadurgaprasad18@gmail.com'

message = """
Hello,

this mail was sent using python

regards
python team
"""
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender_email,sender_app_password)
server.sendmail(sender_email,receiver_email,message)
server.quit()
print('Email sent successfully')
-------------------------------------------------------------------------
Sending Mail using Python with Subject:
----------------------------------------
import smtplib
from email.message import EmailMessage

msg = EmailMessage()
sender_email = 'garaprasad116@gmail.com'
sender_app_password = 'ycjo nzuv mkhk ktuk'
receiver_email = 'bunnyjanga.ai@gmail.com'

msg['from'] = sender_email
msg['to'] = receiver_email
msg['subject'] = 'Python module'
msg.set_content(""" Hello, This is Prasad,
Testing Python module
regards
Python team """)
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender_email,sender_app_password)
server.send_message(msg)
server.quit
print('Email sent successfully')
----------------------------------------------------------
Sending Mail using Python with Subject & attachments:
------------------------------------------------------
import smtplib
from email.message import EmailMessage

msg = EmailMessage()
sender_email = 'garaprasad116@gmail.com'
sender_app_password = 'ycjo nzuv mkhk ktuk'
receiver_email = 'bunnyjanga.ai@gmail.com'

msg['from'] = sender_email
msg['to'] = receiver_email
msg['subject'] = 'Python module'
msg.set_content(""" Hi Bunny anna,
okka backdoor job chudu anna
regards
Codegnan family """)

with open(r"C:\Users\garap\OneDrive\Documents\Desktop\PFS\Python\PRASAD RESUME.pdf",'rb') as file:
    file_content = file.read()
    msg.add_attachment(
        file_content,
        maintype='application',
        subtype='pdf',
        filename='PRASAD RESUME.pdf'
    )
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender_email,sender_app_password)
server.send_message(msg)
server.quit
print('Email sent successfully')
--------------------------------------------------------------------------
