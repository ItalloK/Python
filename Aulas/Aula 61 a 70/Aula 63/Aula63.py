from tkinter import *

def ImprimirEsporte():
    ve = vEsporte.get()
    if ve == "":
        print("Selecione um esporte")
    elif ve == "f":
        print("Futebol")
    elif ve == "v":
        print("Volei")
    elif ve == "b":
        print("Basquete")

app = Tk()
app.title("Ohayo Pokko")
app.geometry("500x300")

vEsporte = StringVar()
vCores = StringVar()

lb_esportes = Label(app, text="Esportes")
lb_esportes.pack()

rb_futebol = Radiobutton(app, text="Futebol", value="f", variable=vEsporte)
rb_futebol.pack()

rb_volei = Radiobutton(app, text="Volei", value="v", variable=vEsporte)
rb_volei.pack()

rb_basquete = Radiobutton(app, text="Basquete", value="b", variable=vEsporte)
rb_basquete.pack()

rb_vermelho = Radiobutton(app, text="Vermelho", value="#f00", variable=vCores)
rb_vermelho.pack()

rb_verde = Radiobutton(app, text="Verde", value="#0f0", variable=vCores)
rb_verde.pack()

btn_Esporte = Button(app, text="Esporte Selecinado", command=ImprimirEsporte)
btn_Esporte.pack()

app.mainloop()