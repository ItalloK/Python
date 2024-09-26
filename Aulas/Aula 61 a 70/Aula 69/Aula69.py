from tkinter import *

def FutebolClicado():
    print(f'Futebol: {vFutebol.get()}')

def VoleiClicado():
    print(f'Volei: {vVolei.get()}')

def BasqueteClicado():
    print(f'Basquete: {vBasquete.get()}')

app = Tk()
app.title("Ohayo Pokko")
app.geometry("500x300")

vFutebol = IntVar()
vVolei = IntVar()
vBasquete = IntVar()

fr_quadro1 = Frame(app, borderwidth=1, relief="solid")
fr_quadro1.place(x=10, y=10, width=300, height=100)

cb_futebol = Checkbutton(fr_quadro1, text="Futebol", variable=vFutebol, onvalue=1, offvalue=0, command=FutebolClicado)
cb_futebol.pack(side=LEFT)

cb_volei = Checkbutton(fr_quadro1, text="Volei", variable=vVolei, onvalue=1, offvalue=0, command=VoleiClicado)
cb_volei.pack(side=LEFT)

cb_basquete = Checkbutton(fr_quadro1, text="Basquete", variable=vBasquete, onvalue=1, offvalue=0, command=BasqueteClicado)
cb_basquete.pack(side=LEFT)

app.mainloop()