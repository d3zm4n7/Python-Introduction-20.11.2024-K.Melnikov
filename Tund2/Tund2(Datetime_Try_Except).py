from calendar import c
from datetime import *
from math import *
from calendar import *
from random import *
from re import A

# #Ülesanne 1
# paevadekogus=monthrange(2024,03)[1] #calendar funktsioonid
# tana = date.today() #funktsioon
# tanaf=date.today().strftime("%B %d, %Y")


# print(f"Tere! Täna on {tanaf}")
# d = tana.day #omadus
# m = tana.month
# y = tana.year
# print(d)
# print(m)
# print(y)

# detsP=monthrange(2024,12)[1]
# novP=monthrange(2024,11)[1]
# jaak=detsP+novP-d
# jaak2= novP-d

# print(f"Aasta lõppuni on {jaak}")
# print(f"Kuu lõppuni on {jaak2}")

# #Ülesanne 2
# var1 = 3 + 8 / ( 4 - 2 ) * 4 #originaal
# var2 = 3 + 8 / 4 - 2 * 4
# var3 = (3 + 8) / ( 4 - 2 ) * 4
# var4 = 3 + ( 8 / 4 - 2 * 4 ) 
# print(var1)
# print(var2)
# print(var3)
# print(var4)

#Ülesanne 3
#VARIANT 1
# try:
#     R=float(input("Sisesta R:"))
#     Sk=pi*R**2
#     Lk=2*pi*R
#     Skv=(2*R)**2
#     Lkv=(2*R)*4
#     print(f"Ringi pindala on {Sk}\nRingu ümbermõõt pn {Lk}\nRuudu pindala on {Skv}\nRuudu ümbermõõt on {Lkv}")
# except:
#     print("On vaja sisestada numbri!")

#VARIANT2
# R=random()*100 #0.0...1.0 R=int(random()*100) R=round(random()*100)
# print(f"R={R}")
# Sk=pi*R**2
# Lk=2*pi*R
# Skv=(2*R)**2
# Lkv=(2*R)*4
# print(f"Ringi pindala on {Sk}\nRingu ümbermõõt pn {Lk}\nRuudu pindala on {Skv}\nRuudu ümbermõõt on {Lkv}")

#Ülesanne 4
# d=2.575 # mündi d sm
# maa=6378 # maaradius km
# maa*=100000 # maaradius sm + maa=maa*100000
# Lmaa=2*pi*maa
# kogus=int(Lmaa/d) #
# print(f"On vaja {kogus} mündi!\nMeil on vaja {kogus*2} eur")

#Ülesanne 5
a1 = "kill-koll ".capitalize()
a2 = "killadi-koll ".capitalize()
print(f"{a1}{a1}{a2}{a1}{a1}{a2}{a1}{a1}{a1}{a1}")
# print(f"""kill-koll kill-koll killadi-koll kill-koll kill-koll killadi-koll kill-koll kill-koll kill-koll
# kill-koll""") #testimiseks panin print("""text""") selleks et see lause võttab 2 rida

#Ülesanne 6
y1 = "Rong see sõitis tsuhh tsuhh tsuhh,".upper()
y2 = "piilupart oli rongijuht.".upper()
y3 = "Rattad tegid rat tat taa,".upper()
y4 = "rat tat taa ja tat tat taa.".upper()
y5 = "Aga seal rongi peal,".upper()
y6 = "kas sa tead, kes olid seal?".upper()

y7 = "Rong see sõitis tuut tuut tuut,".upper()
y8 = "piilupart oli rongijuht.".upper()
y9 = "Rattad tegid kill koll koll,".upper()
y10 = "kill koll koll ja kill koll kill.".upper()
y11 = "....Sisend, väljund, tingimus....".upper()
print(f"{y1}\n{y2}\n{y3}\n{y4}\n{y5}\n{y6}\n\n{y7}\n{y8}\n{y9}\n{y10}\n\n\n\n{y11}")

#Ülesanne7
a = float(input("Palun sisestage esimene ristküliku külg: "))
b = float(input("Palun sisestage teine ristküliku külg: "))
Pr = 2 * (a + b)
Sr = a * b
print(f"Ristküliku ümbermõõt on {Pr} ja pindala on {Sr}!")

#Ülesanne 8
litres = float(input("Palun sisestage tangitud kütuse liitrid: "))
kms = float(input("Palun sisestage läbitud kilomeetrid: "))
kytusekulu = (litres / kms) * 100
print(f"Teie keskmine kütusekulu on {round(kytusekulu,2)}!")

#Ülesanne 9 - Rulluisutajad    Rulluisutaja keskmine kiirus on 29,9km/h    Kui kaugele jõuab M minutiga
minutid = float(input("Sisesta aeg minutites: "))
kiirus_kmh = 29.9
tunnid = minutid / 60
kaugus = kiirus_kmh * tunnid
print(f"Rulluisutaja jõuab {minutid} minutiga {round(kaugus,2)} kaugusele")

#Ülesanne 10 

minutid1 = int(input("Sisesta aeg minutites: "))
tunnid1 = minutid1 // 60
alles_minutid = minutid1 % 60
print(f"{tunnid1}:{alles_minutid}")
