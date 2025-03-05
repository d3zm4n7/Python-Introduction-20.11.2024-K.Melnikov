
def email_kontroll(ent_emailto):
    """Проверяет заполненность поля E-mail и наличие "@" """
    if not ent_emailto:
        return "Поле E-mail не должно быть пустым!"
    if "@" not in ent_emailto:
        return "Некорректный E-mail: отсутствует '@'"
    return "E-mail корректен"



def entryColor(event): # event = sobytie 
    i=ent_emailto.get()
    if i== "":
        ent_emailto.configure(bg="red")
    else:
        ent_emailto.configure(bg="green")

    i=ent_sub.get()
    if i== "":
        ent_sub.configure(bg="red")
    else:
        ent_sub.configure(bg="green")

    i=txt_message.get()
    if i== "":
        txt_message.configure(bg="red")
    else:
        txt_message.configure(bg="green")