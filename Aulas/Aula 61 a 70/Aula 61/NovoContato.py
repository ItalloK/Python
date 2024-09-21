from tkinter import *
import os
import Banco

def GravarDados():
    if tb_Nome.get() != "":
        vnome = tb_Nome.get()
        vfone = tb_Fone.get()
        vemail = tb_Email.get()
        vobs = tb_Obs.get("1.0", END)
        query = "INSERT INTO tb_contatos (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO, T_OBS) VALUES ('"+vnome+"','"+vfone+"','"+vemail+"','"+vobs+"')"
        Banco.Dml(query)
        tb_Nome.delete(0, END)
        tb_Fone.delete(0, END)
        tb_Email.delete(0, END)
        tb_Obs.delete("1.0", END)
        print("Dados Gravados")
    else:
        print("ERRO")


app = Tk()

app.title("Ohayo Pokko")
app.geometry("500x300")
app.configure(background="#DDE")

#Anchor --> N = Norte, S = Sul, E = Leste, W = Oeste
#Nordeste = NE, SE = Sudeste, SO = Sudoeste, NO = Noroeste

Label(app, text="Nome", background="#DDE", foreground="#009", anchor=W).place(x=10, y=10, width=100, height=20)
tb_Nome = Entry(app)
tb_Nome.place(x=10, y=30, width=200, height=20)

Label(app, text="Telefone", background="#DDE", foreground="#009", anchor=W).place(x=10, y=60, width=100, height=20)
tb_Fone = Entry(app)
tb_Fone.place(x=10, y=80, width=100, height=20)

Label(app, text="Email", background="#DDE", foreground="#009", anchor=W).place(x=10, y=110, width=100, height=20)
tb_Email = Entry(app)
tb_Email.place(x=10, y=130, width=300, height=20)

Label(app, text="OBS", background="#DDE", foreground="#009", anchor=W).place(x=10, y=160, width=100, height=20)
tb_Obs = Text(app)
tb_Obs.place(x=10, y=180, width=300, height=80)

Button(app, text="Gravar", command=GravarDados).place(x=10, y=270, width=100, height=20)

app.mainloop()