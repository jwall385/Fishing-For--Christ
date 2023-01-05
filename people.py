print("HTTP/1.0 200 OK\n")
import cgi
form = cgi.FieldStorage()
fname=form.getvalue('fname')
lname=form.getvalue('lname')

print(fname)
print(lname)