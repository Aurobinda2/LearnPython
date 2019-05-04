import cx_Oracle
from faker import Faker
import random
try:
   con=cx_Oracle.connect('system/auro@localhost/XE')
   cursor=con.cursor()
except cx_Oracle.DatabaseError as msg:
   print("Database error with message :",msg)
else:
   query="insert into customer values(:customer_id,:cust_name,:city ,:grade ,:salesman_id)"
   records = [
              (3002,  'Nick Rimando','New York',100,5001),
              (3005, 'Graham Zusi', 'California', 200, 5002),
              (3004, 'Fabian Johns', 'Pari', 300, 5006),
              (3007, 'Brad Davis', 'New York', 200, 5001),
              (3009, 'Geoff Camero', 'Berlin', 100, 5003),
              (3008, 'Julian Green', 'London', 300, 5002),
              (3003, 'Jozy Altidor', 'Moscow', 200, 5007)]

   cursor.executemany(query,records)
   con.commit()
   print('record inserted successfully')
finally:
   if cursor:
      cursor.close()
      con.close()




