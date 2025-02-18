print("*** Arvude mäng ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1:
    try:
        a = abs(int(input("Sisesta täisarv => ")))
        break
    except ValueError:
         print("See pole täisarv!")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a==0:
    print("Pole mõtted midagi teha nulliga!")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Loendame, mitu on paaris ja mitu paaritu arvu: ")
    print()
    c=b=a
    paaris = 0
    paaritu = 0
    while b > 0: # откидывает 10ки 
            if b % 2 == 0 :
                    paaris +=1
            else:
                    paaritu +=1
            b = b // 10

    print(f"Paaris arvude kogus: {paaris}")
    print(f"Paaritu arvude kogus: {paaritu}")
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*Ümberpöörame* sisestatud arv")
    print()
    b=0
    while a > 0:
        number = a % 10
        a = a // 10
        b = b * 10
        b += number
    print("*Ümberpööratud* arv", b)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Siracuse hüpoteesi testimine")
    print()
    # if c % 2 == 0:
    #     print("с - paaris. Jagame 2.")
    # else:
    #     print("с - paaritu. Korrutame 3, liidame 1 ja jagame 2.")
    while c != 1: # != не равно 
        if c % 2 == 0:
            print('{:>4}'.format(round(c))," - Paaris arv, Jagame 2.")
            c = c / 2
        else:
            print('{:>4}'.format(round(c))," - Paaritu arv, Korrutame 3, liidame 1 ja jagame 2.")
            c = (3*c + 1) / 2
    print('{:>4}'.format(round(c)),"- Hüpotees on õige")
    print()