import datetime

def validate_isikukood(isikukood_input):
    """Проверяет корректность личного кода и возвращает его числовое представление или ошибку."""
    if len(isikukood_input) != 11 or not isikukood_input.isdigit():
        return False, "Неверное количество символов или неверный формат. Попробуйте снова."
    
    isikukood = [int(digit) for digit in isikukood_input]
    sugu = isikukood[0]
    if sugu not in [1, 2, 3, 4, 5, 6]:
        return False, "Неверный первый символ. Попробуйте снова."
    
    return True, isikukood

def get_birth_info(isikukood):
    """Возвращает информацию о дате рождения и поле человека."""
    aasta_prefix = {1: 1800, 2: 1800, 3: 1900, 4: 1900, 5: 2000, 6: 2000}
    aasta = aasta_prefix[isikukood[0]] + isikukood[1] * 10 + isikukood[2]
    kuu = isikukood[3] * 10 + isikukood[4]
    paev = isikukood[5] * 10 + isikukood[6]
    
    try:
        datetime.datetime(aasta, kuu, paev)
    except ValueError:
        return False, "Неверная дата рождения. Попробуйте снова."
    
    sugu_tekst = "мужчина" if isikukood[0] % 2 != 0 else "женщина"
    return True, (sugu_tekst, paev, kuu, aasta)

def get_birth_location(synnitus_number):
    """Возвращает место рождения по номеру роддома."""
    location_map = {
        (1, 10): "Kuressaare Haigla",
        (11, 19): "Tartu Ülikooli Naistekliinik, Tartumaa, Tartu",
        (21, 220): "Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla",
        (221, 270): "Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)",
        (271, 370): "Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla",
        (371, 420): "Narva Haigla",
        (421, 470): "Pärnu Haigla",
        (471, 490): "Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigla",
        (491, 520): "Järvamaa Haigla (Paide)",
        (521, 570): "Rakvere, Tapa haigla",
        (571, 600): "Valga Haigla",
        (601, 650): "Viljandi Haigla",
        (651, 700): "Lõuna-Eesti Haigla (Võru), Põlva Haigla"
    }
    
    for (start, end), location in location_map.items():
        if start <= synnitus_number <= end:
            return location
    return "Tundmatu koht"

def leia_kontroll_nr(ikood):
    """Вычисляет контрольный номер личного кода."""
    astme_kaal_1 = [1,2,3,4,5,6,7,8,9,1]
    astme_kaal_2 = [3,4,5,6,7,8,9,1,2,3]
    
    astme_summa_1 = sum(ikood[i] * astme_kaal_1[i] for i in range(10))
    jaak = astme_summa_1 % 11
    
    if jaak == 10:
        astme_summa_2 = sum(ikood[i] * astme_kaal_2[i] for i in range(10))
        jaak = astme_summa_2 % 11
        if jaak == 10:
            jaak = 0
    
    return jaak

def main():
    """Основная функция программы."""
    ikoodid = []
    arvud = []
    
    while True:
        isikukood_input = input("Введите личный код (или 'stop' для выхода): ")
        if isikukood_input.lower() == "stop":
            break

        valid, result = validate_isikukood(isikukood_input)
        if not valid:
            print("Ошибка: ", result)
            arvud.append(isikukood_input)
            continue

        isikukood = result
        kontroll_nr = leia_kontroll_nr(isikukood)
        if kontroll_nr != isikukood[-1]:
            print("Ошибка: Неверный контрольный номер.")
            arvud.append(isikukood_input)
            continue

        valid, birth_info = get_birth_info(isikukood)
        if not valid:
            print("Ошибка: ", birth_info)
            arvud.append(isikukood_input)
            continue

        sugu_tekst, paev, kuu, aasta = birth_info
        synnitus_number = int(isikukood_input[7:10])
        asukoht = get_birth_location(synnitus_number)

        print(f"Это {sugu_tekst}: \nEго/её день рождения {paev:02}.{kuu:02}.{aasta} и \nМесто рождения {asukoht}.")
        ikoodid.append(isikukood_input)
    
    print("Список правильных личных кодов:")
    print("\n".join(ikoodid))
    print("\nСписок неправильных кодов:")
    print("\n".join(arvud))

if __name__ == "__main__":
    main()
