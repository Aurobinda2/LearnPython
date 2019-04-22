import smtplib
import os
from email.message import EmailMessage

email=os.environ.get('email')
password=os.environ.get('password')

message=EmailMessage()
message['from']=email
message['to']='aurobindr.nayak3@gmail.com'
message['subject']='Another way of sending email '
message.content="This a different way of sending email using 'Email Message' library "

with  smtplib.SMTP_SSL('smtp.gmail.com','465') as smtp:
    smtp.login(email,password)
    smtp.send_message(message)



