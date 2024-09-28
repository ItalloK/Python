from tkinter import *

def ImprimirValor():
    print(f'Valor: {sb_Valores.get()}')

app = Tk()
app.title("Ohayo Pokko")
app.geometry("500x300")

#sb_Valores = Spinbox(app, from_=0, to=100)
sb_Valores = Spinbox(app, values=(1,2,3,4,5)) # Define valores especificos
sb_Valores.pack()

btn_Valor = Button(app, text="Imprimir Valor", command=ImprimirValor)
btn_Valor.pack()

app.mainloop()