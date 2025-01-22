from re import A


def summa3(arv1:int, arv2:int, arv3:int)->int:
    """Tagastab kolme taisarvu summa


    :param int arv1: Esimene number
    :param int arv2: Teine number
    :param int arv3: Kolmas number
    :rtype: int

    """

    summa=arv1+arv2+arv3
    return summa
    
#1
def arithmetic(a:float, b:float, t: str)->any:
    """Lihtne kalkulaator.
    + - liitmine
    - - lahutamine
    * - korrutamine
    / - jagamine
    :param float a: arv1
    :param float b: arv2
    :param str t: aritmeetiline tehing
    :rtype: var Määramata tüüp(float or str)
    """
    if t in ["+","-","*","/"]:
        if b==0 and t=="/":
            vastus="DIV/0"
        else:
            vastus=eval(str(a)+t+str(b))
    else:
        vastus="Tundmatu tegevus"

        return vastus

#2
def is_year_leap(aasta:int)->bool:
    """Liigaasta leidmine
    Tagastab True, kui liigaasta ja False kui on tavaline aasta.
    :param int aasta: aasta number
    :rtype: bool tagastab loogilises formaadis tulemus

    """
    if aasta%4==0:
        v=True
    else:
        v=False
    return v

#3
def square(a:float)->any:
    """
    Вычисляет периметр, площадь и диагональ квадрата.

    :param float a: Длина стороны квадрата
    :return: Кортеж из периметра, площади и диагонали квадрата
    :rtype: tuple
    """
    P = 4 * a
    S = a ** 2
    d = (2 ** 0.5) * a
    return P, S, d

# #4
def season(m:int)->str:
"""
"""

if 1<=m<=12:
    if m in [1,2,12]:
        v="talv"
    elif m >2 and m <6:
        v="kevad"
    elif 6<=m<=8:
        v="suvi"
    else:
        v="sügis"
else:
    v="error"
return v

#5
def bank(a: float, years:int )->float:
    """

    Банковский вклад

Пользователь делает вклад в размере a евро сроком на years лет под 10% годовых (каждый год размер его вклада увеличивается на 10%. Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже будут проценты).

Написать функцию bank, принимающая аргументы a и years, и возвращающую сумму, которая будет на счету пользователя.

    :param float a:
    :param float years:
    :rtype: float

    """
    for i in range(years):
        a*=1.1
        return a 
#6
def is_prime(n:int, P:int)->bool:







        
