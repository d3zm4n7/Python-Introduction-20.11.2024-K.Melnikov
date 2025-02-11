import datetime

def kontroll_pikkus(ikood: str) -> bool:
    """Kontrollib isikukoodi pikkust.
    
    :param ikood: Isikukood (Эстонский личный код).
    :return: True, kui pikkus on 11, vastasel juhul False.
    """
    return len(ikood) == 11

def kontroll_esimene_arv(ikood: str) -> bool:
    """Kontrollib isikukoodi esimese numbri.
    
    :param ikood: Isikukood.
    :return: True, kui esimene number on 1-6, vastasel juhul False.
    """
    return ikood[0] in {'1', '2', '3', '4', '5', '6'}

def leia_synniaeg(ikood: str) -> tuple[int, int, int]:
    """Leiab sünniaja isikukoodist.
    
    :param ikood: Isikukood.
    :return: Tuple (aasta, kuu, päev).
    """
    esimene_arv = int(ikood[0])
    aasta = int(ikood[1:3]) + (1800 if esimene_arv in {1, 2} else 1900 if esimene_arv in {3, 4} else 2000)
    kuu = int(ikood[3:5])
    paev = int(ikood[5:7])
    return aasta, kuu, paev

def kontroll_synniaeg(aasta: int, kuu: int, paev: int) -> bool:
    """Kontrollib, kas sünniaeg on kehtiv ja mitte tulevikus.
    
    :param aasta: Sünniaasta.
    :param kuu: Sünnikuu.
    :param paev: Sünnipäev.
    :return: True, kui kuupäev on kehtiv ja minevikus, vastasel juhul False.
    """
    try:
        synniaeg = datetime.datetime(aasta, kuu, paev)
        return synniaeg <= datetime.datetime.now()
    except ValueError as e:
        print(f"Viga sünniaja kontrollimisel: {e}")
        return False

def leia_kontroll_nr(ikood: str) -> int:
    """Leiab isikukoodi kontrollnumbri.
    
    :param ikood: Isikukood.
    :return: Kontrollnumber.
    """
    kaalud = [[1,2,3,4,5,6,7,8,9,1], [3,4,5,6,7,8,9,1,2,3]]
    
    for kaal in kaalud:
        summa = sum(int(ikood[i]) * kaal[i] for i in range(10))
        jaak = summa % 11
        if jaak != 10:
            return jaak
    return 0

def leia_sunnikoht(sunnikoht_num: int) -> str:
    """Määrab sünnikoha isikukoodi järgi.
    
    :param sunnikoht_num: Isikukoodi sünnikoha osa.
    :return: Sünnikoht.
    """
    haiglad = [
        [1, 10, "Kuressaare Haigla"],
        [11, 19, "Tartu Ülikooli Naistekliinik, Tartumaa, Tartu"],
        [21, 220, "Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla"],
        [221, 270, "Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)"],
        [271, 370, "Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla"],
        [371, 420, "Narva Haigla"],
        [421, 470, "Pärnu Haigla"],
        [471, 490, "Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigla"],
        [491, 520, "Järvamaa Haigla (Paide)"],
        [521, 570, "Rakvere, Tapa haigla"],
        [571, 600, "Valga Haigla"],
        [601, 650, "Viljandi Haigla"],
        [651, 700, "Lõuna-Eesti Haigla (Võru), Põlva Haigla"]
    ]
    for alg, lopp, koht in haiglad:
        if alg <= sunnikoht_num <= lopp:
            return koht
    return "Tundmatu sünnikoht"

def leia_sugu(ikood: str) -> str:
    """Määrab isiku soo isikukoodi esimese numbri järgi.
    
    :param ikood: Isikukood.
    :return: "mees" või "naine".
    """
    return "mees" if ikood[0] in {'1', '3', '5'} else "naine"

# Testimiseks
if __name__ == "__main__":
    test_ikood = "39003010252"  # Näide isikukoodist
    if kontroll_pikkus(test_ikood) and kontroll_esimene_arv(test_ikood):
        aasta, kuu, paev = leia_synniaeg(test_ikood)
        if kontroll_synniaeg(aasta, kuu, paev):
            kontroll_nr = leia_kontroll_nr(test_ikood)
            sugu = leia_sugu(test_ikood)
            sunnikoht = leia_sunnikoht(int(test_ikood[7:10]))
            print(f"Isikukood: {test_ikood}")
            print(f"Sugu: {sugu}")
            print(f"Sünniaeg: {paev}.{kuu}.{aasta}")
            print(f"Sünnikoht: {sunnikoht}")
            print(f"Kontrollnumber: {kontroll_nr}")
        else:
            print("Vigane sünniaeg!")
    else:
        print("Vigane isikukood!")
