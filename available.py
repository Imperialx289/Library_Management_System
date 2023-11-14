#!C:/Python39/Python
print("Content-Type:text/html")
print()
import cgi
print("<body bgcolor='lightblue'>")

import mysql.connector

con = mysql.connector.connect(host='localhost', user='root', database='lms')
cur = con.cursor()

# Fetch data based on the provided name and roll number
cur.execute("SELECT * FROM available")
data = cur.fetchall()

cur.close()

print("<table border='1' align=center>")
print("<tr><th>Roll No</th><th>Name</th><th>Address</th></tr>")

if data:
    for row in data:
        print("<tr>")
        print("<td>{}</td>".format(row[0]))  
        print("<td>{}</td>".format(row[1]))  
        print("<td>{}</td>".format(row[2]))  # Assuming the third column is the address
        print("</tr>")
else:
    print("<tr>")
    print("<td colspan='3'>No matching data found. Please try again.</td>")
    print("</tr>")

print("</table>")
