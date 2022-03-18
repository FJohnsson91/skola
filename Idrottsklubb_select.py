import mysql.connector

connect = mysql.connector.Connect(host = "localhost", user = "root", password = "Nellie@123!", database = "idrottsklubb")
c = connect.cursor()

sql = "select * from spelare;"
c.execute(sql)
result = c.fetchall()
print(result)
connect.close()
