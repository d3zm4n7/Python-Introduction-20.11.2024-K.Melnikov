import string #
# vokaali=["a","e","u","o","i","ü","ö","õ","ä"] #гласные
# konsonanti="qwrtpsdfghklzxcvbnm" #согласные
# markid=string.punctuation #функция пунктуации из библиотеки string !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

# while True:
#     v=k=m=t=0
#     tekst=input("Sisetage mingi tekst: ").lower()
#     if tekst.isdigit(): 
#         break #если ввели цифру, то программа остановится
#     else:
#         tekst_list=list(tekst) #преобразует в ['t', 'e', 'k', 's', 't']
#         print(tekst_list) #['P', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'e', 'e', 'r', 'i', 'm', 'i', 'n', 'e']
#         for taht in tekst_list:
#             if taht in vokaali:
#                 v+=1
#             elif taht in konsonanti:
#                 k+=1
#             elif taht in markid or taht=="ˇ":
#                 m+=1
#             elif taht ==" ":
#                 t+=1
#     print("Vokaali:", v)
#     print("Konsonanti:", k)
#     print("Markid:", m)
#     print("Tühikud:", t)

# #Ül2
# nimed=[]
# for i in range(5):
#     nimi=input(f"{i+1}.Nimi: ")
#     nimed.append(nimi)
# print("Enne sorteerimist")
# print(nimed)

# nimed.sort()
# print("Peale sorteerimist")
# print(nimed)
# print(f"Viimasena kusatud nimi on: {nimi}") #{nimed[4]}, {nimed[-1]},
# v=input("Kas muudame nimed?: ").lower()
# if  v=="jah":
#     v=input("Nime või positsioon? N/P: ").upper()
#     if v=="P":
#         print("Sisesta nime asukoht: ")
#         v=int(input())
#         print(f"{nimed[v-1]}?")
#         uus_nimi=input("Sisesta uus nimi: ")
#         nimed[v-1]=uus_nimi
#         print(nimed)
#     else: #elif
#         print("Sisesta nimi")
#         vana_nimi=input("Vana nimi: ")
#         v=nimed.index(vana_nimi)
#         uus_nimi=input("Uus nimi: ")
#         nimed[v]=uus_nimi
#     print(nimed)
# # dublikaatid 1
# dublta=list(set(nimed))
# print("Mitte korduv loetelu 1.variant")
# print(dublta)
# # dublikaatid 2
# dublta=[]
# for nimi in nimed:
#     if nimi not in dublta:
#         dublta.append(nimi)
# print("Mitte korduv loetelu 2.variant")
# print(dublta)

# vanused=[]
# for i in range(7):
#     vanus=int(input(f"{i+1}. Vanus: "))
#     vanused.append(vanus)
# print(f"Sisestatud vanused: {vanused}")
# print(max(vanused)) #maximum
# print(min(vanused)) #minimum
# print(sum(vanused)/len(vanused)) #len количество значений / средний значения

# värtused=[]
# read=int(input("Reade arv: "))
# for i in range(read):
#     arv=int(input(f"{i+1} Arv: "))
#     värtused.append(arv)
# print(värtused)
# s=input("Sümbol: ") #s="*"
# for vartus in värtused:
#     print(vartus*s)
# print()

indexid=["Tallinn","Narva, Narva-Jõesuu","Kohtla-Järve","Ida-Virumaa, Lääne-Virumaa, Jõgevamaa","Tartu linn","Tartumaa, Põlvamaa, Võrumaa, Valgamaa"
"Viljandimaa,Järvamaa, Harjumaa, Raplamaa","Pärnumaa", "Läänemaa, Hiiumaa, Saaremaa"]
while 1:
    try:
        postiindex=int(input("Postiindeks: "))
        if len(str(postiindex))==5:
            break
        else:
            print("Indeks sisaldab 5 numbritest!")
    except:
        print("!!!")
print("Postiindeksi analüüs: ")
index_list=list(str(postiindex)) #"1","2","3"...
s1=int(index_list[0]) #1
print(f"Postiindeks {postiindex} on {indexid[s1-1]} ") #12345 Tallinn
    
 
