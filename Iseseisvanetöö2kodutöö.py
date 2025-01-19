while True:
        print("\nМеню строковых функций Python:")
        print("1. Поиск подстроки (find)")
        print("2. Замена подстроки (replace)")
        print("3. Разбиение строки (split)")
        print("4. Проверка на цифры (isdigit)")
        print("5. Проверка на буквы (isalpha)")
        print("6. Приведение к верхнему регистру (upper)")
        print("7. Приведение к нижнему регистру (lower)")
        print("8. Удаление пробелов (strip)")
        print("9. Переворот регистра (swapcase)")
        print("10. Создание строки из списка (join)")
        print("0. Выход")
        
        choice = input("Выберите номер функции (0-10): ")
        
        if choice == "1":
            text = "Tere, Marina!"
            result = text.find("Marina")
            print(f"Пример: В строке '{text}' ищем 'Marina'. Результат: {result}")
            print("Смысл: Возвращает индекс первого вхождения подстроки или -1.")
        
        elif choice == "2":
            text = "Я учу Programmeerimise alused :)."
            result = text.replace("учу", "люблю")
            print(f"Пример: '{text}' -> '{result}'")
            print("Смысл: Заменяет одну подстроку другой.")
        
        elif choice == "3":
            text = "Kirill Melnikov,Gleb Dranitsõn,Deniel Kruusman"
            result = text.split(",")
            print(f"Пример: '{text}' -> {result}")
            print("Смысл: Разделяет строку на список по указанному разделителю.")
        
        elif choice == "4":
            text = "12345"
            result = text.isdigit()
            print(f"Пример: '{text}'. Результат: {result}")
            print("Смысл: Проверяет, состоит ли строка только из цифр.")
        
        elif choice == "5":
            text = "Tere"
            result = text.isalpha()
            print(f"Пример: '{text}'. Результат: {result}")
            print("Смысл: Проверяет, состоит ли строка только из букв.")
        
        elif choice == "6":
            text = "tere targv24"
            result = text.upper()
            print(f"Пример: '{text}' -> '{result}'")
            print("Смысл: Преобразует строку в верхний регистр.")
        
        elif choice == "7":
            text = "TERE TARGV24"
            result = text.lower()
            print(f"Пример: '{text}' -> '{result}'")
            print("Смысл: Преобразует строку в нижний регистр.")
        
        elif choice == "8":
            text = "  tervist  "
            result = text.strip()
            print(f"Пример: '{text}' -> '{result}'")
            print("Смысл: Удаляет пробельные символы в начале и в конце строки.")
        
        elif choice == "9":
            text = "Tere TARgv24"
            result = text.swapcase()
            print(f"Пример: '{text}' -> '{result}'")
            print("Смысл: Переводит символы нижнего регистра в верхний и наоборот.")
        
        elif choice == "10":
            words = ["Kirill", "Gleb", "Deniel"]
            result = ", ".join(words)
            print(f"Пример: {words} -> '{result}'")
            print("Смысл: Объединяет список строк в одну строку с разделителем.")
        
        elif choice == "0":
            print("Выход из программы.")
            break
        
        else:
            print("Некорректный выбор, попробуйте снова.")