from tkinter import *

def ValorEscala():
    print(f'Valor da Escala: {sc_Escala.get()}')

app = Tk()
app.title("Ohayo Pokko")
app.geometry("500x300")

lb_Valor = Label(app, text="Valor:")
lb_Valor.pack()

sc_Escala = Scale(app, from_=0, to=100, orient=HORIZONTAL)
sc_Escala.set(50) # Define onde começa
sc_Escala.pack()

btn_Valor = Button(app, text="Ver valor", command=ValorEscala)
btn_Valor.pack()

app.mainloop()