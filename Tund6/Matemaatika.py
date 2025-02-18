import random

print("Добро пожаловать в программу проверки знаний по математике!")

print("Выберите уровень сложности:")
print("1 - Сложение и вычитание")
print("2 - Сложение, вычитание и умножение")
print("3 - Все действия (+, -, *, /, **)")

while True:
    level = input("Введите уровень сложности (1, 2, 3): ")
    if level in ["1", "2", "3"]:
        level = int(level)
        break
    else:
        print("Пожалуйста, введите 1, 2 или 3.")

num_problems = int(input("Сколько примеров вы хотите решить? "))

correct_answers = 0

for i in range(num_problems):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    if level == 1:
        operation = random.choice(["+", "-"])
    elif level == 2:
        operation = random.choice(["+", "-", "*"])
    else:
        operation = random.choice(["+", "-", "*", "/", "**"])
        if operation == "/":
            b = random.randint(1, 10)
            a = b * random.randint(1, 5)

    if operation == "+":
        correct = a + b
    elif operation == "-":
        correct = a - b
    elif operation == "*":
        correct = a * b
    elif operation == "/":
        correct = a / b
    elif operation == "**":
        correct = a ** b

    print(f"Пример {i+1}: {a} {operation} {b} = ?")
    user_answer = float(input("Ваш ответ: "))

    if round(user_answer, 2) == round(correct, 2):
        print("Правильно!")
        correct_answers += 1
    else:
        print(f"Неправильно. Правильный ответ: {round(correct, 2)}")

percentage = (correct_answers / num_problems) * 100

print(f"\nВы правильно решили {correct_answers} из {num_problems} примеров ({percentage:.2f}%).")

if percentage < 60:
    print("Ваша оценка: Hinne 2")
elif 60 <= percentage < 75:
    print("Ваша оценка: Hinne 3")
elif 75 <= percentage < 90:
    print("Ваша оценка: Hinne 4")
else:
    print("Ваша оценка: Hinne 5")

print("Спасибо за участие в тесте!")
