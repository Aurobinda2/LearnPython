import smtplib
import os
from email.message import EmailMessage
import imghdr

email=os.environ.get('email')
password=os.environ.get('password')

message=EmailMessage()
message['from']=email
message['to']='aurobindr.nayak3@gmail.com'
message['subject']='Another way of sending email '
message.content="This a different way of sending email using 'Email Message' library "

with open('E:/SMTP/doc1.docx','rb') as f:
    file_data=f.read()
    file_name=f.name
    file_type=imghdr.what(file_name)
    #print(file_type)
message.add_attachment(file_data,maintype='application',subtype='octet-stream',filename=file_name)
with  smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(email,password)
    smtp.send_message(message)



