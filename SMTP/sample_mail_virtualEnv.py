import smtplib
import os
email=os.environ.get('email')
password=os.environ.get('password')

with  smtplib.SMTP('localhost',1025) as smtp:

    smtp.login(email,password)
    subject='This is a test message to check SMTP lib functionality'
    body='Hello ...How are you ?'
    msg="subject:{0}\n\n{1}".format(subject,body)
    smtp.sendmail(email,'aurobindr.nayak3@gmail.com',msg)
