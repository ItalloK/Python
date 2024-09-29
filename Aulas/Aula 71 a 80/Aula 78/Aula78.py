from tkinter import *
from tkinter import ttk


app = Tk()
app.title("Ohayo Pokko")
app.geometry("500x300")

lb_GitHub = Label(app, text="github.com/ItalloK")

lb_Nome = Label(app, text="Digite seu nome:")

lb_Idade = Label(app, text="Digite sua idade:")

et_Nome = Entry(app)
et_Idade = Entry(app)

btn = Button(app, text="Botao")

lb_GitHub.grid(column=0, row=0, columnspan=2, pady=15)
lb_Nome.grid(column=0, row=1, sticky='W') #W, E, N...
et_Nome.grid(column=0, row=2, padx=5)
lb_Idade.grid(column=1, row=1, sticky='W')
et_Idade.grid(column=1, row=2, padx=5)

app.mainloop()