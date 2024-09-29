from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import Banco

def Popular():
    tv.delete(*tv.get_children())
    vquery = "SELECT * FROM tb_contatos order by N_IDCONTATO"
    linhas = Banco.Dql(vquery)
    for i in linhas:
        tv.insert("", "end", values=i)

def Inserir():
    if vnome.get() == "" or vfone == "":
        messagebox.showerror(title="ERRO", message="Digite todos os dados")
        return
    try:
        vquery = "INSERT INTO tb_contatos (T_NOMECONTATO, T_TELEFONECONTATO) VALUES ('"+vnome.get()+"', '"+vfone.get()+"')"
        Banco.Dml(vquery)
    except:
        messagebox.showerror(title="ERRO", message="Erro ao Inserir")
        return
    Popular()
    vnome.delete(0, END)
    vfone.delete(0, END)
    vnome.focus()

def Deletar():
    vid = -1
    itemSelecionado = tv.selection()[0]
    valores = tv.item(itemSelecionado, "values")
    vid = valores[0]
    try:
        vquery = "DELETE FROM tb_contatos WHERE N_IDCONTATO = "+vid
        Banco.Dml(vquery)
    except:
        messagebox.showerror(title="ERRO", message="Erro ao Deletar")
        return
    tv.delete(itemSelecionado)

def Pesquisar():
    tv.delete(*tv.get_children())
    vquery = "SELECT * FROM tb_contatos WHERE T_NOMECONTATO LIKE '%"+vnomepesquisar.get()+"%'"
    linhas = Banco.Dql(vquery)
    for i in linhas:
        tv.insert("", "end", values=i)

app = Tk()
app.title("Ohayo Pokko")
app.geometry("600x450")

###########################################################################################
quadroGrid = LabelFrame(app, text="Contatos")
quadroGrid.pack(fill="both", expand="yes", padx=10, pady=10)
tv = ttk.Treeview(quadroGrid, columns=('N_IDCONTATO', 'T_NOMECONTATO', 'T_TELEFONECONTATO'), show='headings')
tv.column('N_IDCONTATO', minwidth=0, width=50)
tv.column('T_NOMECONTATO', minwidth=0, width=250)
tv.column('T_TELEFONECONTATO', minwidth=0, width=100)
tv.heading('N_IDCONTATO', text="ID")
tv.heading('T_NOMECONTATO', text="NOME")
tv.heading('T_TELEFONECONTATO', text="TELEFONE")
tv.pack()
Popular()

###########################################################################################
quadroInserir = LabelFrame(app, text="Inserir novos contatos")
quadroInserir.pack(fill="both", expand="yes", padx=10, pady=10)
lbnome = Label(quadroInserir, text="Nome")
lbnome.pack(side="left")
vnome = Entry(quadroInserir)
vnome.pack(side="left", padx=10)
lbfone = Label(quadroInserir, text="Fone")
lbfone.pack(side="left")
vfone = Entry(quadroInserir)
vfone.pack(side="left", padx=10)
btn_Inserir = Button(quadroInserir, text="Inserir", command=Inserir)
btn_Inserir.pack(side="left", padx=10)

###########################################################################################
quadroPesquisar = LabelFrame(app, text="Pesquisar Contatos")
quadroPesquisar.pack(fill="both", expand="yes", padx=10, pady=10)

lbid=Label(quadroPesquisar, text="Nome")
lbid.pack(side="left")
vnomepesquisar = Entry(quadroPesquisar)
vnomepesquisar.pack(side="left", padx=10)
btn_pesquisar = Button(quadroPesquisar, text="Pesquisar", command=Pesquisar)
btn_pesquisar.pack(side="left", padx=10)
btn_todos = Button(quadroPesquisar, text="Mostrar Todos", command=Popular)
btn_todos.pack(side="left", padx=10)

app.mainloop()