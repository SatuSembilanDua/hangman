import sqlite3
import json
con = sqlite3.connect('data.db')
cur = con.cursor()

# cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# data = []
# with open('data_db.json') as f:
# 	data = json.load(f)

# for da in data:
# 	kata = da['kata']
# 	clues = da['clues']
# 	desc = da['desc']
# 	sql = f"INSERT INTO tblkata (kata, clues, desc) VALUES ('{kata}', '{clues}', '{desc}') "
# 	cur.execute(sql)

# con.commit()
# con.close()

# sql = "SELECT * FROM tbluser WHERE username = 'admin' AND password = 'admin'"
# q = cur.execute(sql)
# data = []
# for row in q:
# 	data.append({
# 		"id":row[0],
# 		"username":row[1],
# 		"password":row[2],
# 		"nama":row[3],
# 		"score":row[4],
# 		})

# print(len(data))
# print(data)

# usern = "asd"
# passw = "asd"
# namau = "asd"

# sql = f"INSERT INTO tbluser (usernames, password, nama, score) VALUES ('{usern}', '{passw}', '{namau}', 0)"

# try:
# 	cur.execute(sql)
# 	print("SUCCESS")
# except sqlite3.Error as e:
# 	print(e)
# 	print("ERROR")
# finally:
# 	con.commit()


sql = "SELECT * FROM tblkata WHERE LENGTH(kata) >= 4 AND clues != ''"
q = cur.execute(sql)
data = []
for row in q:
	data.append({"kata":row[1], "clue":row[2]})

print(data)