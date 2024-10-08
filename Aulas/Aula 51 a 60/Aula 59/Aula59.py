from tkinter import *
import os

c = os.path.dirname(__file__) # pega o diretoria da aplicacao
nomeArquivo = c+"\\nomes.txt"

def GravarDados():
    arquivo=open(nomeArquivo, "a")
    arquivo.write("Nome....: %s" %vnome.get())
    arquivo.write("\nTelefone: %s" %vfone.get())
    arquivo.write("\nEmail...: %s" %vemail.get())
    arquivo.write("\nObs.....: %s" %vobs.get("1.0", END))
    arquivo.write("\n")
    arquivo.close()


app = Tk()

app.title("Ohayo Pokko")
app.geometry("500x300")
app.configure(background="#DDE")

#Anchor --> N = Norte, S = Sul, E = Leste, W = Oeste
#Nordeste = NE, SE = Sudeste, SO = Sudoeste, NO = Noroeste

Label(app, text="Nome", background="#DDE", foreground="#009", anchor=W).place(x=10, y=10, width=100, height=20)
vnome = Entry(app)
vnome.place(x=10, y=30, width=200, height=20)

Label(app, text="Telefone", background="#DDE", foreground="#009", anchor=W).place(x=10, y=60, width=100, height=20)
vfone = Entry(app)
vfone.place(x=10, y=80, width=100, height=20)

Label(app, text="Email", background="#DDE", foreground="#009", anchor=W).place(x=10, y=110, width=100, height=20)
vemail = Entry(app)
vemail.place(x=10, y=130, width=300, height=20)

Label(app, text="OBS", background="#DDE", foreground="#009", anchor=W).place(x=10, y=160, width=100, height=20)
vobs = Text(app)
vobs.place(x=10, y=180, width=300, height=80)

Button(app, text="Gravar", command=GravarDados).place(x=10, y=270, width=100, height=20)

app.mainloop()