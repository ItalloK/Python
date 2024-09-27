from tkinter import *

def ImpSenha():
    print(f'Senha digitada: {senha.get()}')

app = Tk()
app.title("Ohayo Pokko")
app.geometry("500x300")

senha = StringVar()

tb_senha = Entry(app, textvariable=senha, show="*")
tb_senha.pack()

btn_mostrarsenha = Button(app, text="Mostrar Senha", command=ImpSenha)
btn_mostrarsenha.pack()

app.mainloop()