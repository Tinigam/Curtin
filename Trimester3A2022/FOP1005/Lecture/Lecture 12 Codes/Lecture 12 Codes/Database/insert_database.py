import sqlite3

data = [("John", "Lim", 20, 1.73, 65.7),
        ("Peter", "Tan", 21, 1.83, 87.9)]

con = sqlite3.connect("patient_data.sqlite")
stmt = "INSERT INTO patient VALUES(?,?,?,?,?)"
con.executemany(stmt, data)
con.commit()
con.close()

print("Data inserted into Database")
