import tkinter as tk
import random
from tkinter import Entry, Button, Frame, messagebox

# Глобальные переменные
current_layout = "qwerty"
word_lists = {
    "qwerty": ["APPLE", "GRAPE", "MOUSE", "TABLE", "CHAIR", "PLANT", "WATER", "BREAD", "LIGHT", "STONE"],
    "йцукен": ["ГРУША", "МЫШКА", "ТРАВА", "БАЛКА", "ПИТОН", "ДОСКА", "ПАРТА", "ЛАМПА", "ЗАМОК", "КНИГА"]
}
word = ""
attempts = 0
max_attempts = 6
entries = []
keyboard_frame = None

# Функция выбора случайного слова 
def choose_word():
    global word
    word = random.choice(word_lists[current_layout])

# Функция обработки нажатия клавиш
def on_key_press(letter):
    for entry in entries[attempts]:
        if entry.get() == "":
            entry.insert(0, letter)
            return

# Функция очистки ввода последней буквы
def delete_last_letter():
    for entry in reversed(entries[attempts]):
        if entry.get() != "":
            entry.delete(0, tk.END)
            return

# Функция проверки введённого слова
def check_guess():
    global attempts
    if attempts >= max_attempts:
        return

    guess = "".join(entry.get().upper() for entry in entries[attempts])
    if len(guess) != 5:
        messagebox.showwarning("Ошибка", "Введите слово из 5 букв!")
        return

    for i, letter in enumerate(guess):
        if letter == word[i]:
            entries[attempts][i].config(bg="green", fg="white")
        elif letter in word:
            entries[attempts][i].config(bg="yellow", fg="black")
        else:
            entries[attempts][i].config(bg="gray", fg="white")
    
    if guess == word:
        messagebox.showinfo("Поздравляем!", "Вы угадали слово!")
        window.quit()
    
    attempts += 1
    if attempts == max_attempts:
        messagebox.showinfo("Игра окончена", f"Загаданное слово: {word}")
        window.quit()

# Функция смены раскладки
def switch_layout():
    global current_layout, word, attempts
    current_layout = "йцукен" if current_layout == "qwerty" else "qwerty"
    choose_word()
    reset_game()
    draw_keyboard()

# Функция очистки игрового поля
def reset_game():
    global attempts
    attempts = 0
    for row in entries:
        for entry in row:
            entry.delete(0, tk.END)
            entry.config(bg="white", fg="black")

# Функция отрисовки клавиатуры
def draw_keyboard():
    for widget in keyboard_frame.winfo_children():
        widget.destroy()
    
    layouts = {
        "qwerty": ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"],
        "йцукен": ["ЙЦУКЕНГШЩЗ", "ФЫВАПРОЛДЖ", "ЯЧСМИТЬБЮ"]
    }
    
    for row in layouts[current_layout]:
        key_row = Frame(keyboard_frame, bg="beige")
        key_row.pack()
        for letter in row:
            key_button = Button(key_row, text=letter, width=3, font=("Arial", 14),
                                command=lambda l=letter: on_key_press(l))
            key_button.pack(side=tk.LEFT, padx=2, pady=2)
    
    switch_button = Button(window, text="Сменить раскладку", command=switch_layout)
    switch_button.pack(pady=5)
    delete_button = Button(window, text="⌫", command=delete_last_letter)
    delete_button.pack(pady=5)

# Создание окна
window = tk.Tk()
window.geometry("500x700")
window.resizable(False, False)
window.title("WORLDE")
window.configure(bg="beige")

# Фрейм для игрового поля
frame = Frame(window, bg="beige")
frame.pack(pady=20)

# Создание сетки 5x6
entries = []
for i in range(max_attempts):
    row = []
    for j in range(5):
        entry = Entry(frame, width=3, font=("Arial", 18), justify="center")
        entry.grid(row=i, column=j, padx=5, pady=5)
        row.append(entry)
    entries.append(row)

# Фрейм для кнопок-клавиатуры
keyboard_frame = Frame(window, bg="beige")
keyboard_frame.pack(pady=10)

# Кнопка проверки слова
submit_button = Button(window, text="Проверить", command=check_guess)
submit_button.pack(pady=10)

# Выбор начального слова и отрисовка клавиатуры
choose_word()
draw_keyboard()

window.mainloop()
 