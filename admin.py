#!C:/Python39/Python
print("Content-Type:text/html")
print()
import cgi
print("<body bgcolor='lightblue'>")
import mysql.connector

con = mysql.connector.connect(host='localhost', user='root', database='lms')
cur = con.cursor()

cur.execute("SELECT * FROM admin")
data = cur.fetchall()

cur.close()

print("<table border='1' align=center>")
print("<tr><th>ID</th><th>Name</th><th>Contact</th><th>Address</th></tr>")

if data:
    for row in data:
        print("<tr>")
        print("<td>{}</td>".format(row[0]))  
        print("<td>{}</td>".format(row[1]))  
        print("<td>{}</td>".format(row[2]))  
        print("<td>{}</td>".format(row[3]))  
        print("</tr>")


print("</table>")
