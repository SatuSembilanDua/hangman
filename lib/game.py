from random import randint, randrange, sample, shuffle
import json
from lib.menu import *
import datetime

class main_game:
	lvl = 1
	data = []
	length_data = 0
	attempt = 20
	kata = ""
	clues = []
	guesses = ""

	def __init__(self, lvl, cur, player):
		self.lvl = lvl
		self.cur = cur
		self.player = player
		self.load_data()
		self.load_attempt(lvl)
		self.load_rand_data()

	def load_data(self):
		# with open('../data.json') as f:
		# with open('data.json') as f:
		# 	self.data = json.load(f)
		# self.length_data = len(self.data)
		sql = "SELECT * FROM tblkata WHERE LENGTH(kata) >= 4 AND LENGTH(kata) <= 6 AND clues != ''"
		q = self.cur.execute(sql)
		for row in q:
			self.data.append({"kata":row[1], "clue":row[2]})
		self.length_data = len(self.data)

	def load_attempt(self, lvl):
		if lvl == 1:
			self.attempt = 20
		elif lvl == 2:
			self.attempt = 15
		elif lvl == 3:
			self.attempt = 10
		else:
			self.attempt = 5

	def load_rand_data(self):
		pointer = randrange(0, self.length_data)
		tmp = self.data[pointer]
		self.kata = tmp["kata"]
		self.clues = tmp["clue"].split("|")

	def cek_banner(self):
		game_message(1, 10)

	def get_time(self):
		x = datetime.datetime.now()
		y = x.strftime("%Y-%m-%d %H:%M:%S")
		return y

	def mainkan(self):
		word = self.kata
		guesses = ''
		turns = self.attempt
		numc = 0
		gtype = 0
		coba = 0
		hist_guess = ''
		waktu_mulai = self.get_time()
		while turns > 0:     
			game_message(gtype, f"{turns}")
			cl = len(self.clues)
			#print(f" * Kata : {self.kata}")
			print(f" * Petunjuk : {self.clues[numc]} \n")
			numc = numc + 1 if numc < cl-1 else 0
			failed = 0   
			print("\t", end="")          
			for char in word:      
				if char in guesses:    
					print(char, end=" ")
				else:
					print("_", end=" ")
					failed += 1    

			print("")
			if failed == 0:       
				gtype = 1
				da = self.attempt - turns
				game_message(gtype, coba)
				break              

			print("")
			guess = input("Tebak huruf : ") 

			if guess == "qq":
				game_message(4, word)
				break

			if len(guess)>1:
				if guess != word:
					turns -= 1
					gtype = 5
					coba+=1
				else:
					failed = 0
					game_message(1, coba)
					break  
			else:
				guesses += guess  
				gtype = 0                  
				if guess not in word:  
					coba+=1
					if guess not in hist_guess:
						hist_guess += guess
						turns -= 1        
					gtype = 3
			if turns == 0:           
				gtype = 2
				game_message(gtype, word)
				break

		skor = self.calc_score(turns, len(self.kata)) if failed == 0 else 0
		statistic = {
			"kata": self.kata,
			"hasil": "SUCCESS" if failed==0 else "FAILED",
			"percobaan": coba,
			"turn": turns,
			"waktu_mulai": waktu_mulai,
			"waktu_selesai": self.get_time(),
			"skor": skor,
		}
		# game_message(6, statistic)
		print_statistik(statistic)
		return statistic		

	def calc_score(self, coba, kata):
		percoba = coba - kata
		# print(f"(( {self.attempt} - ( {coba} - 1 )))")
		# skor = ( (self.attempt - percoba ) / self.attempt) * 100
		skor = ( coba / self.attempt) * 100
		return skor

if __name__ == '__main__':
	mg = main_game(20)
	# print(mg.kata)
	# print(mg.clues)

