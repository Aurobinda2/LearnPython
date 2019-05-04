import cx_Oracle as ora
try:
    con=ora.connect('system/auro@localhost/XE')
    cursor=con.cursor()
except ora.DatabaseError as msg:
    print('Database connection fail with error as :{0}'.format(msg))
else:
    try:
        query="insert into customer(customer_id,cust_name,city,salesman_id)values(3001,'Brad Guzan','London',5005) ; 'select * from customer where rownum<=4'"
        cursor.execute(query)
    except Exception as msg:
        print('Error while working on query with msg as {0}'.format(msg))
        con.rollback()
        print('Rollback successfully ....')
    else:
        print('Query successfully imported...')
        con.commit()
        print()
finally:
    if cursor:
        cursor.close()
        con.close()


