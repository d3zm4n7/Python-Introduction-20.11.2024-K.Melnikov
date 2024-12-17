from math import *

# Ülesanne 1 Пользователь вводит число, программа определяет знак числа(положительное оно или отрицательное), если число положительное, то проверяет его на  четность и нечетность.

number = float(input("Введите число: "))

if number > 0:
    print("Число положительное.")
    if number % 2 == 0:
        print("Число четное.")
    else:
        print("Число нечетное.")
elif number < 0:
    print("Число отрицательное.")
else:
    print("Число равно нулю.")

# Ülesanne 2 Спросить у пользователя 3 числа, если они окажуться положительными, то проверить могут ли они быть углами одного треугольника(сумма углов 180) и уточнить какого именно треугольника(равносторонний, равнобедренный или разносторонний).

angle1 = float(input("Введите первый угол треугольника: "))
angle2 = float(input("Введите второй угол треугольника: "))
angle3 = float(input("Введите третий угол треугольника: "))

if angle1 > 0 and angle2 > 0 and angle3 > 0:
    if angle1 + angle2 + angle3 == 180:
        print("Это треугольник.")
        if angle1 == angle2 == angle3:
            print("Треугольник равносторонний.")
        elif angle1 == angle2 or angle1 == angle3 or angle2 == angle3:
            print("Треугольник равнобедренный.")
        else:
            print("Треугольник разносторонний.")
    else:
        print("Сумма углов не равна 180 градусам. Это не треугольник.")
else:
    print("Все углы должны быть положительными числами.")

# Ülesanne 3 Выяснить у пользователя желание расшифровать порядковый номер дня недели в название. Если пользователь отвечает "да"(учесть, что можно отвечать маленькими и большими буквами), спросить у него число, если это число от 1 до 7, то вывести на экран соответствующее название дня недели.

response = input("Хотите расшифровать порядковый номер дня недели в название? (да/нет): ").lower()

if response == "да":
    try:
        day_number = int(input("Введите число от 1 до 7: "))
        days_of_week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
        if 1 <= day_number <= 7:
            print(f"День недели: {days_of_week[day_number - 1]}")
        else:
            print("Ошибка: число должно быть от 1 до 7.")
    except ValueError:
        print("Ошибка: пожалуйста, введите целое число.")
else:
    print("Операция отменена.")

# Ülesanne 4 Определить по дню и месяцу рождения пользователя кто он по гороскопу. Проверять введенные данные(тип данных и промежуток значений), иначе выводить сообветствующее сообщение!

try:
    day = int(input("Введите день вашего рождения (1-31): "))
    month = int(input("Введите месяц вашего рождения (1-12): "))

    if 1 <= day <= 31 and 1 <= month <= 12:
        if (month == 1 and day >= 20) or (month == 2 and day <= 18):
            zodiac = "Водолей"
        elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
            zodiac = "Рыбы"
        elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
            zodiac = "Овен"
        elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
            zodiac = "Телец"
        elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
            zodiac = "Близнецы"
        elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
            zodiac = "Рак"
        elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
            zodiac = "Лев"
        elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
            zodiac = "Дева"
        elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
            zodiac = "Весы"
        elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
            zodiac = "Скорпион"
        elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
            zodiac = "Стрелец"
        elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
            zodiac = "Козерог"
        else:
            zodiac = None
        
        if zodiac:
            print(f"Ваш знак зодиака: {zodiac}")
        else:
            print("Ошибка: некорректная дата.")
    else:
        print("Ошибка: день должен быть от 1 до 31, а месяц от 1 до 12.")
except ValueError:
    print("Ошибка: введите числовое значение для дня и месяца.")

# Ülesanne 5 Проверить введенное пользователем число, отпределить его тип и если число целое, то найти от него 50%, если число дробное, то найти от него 70%, если это текст, то вывести его на экран. Для решения можно использовать: is_integer(), isalpha(), isdigit(), int(), float(), //, %.

user_input = input("Введите число или текст: ")

try:
    number = float(user_input)
    if number.is_integer():
        print(f"Число целое. 50% от {int(number)}: {int(number) // 2}")
    else:
        print(f"Число дробное. 70% от {number}: {number * 0.7:.2f}")
except ValueError:
    if user_input.isalpha():
        print(f"Это текст: {user_input}")
    else:
        print("Ошибка: введённые данные не соответствуют числу или тексту.")

# Ülesanne 6 Функция для решения квадратного уравнения

answer = input("Хотите решить квадратное уравнение? (да/нет): ").lower()

if answer == "да":
    try:
        a = float(input("Введите коэффициент a: "))
        b = float(input("Введите коэффициент b: "))
        c = float(input("Введите коэффициент c: "))
        
        if a == 0:
            print("Коэффициент 'a' не может быть равен 0 при решении квадратного уравнения.")
        else:
            D = b ** 2 - 4 * a * c
            print(f"Дискриминант D = {D:.2f}")
            if D > 0:
                x1 = (-b + sqrt(D)) / (2 * a)
                x2 = (-b - sqrt(D)) / (2 * a)
                print(f"Уравнение имеет два решения: x1 = {x1:.2f}, x2 = {x2:.2f}")
            elif D == 0:
                x = -b / (2 * a)
                print(f"Уравнение имеет одно решение: x = {x:.2f}")
            else:
                print("Уравнение не имеет действительных решений, так как D < 0.")
    except ValueError:
        print("Ошибка ввода! Введите числовые значения для коэффициентов a, b и c.")
else:
    print("Спасибо! До свидания.")
