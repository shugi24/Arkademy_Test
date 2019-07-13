

# Jawaban Nomor 3 #

def hitungKata():
    string = input(str("Masukan String yang diinginkan: "))
    frasa = input(str("Masukan Frasa yang diinginkan: "))

    
    if len(frasa)>len(string):
        return print("\nKata/Frasa tidak boleh lebih panjang dibandingkan string.\n")
    else:
        return print("\nDitemukan %s kali.\n" % (string.count(frasa)))

hitungKata()


# def hitungKata(string, frasa):    
#     if len(str(frasa))>len(str(string)):
#         return print("Kata/Frasa tidak boleh lebih panjang dibandingkan string")
#     else:
#         return print("\nDitemukan %s kali\n" % (string.count(frasa)))

#hitungKata('kucing', 'gn')
