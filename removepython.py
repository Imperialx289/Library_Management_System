#!C:/Python39/Python

print("Content-Type: text/html")
print()
import cgi
import mysql.connector

print("<html>")
print("<head>")
print("<title>Data Removal</title>")
print("</head>")
print("<body bgcolor='gray'>")

form = cgi.FieldStorage()
BookID = form.getvalue("BookID")
BookName = form.getvalue("BookName")


con = mysql.connector.connect(host='localhost', user='root', database='lms')
cur = con.cursor()

sql = "DELETE FROM available WHERE BookID=%s OR BookName=%s"
r = (BookID, BookName)
cur.execute(sql,r)

con.commit()

if cur.rowcount > 0:
    print("<h1>Data Removed Successfully</h1>")
else:
    print("<h1>No matching records found for deletion</h1>")

cur.close()
con.close()

print("</body>")
print("</html>")
