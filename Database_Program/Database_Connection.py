import cx_Oracle

try:
   con=cx_Oracle.connect('system/password@localhost/XE')
   cursor=con.cursor()

except cx_Oracle.DatabaseError as msg :
   print("Database connection fail with error msg : ", msg)
else:
   print('Database connection successful.......')

finally:
   if cursor:
      cursor.close()
      con.close()


