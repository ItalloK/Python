from tkinter import *
from tkinter import messagebox

def MostrarMsg():
    messagebox.showinfo(title="INFO", message="Curso de Python / Tkinter")

vMsg = "Ohayo Pokko"

app = Tk()
app.title("Ohayo Pokko")
app.geometry("500x300")

caixaTexto=StringVar()

fr_quadro1 = Frame(app, borderwidth=1, relief="solid")
#relief  == "flat", "raised", "sunken", "solid"
fr_quadro1.place(x = 10, y = 10, width=300, height=100)

lb_tipo = Label(fr_quadro1, text="Tipo de Caixa (1,2 ou 3)")
lb_tipo.place(x=10, y=10)

tb_num = Entry(fr_quadro1, textvariable=caixaTexto)
caixaTexto.set("1")
tb_num.place(x=10, y=30)

btnMsg = Button(fr_quadro1, text="Mostrar Mensagem", command=MostrarMsg)
btnMsg.place(x=10, y=50)

fr_quadro2 = Frame(app, borderwidth=1, relief="solid", background="#008")
fr_quadro2.place(x = 10, y = 120, width=300, height=100)


lb_teste = Label(fr_quadro2, text="Curso de Python", background="#008", foreground="#fff", font = ("Arial", 25))
lb_teste.pack(side="left", fill=X, expand=True )


app.mainloop()