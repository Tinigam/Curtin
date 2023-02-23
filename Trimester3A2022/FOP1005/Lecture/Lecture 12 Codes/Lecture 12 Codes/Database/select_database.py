import sqlite3

con = sqlite3.connect("patient_data.sqlite")
cursor = con.execute("SELECT * FROM patient")
rows = cursor.fetchall()

for i in range(len(rows)):
	print(rows[i])

con.close()
