ikoodid = []
arvud = []

while True:
    isikukood_input = input("Введите личный код (или 'stop' для выхода): ")
    if isikukood_input.lower() == "stop":
        break

    if len(isikukood_input) != 11 or not isikukood_input.isdigit():
        print("Неверное количество символов. Попробуйте снова.")
        arvud.append(isikukood_input)
        continue

    isikukood = [int(digit) for digit in isikukood_input]

    sugu = isikukood[0] #проверка первой цифры личного кода
    if sugu not in [1, 2, 3, 4, 5, 6]:
        print("Неверный первый символ. Попробуйте снова.")
        arvud.append(isikukood_input)
        continue

    aasta_prefix = {1: 1800, 2: 1800, 3: 1900, 4: 1900, 5: 2000, 6: 2000} #условия, чтобы программа понимала в каком столетии родился человек и какого он пола
    aasta = aasta_prefix[sugu] + int(isikukood_input[1:3])
    kuu = int(isikukood_input[3:5])
    paev = int(isikukood_input[5:7])

    if not (1 <= kuu <= 12 and 1 <= paev <= 31):
        print("Неверная дата рождения. Попробуйте снова.")
        arvud.append(isikukood_input)
        continue

    synnitus_number = int(isikukood_input[7:10]) #условия, чтобы программа понимала в каком региони Эстонии человек родился
    if 1 <= synnitus_number <= 10:
        asukoht = "Kuressaare Haigla"
    elif 11 <= synnitus_number <= 19:
        asukoht = "Tartu Ülikooli Naistekliinik, Tartumaa, Tartu"
    elif 21 <= synnitus_number <= 220:
        asukoht = "Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla"
    elif 221 <= synnitus_number <= 270:
        asukoht = "Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)"
    elif 271 <= synnitus_number <= 370:
        asukoht = "Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla"
    elif 371 <= synnitus_number <= 420:
        asukoht = "Narva Haigla"
    elif 421 <= synnitus_number <= 470:
        asukoht = "Pärnu Haigla"
    elif 471 <= synnitus_number <= 490:
        asukoht = "Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigla"
    elif 491 <= synnitus_number <= 520:
        asukoht = "Järvamaa Haigla (Paide)"
    elif 521 <= synnitus_number <= 570:
        asukoht = "Rakvere, Tapa haigla"
    elif 571 <= synnitus_number <= 600:
        asukoht = "Valga Haigla"
    elif 601 <= synnitus_number <= 650:
        asukoht = "Viljandi Haigla"
    elif 651 <= synnitus_number <= 700:
        asukoht = "Lõuna-Eesti Haigla (Võru), Põlva Haigla"
    else:
        asukoht = "Tundmatu koht"

    astmekaal1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    astmekaal2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]

    sum1 = sum(isikukood[i] * astmekaal1[i] for i in range(10))
    jaak1 = sum1 % 11

    if jaak1 == 10:
        sum2 = sum(isikukood[i] * astmekaal2[i] for i in range(10))
        jaak2 = sum2 % 11
        kontrollnumber = jaak2 if jaak2 != 10 else 0
    else:
        kontrollnumber = jaak1

    if kontrollnumber != isikukood[-1]:
        print("Неверный контрольный номер. Попробуйте снова.")
        arvud.append(isikukood_input)
        continue

    sugu_tekst = "мужчина" if sugu % 2 != 0 else "женщина"
    print(f"Это {sugu_tekst}, его/ее день рождения {paev:02}.{kuu:02}.{aasta} и место рождения {asukoht}.")
    ikoodid.append(isikukood_input)

# Разделение на мужские и женские коды
mehed = [code for code in ikoodid if int(code[0]) % 2 != 0]
naised = [code for code in ikoodid if int(code[0]) % 2 == 0]

arvud.sort()
ikoodid = mehed + naised

print("\nСписок правильных личных кодов:")
print("\n".join(ikoodid))
print("\nСписок неправильных кодов:")
print("\n".join(arvud))
