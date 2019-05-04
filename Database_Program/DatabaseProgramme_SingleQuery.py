import cx_Oracle
from faker import Faker
import random
try:
   con=cx_Oracle.connect('system/auro@localhost/XE')
   cursor=con.cursor()
except cx_Oracle.DatabaseError as msg:
   print("Database error with message :",msg)
else:
   #query="insert into orders values(:ord_no,:purch_amt,:ord_date,:customer_id,:salesman_id)"
   with open ('salesman_data.txt','r')as f:
      for line in f.readlines():
         #cursor.execute('insert into orders values({0})'.format(line))
         cursor.execute('insert into salesman values({0})'.format(line))
         con.commit()
   print('record inserted successfully')
finally:
   if cursor:
      cursor.close()
      con.close()




