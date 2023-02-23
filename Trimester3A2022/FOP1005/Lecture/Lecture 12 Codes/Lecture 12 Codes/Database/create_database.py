
import sqlite3

query = """
CREATE TABLE patient
(first_name VARCHAR(50),
	last_name VARCHAR(50),
	age INTEGER,
	height REAL,
	weight REAL
)"""

con = sqlite3.connect("patient_data.sqlite")
con.execute(query)
con.commit()
con.close()

print("Database and table created")
