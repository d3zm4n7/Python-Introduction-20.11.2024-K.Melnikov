from tkinter import *
from tkinter import messagebox
from Ruutvorrandi_lahendamine_Matplotlib_def import *
from PIL import Image, ImageTk

def sisend_kontroll():
    """Проверяет заполненность полей ввода"""
    for field in [sisesta_a, sisesta_b, sisesta_c]:
        field.configure(bg="mistyrose" if field.get() == "" else "honeydew")

def lahenda():
    """Решает квадратное уравнение"""
    try:
        sisend_kontroll()
        a, b, c = float(sisesta_a.get()), float(sisesta_b.get()), float(sisesta_c.get())
        tulemus.configure(text=funktsiooni_lahendamine(a, b, c)) 
    except:
        tulemus.configure(text="Ошибка ввода!")

def graafik():
    """Строит график функции"""
    try:
        sisend_kontroll()
        a, b, c = float(sisesta_a.get()), float(sisesta_b.get()), float(sisesta_c.get())
        funktsiooni_graafik(a, b, c)
    except:
        tulemus.configure(text="Ошибка ввода!")

def entryColor(event): # event = sobytie 
    i=sisesta_a.get()
    if i== "":
        sisesta_a.configure(bg="red")
    else:
        sisesta_a.configure(bg="green")

    i=sisesta_b.get()
    if i== "":
        sisesta_b.configure(bg="red")
    else:
        sisesta_b.configure(bg="green")

    i=sisesta_c.get()
    if i== "":
        sisesta_c.configure(bg="red")
    else:
        sisesta_c.configure(bg="green")

# Окно
aken = Tk()
aken.geometry("550x200")
aken.resizable(False,False) #x=False y=False disables resize of the programm window
aken.title("Квадратные уравнения")
aken.configure(bg="beige")

# Add background picture
original_bg = Image.open(r"bg.png")
resized_bg = original_bg.resize((550, 200))
bgimage=ImageTk.PhotoImage(resized_bg)

labelBG=Label(aken, image=bgimage)
labelBG.place(x=0, y=0)

# Заголовок
pealkiri = Label(aken, text="Решение квадратного уравнения", font=("Times New Roman", 20), fg="darkslategray", bg="lightgoldenrodyellow")

# Контейнер для ввода
teine_rida = Frame(aken, bg="beige")

# Поля ввода
sisesta_a = Entry(teine_rida, font=("Times New Roman", 16), width=3)
sisesta_a.bind("<KeyRelease>" ,entryColor)

sisesta_b = Entry(teine_rida, font=("Times New Roman", 16), width=3)
sisesta_b.bind("<KeyRelease>" ,entryColor)

sisesta_c = Entry(teine_rida, font=("Times New Roman", 16), width=3)
sisesta_c.bind("<KeyRelease>" ,entryColor)

# Метки
tekst1 = Label(teine_rida, text="x² +", font=("Times New Roman", 16), bg="beige")
tekst2 = Label(teine_rida, text="x +", font=("Times New Roman", 16), bg="beige")
tekst3 = Label(teine_rida, text="= 0", font=("Times New Roman", 16), bg="beige")

# Кнопки
lahenda_nupp = Button(teine_rida, text="Решить", command=lahenda, font=("Times New Roman", 14), bg="lightblue", fg="black", width=7)
graafik_nupp = Button(teine_rida, text="График", command=graafik, font=("Times New Roman", 14), bg="lightblue", fg="black", width=7)

# Поле вывода
tulemus = Label(aken, font=("Times New Roman", 14), text="Решение", bg="lightgoldenrodyellow", width=50, height=3)

# Размещение элементов
pealkiri.pack()
teine_rida.pack(pady=10)
sisesta_a.grid(row=0, column=0)
tekst1.grid(row=0, column=1)
sisesta_b.grid(row=0, column=2)
tekst2.grid(row=0, column=3)
sisesta_c.grid(row=0, column=4)
tekst3.grid(row=0, column=5)
lahenda_nupp.grid(row=0, column=6)
graafik_nupp.grid(row=0, column=7)
tulemus.pack()

aken.mainloop()