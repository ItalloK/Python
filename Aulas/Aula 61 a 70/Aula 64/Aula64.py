from tkinter import *

def ImprimirEsporte():
    ve = vEsporte.get()
    if ve == "":
        print("Selecione um esporte")
    elif ve == "Futebol":
        print("Futebol")
    elif ve == "Volei":
        print("Volei")
    elif ve == "Basquete":
        print("Basquete")

app = Tk()
app.title("Ohayo Pokko")
app.geometry("500x300")

listaEsportes = ["Futebol", "Volei", "Basquete"]

vEsporte = StringVar()
vEsporte.set(listaEsportes[0]) # Valor padrao da lista

lb_esportes = Label(app, text="Esportes")
lb_esportes.pack()


op_Esportes = OptionMenu(app, vEsporte, *listaEsportes) # * pra usar todos os itens
op_Esportes.pack()

btn_Esporte = Button(app, text="Esporte Selecinado", command=ImprimirEsporte)
btn_Esporte.pack()

app.mainloop()