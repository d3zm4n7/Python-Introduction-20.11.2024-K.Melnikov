from datetime import *
from math import *
from calendar import *
from random import *

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
R=random()*100 #0.0...1.0 R=int(random()*100) R=round(random()*100)
print(f"R={R}")
Sk=pi*R**2
Lk=2*pi*R
Skv=(2*R)**2
Lkv=(2*R)*4
print(f"Ringi pindala on {Sk}\nRingu ümbermõõt pn {Lk}\nRuudu pindala on {Skv}\nRuudu ümbermõõt on {Lkv}")