import os
from lib.game import main_game
from lib.menu import *
from getpass import getpass
import json

def main():
	while True:
		cls_scrn()
		welcome_massage()
		print("  Menu :")
		print("  1. Main level Mudah  		(20 Kali Percobaan)")
		print("  2. Main level Medium 		(15 Kali Percobaan)")
		print("  3. Main level Susah 	 	(10 Kali Percobaan)")
		print("  4. Main level Sangat Susah 	( 5 Kali Percobaan)")
		print("  5. Keluar")
		print("  Pilih Menu (1-5) : ",end="")
		menu = input()
		if menu == "1" or menu == "2" or menu == "3" or menu == "4":
			lvl = int(menu)
			mainkan(lvl)
		elif menu == "5" or menu=="q":
			quit()
			exit()
		else:
			print("Masukan Salah!!")

def mainkan(lvl):
	lvl = int(lvl)
	while True:
		game = main_game(lvl)
		game.mainkan()
		menu = input("Main Lagi? (y/n) : ")
		if menu != "y":
			break 

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
			iniuser = {
				"nama":namau,
				"user":usern,
				"password":passw,
				"score":0
			}
			print(iniuser)
			break
		else:
			psntype = "1"

def login_menu():
	while True:
		login_msg("")
		print("  Menu :")
		print("  1. Login")
		print("  2. Daftar")
		print("  3. Keluar")
		logmenu = input("  Pilih Menu (1-3) : ")
		if logmenu == "1":
			login_msg("")
			print("  Login")
			usern = input("  Username : ")
			passw = getpass("  Password : ")
		elif logmenu == "2":
			daftar_user()
			break
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
	# login_menu()
	
	# main()

