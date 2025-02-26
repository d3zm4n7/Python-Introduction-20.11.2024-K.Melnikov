from tkinter import *


# Окно
window = Tk()
window.geometry("550x200")
window.resizable(False,False) #x=False y=False disables resize of the programm window
window.title("Compose new E-mail")
window.configure(bg="beige")



lbl_emailto = Label(window, text="E-mail:", font=("Times New Roman", 20), fg="darkgreen", bg="lightgoldenrodyellow")
lbl_sub = Label(window, text="Subject:", font=("Times New Roman", 20), fg="darkgreen", bg="lightgoldenrodyellow")
lbl_attach = Label(window, text="Attach File:", font=("Times New Roman", 20), fg="darkslategray", bg="lightgoldenrodyellow")

