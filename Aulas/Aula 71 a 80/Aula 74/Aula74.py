from tkinter import *

def ImprimirEsporte():
    print(f'Esporte selecionado: {lb_Esportes.get(ACTIVE)}')

def AdicionarEsporte():
    lb_Esportes.insert(END, novoEsporte.get())

app = Tk()
app.title("Ohayo Pokko")
app.geometry("500x300")

listaEsportes = ["Futebol", "Volei", "Basquete"]

lb_Esportes = Listbox(app)
for esportes in listaEsportes:
    lb_Esportes.insert(END, esportes)
lb_Esportes.pack()

btn_esporte=Button(app, text="Imprimir Esporte", command=ImprimirEsporte)
btn_esporte.pack()

novoEsporte = Entry(app)
novoEsporte.pack()

btn_InserirEsporte=Button(app, text="Adicionar Esporte", command=AdicionarEsporte)
btn_InserirEsporte.pack()
app.mainloop()