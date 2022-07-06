from datetime import datetime
import pyodbc 
from fastapi import FastAPI



# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'tcp:myserver.database.windows.net' 
database = 'mydb' 
username = 'myusername' 
password = 'mypassword' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()


#Sample select query
cursor.execute("SELECT @@version;") 
row = cursor.fetchone() 
while row: 
    print(row[0])
    row = cursor.fetchone()

#Sample insert query VALUES (?,?,?,?,?)""",'SQL Server Express New 20', 'SQLEXPRESS New 20', 0, 0, CURRENT_TIMESTAMP).rowcount
count = cursor.execute("""
INSERT INTO SalesLT.Product (Name, ProductNumber, StandardCost, ListPrice, SellStartDate) 
VALUES (?,?,?,?,?)""",'SQL Server Express New 20', 'SQLEXPRESS New 20', 0, 0, datetime.utcnow()).rowcount
cnxn.commit()
print('Rows inserted: ' + str(count))


cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=mine;UID=me;PWD=pwd')


cnxn = pyodbc.connect(...)
# all uncommitted work will be discarded when the Connection object is closed. 
# You must call cnxn.commit() or your work will be lost
cnxn.commit()
cnxn.close()

cnxn.execute("insert into t1 values (?)", "x")
cnxn.execute("insert into t1 values (?)", "yy")

cnxn   = pyodbc.connect(...)
cursor = cnxn.cursor()
twoweeks = ""

cursor.execute("""
               select user_id, last_logon
                 from users
                where last_logon > ?
                  and user_type <> 'admin'
               """, twoweeks)

rows = cursor.fetchall()

for row in rows:
    print('user %s logged on at %s' % (row.user_id, row.last_logon))