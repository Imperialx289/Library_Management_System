#!C:/Python39/Python
print("Content-Type:text/html")
print()
import cgi

print("<h1>Data Of Student Enter Successfully</h1>")
print("<body bgcolor='gray'>")



form = cgi.FieldStorage()
BookID = form.getvalue("BookID")
StudentName = form.getvalue("StudentName")
ContactNumber = form.getvalue("ContactNumber")


import mysql.connector

con = mysql.connector.connect(host='localhost', user='root', database='lms')
cur = con.cursor()

i = "insert into assign values(%s,%s,%s)"

t = (BookID,StudentName,ContactNumber)

cur.execute(i, t)

con.commit()

cur.close()
