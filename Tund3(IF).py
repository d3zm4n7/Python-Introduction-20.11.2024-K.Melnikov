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