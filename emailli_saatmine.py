import tkinter as tk


# Окно
window = tk()
window.geometry("550x200")
window.resizable(False,False) #x=False y=False disables resize of the programm window
window.title("Квадратные уравнения")
window.configure(bg="beige")


lbl_email = tk.label(window, text="E-mail:")
lbl_sub = tk.label(window, text="Subject:")
lbl_attach = tk.label(window, text="Attach File:")

