import json
import sqlite3


con = sqlite3.connect('data.db')
cur = con.cursor()

sql = "SELECT * FROM tblhistory a JOIN tblkata b ON a.kata = b.kata"

q = cur.execute(sql)

for row in q:
	ssts = row[3] if row[3] == "SUSSCESS" else row[3]+" "
	print(f"{row[2]} \t{ssts} \t{row[7]}")
	#print(json.dumps(row, indent=4))
