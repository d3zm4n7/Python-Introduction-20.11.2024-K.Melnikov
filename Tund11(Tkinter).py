from tkinter import *
from Tund10graafilineliides import *
global varv

def v_valik():
    varv="white"
    if tekst.get()!="":
        tekst.configure(bg="yellow")
        varv=tekst.get()

    else:
        tekst.configure(bg="red")
    return varv


def figuur(varv:str):
    valik=var.get()
   # varv=v_valik()
    if valik==1:
        prillid(varv)
    elif valik==2:
        Vaal(varv)
    else:
        Vihmavari(varv)
        print("Joonistan hiljem")

aken = Tk()
aken.geometry("400x800")
aken.title("Graafikud")
pealkiri = Label(aken, text="Erinevad pildid Matpoltlib abil", font="Calibri 24", fg="green", bg="lightgreen", pady=20, width=50)
var=IntVar()
r1=Radiobutton(aken,text="Vaal", font="Calibri 18", variable=var,value=1,command=figuur)
r2=Radiobutton(aken,text="prillid", font="Calibri 18", variable=var,value=2,command=figuur)
r3=Radiobutton(aken,text="Vihmavari", font="Calibri 18", variable=var,value=2,command=figuur)
tekst=Entry(aken, font="Calibri 24", fg="yellow", bg="green", width=45)
nupp=Button(aken, text="Varvi valik",  font="Calibri 24", fg="black", bg="green", command=v_valik)


pealkiri.pack() #place(x=...,y=...) / grid(column=...,row=...)
tekst.pack(side=LEFT)
nupp.pack()
r1.pack()
r2.pack()
r3.pack()
aken.mainloop()  # Add the parentheses here to call mainloop as a function

