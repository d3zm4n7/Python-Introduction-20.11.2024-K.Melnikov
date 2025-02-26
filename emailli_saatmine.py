import tkinter as tk
from tkinter import Entry, Label, Text, Button, Frame

# Окно
window = tk.Tk()
window.geometry("550x300")
window.resizable(False, False)  # Отключаем изменение размера
window.title("Compose new E-mail")
window.configure(bg="beige")

# Цвета
bg_label = "lightgoldenrodyellow"
fg_text = "darkgreen"
btn_bg = "darkgreen"
btn_fg = "white"

# Метки (Labels)
lbl_emailto = Label(window, text="E-mail:", font=("Times New Roman", 14), fg=fg_text, bg=bg_label)
lbl_emailto.grid(row=0, column=0, sticky="w", padx=5, pady=5)

lbl_sub = Label(window, text="Subject:", font=("Times New Roman", 14), fg=fg_text, bg=bg_label)
lbl_sub.grid(row=1, column=0, sticky="w", padx=5, pady=5)

lbl_attach = Label(window, text="Attach File:", font=("Times New Roman", 14), fg="darkslategray", bg=bg_label)
lbl_attach.grid(row=2, column=0, sticky="w", padx=5, pady=5)

lbl_body = Label(window, text="Message:", font=("Times New Roman", 14), fg=fg_text, bg=bg_label)
lbl_body.grid(row=3, column=0, sticky="nw", padx=5, pady=5)

# Поля ввода (Entries)
ent_emailto = Entry(window, width=30)
ent_emailto.grid(row=0, column=1, columnspan=4, padx=5, pady=5, sticky="ew")

ent_sub = Entry(window, width=30)
ent_sub.grid(row=1, column=1, columnspan=3, padx=5, pady=5, sticky="ew")

ent_attach = Label(window, text="...", font=("Times New Roman", 14), fg=fg_text, bg=bg_label)
ent_attach.grid(row=2, column=1,columnspan=3, padx=5, pady=5, sticky="ew")



# Поле для ввода текста письма (Text)
txt_message = Text(window, width=30, height=5)
txt_message.grid(row=3, column=1, columnspan=3, padx=5, pady=5, sticky="ew")

# Кнопка отправки
btn_attach = Button(window, text="LISA PILT", font=("Times New Roman", 10, "bold"), bg=btn_bg, fg=btn_fg)
btn_attach.grid(row=4, column=2, padx=5, pady=5, sticky="ew")

btn_send = Button(window, text="SAADA", font=("Times New Roman", 10, "bold"), bg=btn_bg, fg=btn_fg)
btn_send.grid(row=4, column=3, padx=5, pady=10, sticky="ew")

# Настройка сетки
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)

# Запуск программы
window.mainloop()
