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
print("Läbimõõdu leidmine ")
#l-ümbermõõt
l=float(input("Ümbermõõt: "))
#d-läbimõõt
d=l/pi
print(f"Läbimõõdu suurus on {round(d,2)}")
