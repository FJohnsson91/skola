import mysql.connector

connect = mysql.connector.Connect(host = "localhost", user = "root", password = "Nellie@123!", database = "classicmodels")
c = connect.cursor()

sql = "select * from employees;"
c.execute(sql)
result = c.fetchall()
print(result)
connect.close()