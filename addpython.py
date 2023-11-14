#!C:/Python39/Python
print("Content-Type:text/html")
print()
import cgi

print("<h1>Data Enter Successfully</h1>")
print("<body bgcolor='gray'>")



form = cgi.FieldStorage()
BookID = form.getvalue("BookID")
BookName = form.getvalue("BookName")
BookQuantity = form.getvalue("Book Quantity")


import mysql.connector

con = mysql.connector.connect(host='localhost', user='root', database='lms')
cur = con.cursor()

i = "insert into available values(%s,%s,%s)"

t = (BookID,BookName,BookQuantity)

cur.execute(i, t)

con.commit()

cur.close()
