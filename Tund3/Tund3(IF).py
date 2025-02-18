# # Ülesanne 1

# nimi=input("Mis on sinu nimi? ")
# if nimi.isalpha() and nimi.isupper():
#     if nimi=="JUKU":
#         print("Lähme kinno")
#         try:
#             vanus=int(input(f"Kui vana sa oled {nimi}?"))
#             if vanus <0:
#                 print("Viga!")
#             elif vanus <= 6:
#                 print("Tasuta!")
#             elif vanus < 15:
#                 print("Lastepilet!")
#             elif vanus < 65:
#                 print("Täispilet!")
#             elif vanus < 100:
#                 print("Sooduspilet!")
#             else:
#                 print("Nii palju!!!")
#         except: 
#             print("Vale andmetüüp, sisesta täisarv!")
#     else:
#         print("Ootan Juku")
# else:
#     print("Segatud sõne")

# # Ülesanne 2
# nimi1=input("1. Mis on sinu nimi? ")
# nimi2=input("2. Mis on sinu nimi? ")
# nimed=["Gleb", "MariLuna", "Deniel", "Zhan", "Veronika"] #isascii() для Mari-Luna ## list of names
# if nimi1.isalpha() and nimi2.isalpha():
#     if (nimi1 in nimed) and (nimi2 in nimed):
#         print("Nad on pinginaabrid!")
#     else:
#         print("Pole pinginaabrid!")
# #2. variant
# if (nimi1=="Gleb" and nimi2=="Deniel") or (nimi1=="Deniel" and nimi2=="Gleb"):
#     print("Nad on pinginaabrid!")
# else:
#     print("Pole pinginaabrid!")

# # Ülesanne 3
# try:
#     a = float(input("Pikkus: "))
#     b = float(input("Laius: "))
#     S = a * b 
#     print(f"Põranda pindala on {S}m**2")
#     vastus=input("Kas tahad remondi teha?(Jah-1/Ei-0)") #Jah/Ei 1/0
#     if vastus.upper()=="JAH" or vastus=="1":
#         print("Teeme remondi!")
#         hind = float(input("Ühe meetri hind: "))
#         summa = S * hind
#         print(f"Remondi kulud {summa} EUR!")
#     elif vastus.upper()=="EI" or vastus == "0":
#         print("Ei tee remondi!")
#     else:
#         print("Ei saa aru!")
# except:
#     print("Numbrid!!!")

# #Ülesanne 4
# hind = float(input("Sisesta toote hind: "))
# if hind > 700:
#     soodukas = hind * 0.3
#     uus_hind = hind - soodukas
#     print(f"Soodustus on {soodukas:.2f} eurot. Lõpphind on {uus_hind:.2f} eurot.")
# else:
#     print("Soodust ei ole!")
        
# #Ülesanne 5
# temp = float(input("Sisesta temperatuuri: "))

# if temp < 18:
#     print(f"Temperatuur on {temp}! ")
# else:
#     print(f"Temperatuur on {temp}, see on rohkem kui keskmine talve toa temperatuur!")

# #Ülesanne 6
# pikkus = float(input("Sisesta enda pikkust: "))
# if pikkus < 150:
#     print("Sa oled väike mummi :D")
# elif pikkus <180:
#     print("Sul on tavalise inimese pikkus!")
# elif pikkus <200:
#     print("Sa oled päris pikk! :O")

#Ülesanne 7 - Küsi inimeselt pikkus ja sugu ning teata, kas ta on lühike, keskmine või pikk (mitu tingimusplokki võib olla üksteise sees).
try:
    pikkus2 = float(input("Sisesta enda pikkust: "))
    sugu = str(input("Sisesta enda sugu: (M/N)"))
    if sugu.upper = "M"
        
    if pikkus2 < 150:
      print("Sa oled väike mummi :D")
    elif pikkus2 <180:
        print("Sul on tavalise inimese pikkus!")
    elif pikkus2 <200:
        print("Sa oled päris pikk! :O")
except:
    print("Sisestasid valed andmed, ai ai ai!")