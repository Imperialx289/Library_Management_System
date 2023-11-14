#!C:/Python39/Python
print("Content-Type:text/html")
print()
import cgi

print("<h1>Data Of Admin Recorded Successfully</h1>")
print("<body bgcolor='gray'>")



form = cgi.FieldStorage()
ID = form.getvalue("Id")
name = form.getvalue("name")
Contact = form.getvalue("Contact")
Address = form.getvalue("Address")

import mysql.connector

con = mysql.connector.connect(host='localhost', user='root', database='lms')
cur = con.cursor()

i = "insert into admin values(%s,%s,%s,%s)"

t = (ID,name,Contact,Address)

cur.execute(i, t)

con.commit()

cur.close()
