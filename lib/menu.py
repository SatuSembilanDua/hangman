import pyfiglet
import os, re
from colorama import Fore, Style, init
# from lib.game import Bbanner


init()

class Bbanner:
	border = "*"
	len_screen = 40
	message = ""
	warna = ""
	gaya = ""
	reset = ""

	def __init__(self, border="*", len_screen=40):
		self.border = border
		self.len_screen = len_screen

	def print_border(self):
		return (f"{self.border}"*self.len_screen)

	def print_space(self, with_border=True):
		_border = self.border if with_border else " "
		return (_border+(" "*(self.len_screen-2))+_border)

	def get_len(self, te):
		regex = r"\[\d+m"
		matches = re.findall(regex, te, re.MULTILINE)
		nelen = 0
		if len(matches) > 0:
			for m in matches:
				nelen += len(m)+1
		return len(te) - nelen

	def print_text(self, msg, align="left", with_border=True):
		len_msg = self.get_len(msg)
		len_screen = self.len_screen-4
		output = "your message exceeds the screen limit!"
		_border = self.border if with_border else " "
		if len_msg < len_screen:
			space = len_screen - len_msg
			if align=="center":
				space_ceter = int(space/2)
				output = f"{_border} "+(" "*space_ceter)+msg+(" "*space_ceter)+f" {_border}"
			elif align=="right":
				output = f"{_border} "+(" "*space)+f"{msg} {_border}"
			else:
				output = f"{_border} {msg}"+(" "*space)+f" {_border}"
		return output

	def gen_text(self, p):
		wr = ""
		gy = ""
		rs = ""
		if "warna" in p:
			wr = p["warna"]
			rs = "\033[0m"
		if "gaya" in p:
			gy = p["gaya"]
			rs = "\033[0m"

		msg = f"{gy}{wr}{p['msg']}{rs}"
		align = p["align"] if "align" in p else ""
		tb = self.print_text(p["msg"], align=align)
		tb = tb.replace("*", f"{self.gaya}{self.warna}*{self.reset}")
		tb = tb.replace(p['msg'], msg)
		return tb

	def gen_welcome(self, css={}, psn={}):
		ret = ""

		if len(css) > 0:
			self.warna = css["warna"] if "warna" in css else ""
			self.gaya = css["gaya"] if "gaya" in css else ""
			self.reset = "\033[0m"

		if len(psn) > 0:
			for p in psn:
				if type(p) is dict:
					ret += self.gen_text(p)+"\n"
					# print(tb)
				else:
					if p == "border":
						ret += f"{self.gaya}{self.warna}{self.print_border()}{self.reset}\n"
					elif p == "space":
						ret += f"{self.gaya}{self.warna}{self.print_space()}{self.reset}\n"
					else:
						ret += ""

		return ret


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


ascii_banner = pyfiglet.figlet_format("=Hangman=")
ban = Bbanner(len_screen=64, border="*")

_color = {
			"BLACK":Fore.BLACK,
			"RED":Fore.RED,
			"GREEN":Fore.GREEN,
			"YELLOW":Fore.YELLOW,
			"BLUE":Fore.BLUE,
			"MAGENTA":Fore.MAGENTA,
			"CYAN":Fore.CYAN,
			"WHITE":Fore.WHITE,		
		}
_style = {
			"NORMAL":Style.NORMAL,
			"DIM":Style.DIM,
			"BRIGHT":Style.BRIGHT,
			"RESET":Style.RESET_ALL
		}

def styled(msg, color="", style=""):
	color = color.upper()
	style = style.upper()
	warna = ""
	gaya = ""
	reset = ""
	if color in _color:
		warna = _color[color]
		reset = Style.RESET_ALL
	if style in _style:
		gaya = _style[style]
		reset = Style.RESET_ALL
	return (f"{gaya}{warna}{msg}{reset}")

def _print(msg="", color="", style="", align="", msg_type=1):
	if msg_type == 2:
		pesan = msg
		print(pesan)
		print(styled(ban.print_text(pesan, align=align), color, style))
	elif msg_type == 3:
		print(styled(ban.print_border(), color, style))
	elif msg_type == 4:
		print(styled(ban.print_space(), color, style))
	else:
		print(styled(msg, color, style))

def welcome_massage(player):
	_print(ascii_banner, color="blue", style="bright")
	css = {
		"warna":Fore.GREEN,
		"gaya":Style.BRIGHT,
		}
	mskore = "{:.2f}".format(player["score"])
	psn = [
			"border","space",
			{"msg":"Tebak Kata yang diberikan ", "align":"center", "warna":Fore.RED},
			"space",
			{"msg":f"Selamat datang : {player['nama']}"},
			{"msg":f"Skor terakhir anda : {mskore}"},
			"space",
			{"msg":"Cara Bermain : "},
			{"msg":"# Pilih level yang akan dimainkan."},
			{"msg":"# Akan diberikan beberapa petunjuk sebagai bantuan."},
			{"msg":"# Mulai tebak kata!"},
			"space","border"
		]
	print(ban.gen_welcome(css, psn))

def game_message(gtype, data=""):
	cls_scrn()
	_print(ascii_banner, color="blue", style="bright")
	css = {
		"warna":Fore.GREEN,
		"gaya":Style.BRIGHT,
		}

	psn = [
			"border","space",
			{"msg":"Masukan huruf yang anda tebak dibawah"},
			{"msg":"Jika menyerah ketikan \"qq\""}
		]

	print(ban.gen_welcome(css, psn),end="")

	print(ban.gen_welcome(css, ["space","border"]))
	if gtype == 5:
		_print(" [!] Masukan hanya 1 huruf!!", color="red")
		_print(f" [!] Kamu punya {data} tebakan lagi", color="blue", style="bright")
	elif gtype == 4:
		_print(" [!] Kamu Menyerah !!", color="red")
		print(f"\n Kata yang harus ditebak adalah : {data}\n")
	elif gtype == 3:
		_print(" [!] Tebakan Salah", color="red")
		_print(f" [!] Kamu punya {data} tebakan lagi", color="blue", style="bright")
	elif gtype == 2:
		_print(" [!] Kalah !!", color="red")
		print(f"\n Kata yang harus ditebak adalah : {data}\n")
	elif gtype == 1:
		_print(" [!] Horee !!", color="green", style="bright")
		_print(f" [!] Anda berhasil menebak dengan {data} kali tebakan salah !!", color="green", style="bright")
	else:
		print("")
	
	print("")

def print_statistik(data):
	# _print(f"  *  Hasil : {data['hasil']}", color="blue", style="bright")
	_print(f" [!] Statistik", color="blue")
	_print(f"  *  Kata          : {data['kata']}", color="CYAN", style="bright")
	_print(f"  *  Salah Tebak   : {data['percobaan']}", color="CYAN", style="bright")
	_print(f"  *  Sisa Tebak    : {data['turn']}", color="CYAN", style="bright")
	_print(f"  *  waktu mulai   : {data['waktu_mulai']}", color="CYAN", style="bright")
	_print(f"  *  waktu selesai : {data['waktu_selesai']}", color="CYAN", style="bright")
	_print(f"  *  Skor          : {data['skor']}", color="CYAN", style="bright")

def login_msg(pesan=""):
	cls_scrn()
	_print(ascii_banner, color="blue")
	css = {
		"warna":Fore.GREEN,
		"gaya":Style.BRIGHT,
		}

	ext_msg = {}
	if pesan=="1":
		ext_msg = {"msg":"Inputan Tidak valid!!", "warna":Fore.RED}
	elif pesan=="2":
		ext_msg = {"msg":"Pendaftaran berhasil!!", "warna":Fore.GREEN}
	elif pesan=="3":
		ext_msg = {"msg":"Login gagal, Username/Password Salah!!", "warna":Fore.RED}

	psn = [
			"border","space",
			{"msg":"Welcome ", "align":"center"}
		]
	if ext_msg:
		psn.append(ext_msg)
	psn.append("space")
	psn.append("border")

	print(ban.gen_welcome(css, psn),end="")

def quit():
	cls_scrn()
	_print(ascii_banner, color="blue")
	css = {
		"warna":Fore.GREEN,
		"gaya":Style.BRIGHT,
		}

	psn = [
			"border","space",
			{"msg":"Terima Kasih", "align":"center"},
			"space","border",
		]

	print(ban.gen_welcome(css, psn),end="")

def cls_scrn():
	os.system('cls' if os.name == 'nt' else 'clear')