import mysql.connector

connect = mysql.connector.Connect(host = "localhost", user = "root", password = "Nellie@123!", database = "idrottsklubb")
c = connect.cursor()

förnamn = input('Vad heter du i förnamn: ')
efternamn = input('Vad heter du i efternamn: ')
säsongskort = input('Vill du ha ett säsongskort (JA eller NEJ): ')
klubb = int(input("Vilken klubb vill du bli medlem i? \n1: Chelsea\n7: Färjestad\n9: New England Patriots\n14: Chicago Bulls\n-> "))
sql = "insert into medlemmar (förnamn, efternamn, säsongskort, medlemI) values (%s, %s, %s, %s);"
val = (förnamn, efternamn, säsongskort, klubb)
c.execute(sql, val)
connect.commit()
print(c.rowcount, "record inserted.")