import mysql.connector

connect = mysql.connector.Connect(host = "localhost", user = "root", password = "Nellie@123!", database = "classicmodels")
c = connect.cursor()

print("""1: San Fransisco
2: Boston
3: NYC
4: Paris
5: Tokyo
6: Sydney
7: London""")
moved_office = input("Which office has moved to a new country: ")
sql = "select * from offices where officeCode = '" + moved_office + "';"
c.execute(sql)
result = c.fetchall()
new_location = input("The (" + str(result[0][1] + ") office new country is: "))

if new_location != "":
    sql = "update offices set country = '" + new_location + "' where officeCode = '" + moved_office + "';"
    c.execute(sql)
    connect.commit()
    connect.close()
    




