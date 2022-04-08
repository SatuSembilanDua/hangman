import json
import pyfiglet

def load_json():
    f = open("data_db.json")
    data = json.load(f)
    f.close()
    return data
    
def load_engjson():
    f = open("data.eng.json")
    data = json.load(f)
    f.close()
    ret = []
    for x in data:
        ret.append(x)
    return ret

def huruf(jsondata):
    letter = input("Input huruf : ")
    panjang = input("Input Panjang : ")

    # validation
    panjang = "0" if panjang == "" else panjang
    if letter.isalpha() and panjang.isnumeric():
        panjang = int(panjang)
        let_set = set(letter)
        hasil = []
        for word in jsondata: 
            #print(set(word["kata"]))
            if all(x in let_set for x in set(word["kata"])): 
                if len(word["kata"]) > 2:
                    hasil.append(word)
             
        if panjang > 0 :
            hasil = [x for x in hasil if len(x["kata"]) == panjang]
        
        kata = []
        for x in hasil:
            if x["kata"] not in kata:
                kata.append(x["kata"])
        
        print(f"\nHasil ({len(kata)}) : \n")
        # print(kata)
        if len(kata) > 0 :
            prety(kata, 3)
        
        print()
        """
        for x in kata:
            print(x)
        """

def prety(data, col):
    res = []
    for x in range(0, len(data), col):
        slice_itm = slice(x, x + col, 1)
        res.append(data[slice_itm])
    col_width = max(len(word) for row in res for word in row) + 10
    for x in res:
        print("".join(word.ljust(col_width) for word in x))
    """
    for row in res:
        print("{: >20} {: >20} {: >20}".format(*row))
    """
    
def enghuruf(jsondata):
    letter = input("Input huruf : ")
    panjang = input("Input Panjang : ")

    # validation
    panjang = "0" if panjang == "" else panjang
    if letter.isalpha() and panjang.isnumeric():
        panjang = int(panjang)
        let_set = set(letter)
        hasil = []
        for word in jsondata: 
            #print(set(word["kata"]))
            if all(x in let_set for x in set(word)): 
                if len(word) > 2:
                    hasil.append(word)
             
        if panjang > 0 :
            hasil = [x for x in hasil if len(x) == panjang]
            
        print(f"\nHasil ({len(hasil)}) : \n")
        # print(kata)
        if len(hasil) > 0 :
            prety(hasil, 3)
    

def test():
    kat = "abadi"
    let_set = set(kat)
    print(let_set)
    print(set(kat))
    i = 1
    for word in load_json(): 
        print(str(i)+" "+word["kata"])
        for x in set(word["kata"]):
            print(x, end=" ")
        print()
        if i == 21:
            break
        i+=1
        
    

if __name__ == "__main__":
    #huruf()
    #test()
    #eng = load_engjson()
    #enghuruf(eng)
    while True:
        ascii_banner = pyfiglet.figlet_format("=Find Words=")
        print(ascii_banner)
        print("Menu : ")
        print("  1. Indo")
        print("  2. English")
        print("  3. Keluar")
        men = input("Pilih Menu : ")
        if not men.isnumeric():
            break
        if men == "1":
            da = load_json()
            while True:
                print()
                huruf(da)
                print()
                ext = input("lanjut (y/n) : ")
                if ext != "y":
                    break
        elif men == "2":
            da = load_engjson()
            while True:
                print()
                enghuruf(da)
                print()
                ext = input("lanjut (y/n) : ")
                if ext != "y":
                    break
        else:
            break