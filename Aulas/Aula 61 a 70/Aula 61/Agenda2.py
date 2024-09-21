from tkinter import *
import os
import Banco

def SemComando():
    print("")

def NovoContato():
    exec(open(Banco.pastaApp+"\\NovoContato.py").read(), {'x':10}) # Passando Parametro

app = Tk()

app.title("Ohayo Pokko")
app.geometry("500x300")
app.configure(background="#DDE")

barraDeMenus = Menu(app)

menuContatos = Menu(barraDeMenus, tearoff=0)
menuContatos.add_command(label="Novo", command=NovoContato)
menuContatos.add_command(label="Pesquisar", command=SemComando)
menuContatos.add_command(label="Deletar", command=SemComando)
menuContatos.add_separator()
menuContatos.add_command(label="Fechar", command=app.quit)
barraDeMenus.add_cascade(label="Contatos", menu=menuContatos)

menuManutencao = Menu(barraDeMenus, tearoff=0)
menuManutencao.add_command(label="Banco de Dados", command=SemComando)
barraDeMenus.add_cascade(label="Manutencao", menu=menuManutencao)

menuSobre = Menu(barraDeMenus, tearoff=0)
menuSobre.add_command(label="Github", command=SemComando)
barraDeMenus.add_cascade(label="Sobre", menu=menuSobre)

app.config(menu=barraDeMenus)
app.mainloop()