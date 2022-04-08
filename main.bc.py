import os
from lib.game import main_game
from lib.menu import *
from getpass import getpass
import json
import sqlite3

con = sqlite3.connect('data.db')
cur = con.cursor()
player = {}

def main():
	while True:
		cls_scrn()
		welcome_massage(player)
		print("  Menu :")
		print("  1. Main level Mudah  		(20 Kali Percobaan)")
		print("  2. Main level Medium 		(15 Kali Percobaan)")
		print("  3. Main level Susah 	 	(10 Kali Percobaan)")
		print("  4. Main level Sangat Susah 	( 5 Kali Percobaan)")
		print("  5. History")
		print("  6. Keluar")
		print("  Pilih Menu (1-6) : ",end="")
		menu = input()
		if menu == "1" or menu == "2" or menu == "3" or menu == "4":
			lvl = int(menu)
			mainkan(lvl)
		elif menu == "5":
			print("history")
		elif menu == "6" or menu=="q":
			quit()
			exit()
		else:
			print("Masukan Salah!!")

def mainkan(lvl):
	lvl = int(lvl)
	while True:
		game = main_game(lvl, cur, player)
		statistic = game.mainkan()
		# print(statistic)
		add_history(statistic)
		menu = input("Main Lagi? (y/n) : ")
		if menu != "y" and menu != "" and menu != " " and menu != "Y": 
			break 

def add_history(data):
	
	try:
		sql = f"INSERT INTO tblhistory (id_user, kata, hasil, percobaan, waktu_mulai, waktu_selesai, skor) VALUES ('{player['id']}', '{data['kata']}', '{data['hasil']}', {data['percobaan']}, '{data['waktu_mulai']}', '{data['waktu_selesai']}', {data['skor']})"
		cur.execute(sql)
	except sqlite3.Error as er:
		ini = "1"
		print("ERROR INSERT History")
		print(f"\n{sql}\n")
		print('SQLite error: %s' % (' '.join(er.args)))
		print("Exception class is: ", er.__class__)
		print('SQLite traceback: ')
		exc_type, exc_value, exc_tb = sys.exc_info()
		print(traceback.format_exception(exc_type, exc_value, exc_tb))
	finally:
		con.commit()
		update_score(data['skor'])

def update_score(skor):
	sql = f"SELECT score FROM tbluser WHERE id_user = '{player['id']}' "
	q = cur.execute(sql)
	for row in q:
		skor += row[0]

	sql = f"UPDATE tbluser SET score = {skor} WHERE id_user = '{player['id']}' "
	try:
		player["score"] = skor
		cur.execute(sql)
	except sqlite3.Error as e:
		ini = "1"
	finally:
		con.commit()

def daftar_user():
	psntype = ""
	while True:
		login_msg(psntype)
		print("  Daftar")
		namau = input("  Nama : ")
		usern = input("  Username : ")
		passw = getpass("  Password : ")
		rpass = getpass("  Re-Password : ")
		if namau != "" or usern != "" or passw != "" or (passw!=rpass):
			sql = f"INSERT INTO tbluser (username, password, nama, score) VALUES ('{usern}', '{passw}', '{namau}', 0)"
			try:
				cur.execute(sql)
			except sqlite3.Error as e:
				psntype = "1"
			finally:
				con.commit()
				break
		else:
			psntype = "1"

def proc_login():
	psntype = ""
	while True:
		login_msg(psntype)
		print("  Login")
		usern = input("  Username : ")
		passw = getpass("  Password : ")
		sql = f"SELECT * FROM tbluser WHERE username = '{usern}' AND password = '{passw}' "
		q = cur.execute(sql)
		con = 0
		for row in q:
			player["id"] = row[0]
			player["username"] = row[1]
			player["password"] = row[2]
			player["nama"] = row[3]
			player["score"] = row[4]
			con+=1
		print(con)
		if con > 0:
			break
		else:
			psntype = "3"
		# print(player)


def login_menu():
	while True:
		login_msg("")
		print("  Menu :")
		print("  1. Login")
		print("  2. Daftar")
		print("  3. Keluar")
		logmenu = input("  Pilih Menu (1-3) : ")
		if logmenu == "1":
			proc_login()
			break
		elif logmenu == "2":
			daftar_user()
		elif logmenu == "3":
			quit()
			exit()
		else:
			print("")

def load_data_user():
	data = []
	with open('user.json') as f:
		data = json.load(f)

if __name__ == '__main__':
	# print("MAIN : ")
	# print(player)
	# print(type(player))
	# print(player["username"])
	
	login_menu()
	main()

	# player = {"id": "3",
	# 		"username": "asd",
	# 		"password": "asd",
	# 		"nama": "asd",
	# 		"score": 0}
	# game = main_game(5, cur, player)
	# game.mainkan()


