from random import * #*все функции // * as rd переименование функции
#import random -> random.randint()
from math import * #pi kastutamiseks
#Ülesanne 1
# print("Hello World!")
# nimi=input("What's your name?").capitalize() #lower()-aaa, #upper()-AAA #capitalize()-Aaa
# print("Hello World! Greeetings! How's your day", nimi, "?")
# print("Hello World! Greeetings! How's your day "+ nimi, "?")
# vanus=int(input("How old are you? "))
# print("Hello World! Greetings! "+nimi+" You're",vanus, "years old!")
# print(f"\tHello World! \nGreetings! {nimi} You're {vanus} years old!") #f даёт возможность использовать фигурные скобки, \t Красная строка \n Новая строка


#Ülesanne 2
# vanus = 18
# eesnimi = "Jaak"
# pikkus = 16.5
# kas_käib_koolis = True
# print(type(vanus), \ntype(eesnimi), type(pikkus), type(kas_käib_koolis))

#Ülesanne 3
# kokku=randint(1,1000)
# print(f"Kokku on {kokku} kommi")
# kommi=int(input("Mitu kommi sa tahad?"))
# kokku=kokku-kommi
# print(f"Jääk on {kokku} kommi")

#Ülesanne 4
# print("Läbimõõdu leidmine ")
# #l-ümbermõõt
# l=float(input("Ümbermõõt: "))
# #d-läbimõõt
# d=l/pi
# print(f"Läbimõõdu suurus on {round(d,2)}")

#Ülesanne 5
a = float(input("Sisestage külje a pikkus (meetrites): "))
b = float(input("Sisestage külje b pikkus (meetrites): "))

d = sqrt(a**2 + b**2)
print(f"Ristkülikukujulise maatüki diagonaal on: {round(d,2)}m")

#Ülesanne 6
aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = teepikkus / aeg

print(f"Sinu kiirus oli " + str(round(kiirus,2)) + " km/h")

#Ülesanne 7
print("Peate sisestama 5 täisarvu")

a = int(input("Sisesta esimest täisarvu: "))
b = int(input("Sisesta teist täisarvu: "))
c = int(input("Sisesta kolmandat täisarvu: "))
d = int(input("Sisesta neljat täisarvu: "))
e = int(input("Sisesta viiet täisarvu: "))

keskmine = (a + b + c + d + e) / 5
print(input(f"Teie sisestatud numbrites keskmine on: {keskmine}"))

#Ülesanne 8
print(input("Kas tahate, ma näitan teile konna?"))
print(f"    @..@ \n   (----)\n  ( \__/ )\n   ^^ "" ^^")
print(input("Kas tahate, ma näitan veel teile midagi :)?"))
print(f"    /)/) \n   (O.O)\n  (,)_(,) \n  (^)_(^)")

#Ülesanne 9
print("Arvutame kolmnurga ümbermõõdu: ")
print("Matemaatikast teame, et ümbermõõdu valem on P = a + b + c: ")

a1 = float(input("Sisesta a: "))
b1 = float(input("Sisesta b: "))
c1 = float(input("Sisesta c: "))

P = a1 + b1 + c1
print(input(f"Kolmnurga ümbermõõt on: {round(P,2)}"))

#Ülesanne 10
print(f"Võtsime Zhenjaga pitsat! \n Pitsa maksis meile 12.90€")
tips = float(12.90 * 0.1)
maks = float((12.90 + tips)/ 2)
print(input(f"Igaüks meist peab maksma {round(maks,2)}€, sest peale pitsa rahat, me andsime veel {tips}€ jooraha!"))

