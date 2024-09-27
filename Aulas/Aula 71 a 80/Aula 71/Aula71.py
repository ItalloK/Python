from tkinter import *
from tkinter import ttk

def EsporteSelecionado():
    esporte = cb_Esportes.get()
    print(f'Esporte selecionado: {esporte}')

app = Tk()
app.title("Ohayo Pokko")
app.geometry("500x300")

listaEsportes = ["Futebol", "Volei", "Basquete"]

lbl_Esportes = Label(app, text="Esportes")
lbl_Esportes.pack()

cb_Esportes = ttk.Combobox(app, values=listaEsportes)
cb_Esportes.set("Futebol")
cb_Esportes.pack()

btn_Esporte = Button(app, text="Esporte Selecionado", command=EsporteSelecionado)
btn_Esporte.pack()

app.mainloop()