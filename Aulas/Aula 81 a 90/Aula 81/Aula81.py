from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def Inserir():
    if id.get() == "" or nome.get() == "" or fone.get() == "":
        messagebox.showerror(title="ERRO", message="Digite todos os dados")
        return
    tv.insert("", "end", values=(id.get(), nome.get(), fone.get()))
    id.delete(0, END)
    nome.delete(0, END)
    fone.delete(0, END)
    id.focus()

def Deletar():
    try:
        itemSelecionado = tv.selection()[0]
        tv.delete(itemSelecionado)
    except:
        messagebox.showerror(title="ERRO", message="Selecione um elemente a ser deletado.")

def Obter():
    try:
        itemSelecionado = tv.selection()[0]
        valores = tv.item(itemSelecionado, option="values")
        print(f'ID: {valores[0]}')
        print(f'Nome: {valores[1]}')
        print(f'Telefone: {valores[2]}')
    except:
        messagebox.showerror(title="ERRO", message="Selecione um elemente a ser obtido.")

app = Tk()
app.title("Ohayo Pokko")
app.geometry("410x310")

lbId = Label(app, text="ID")#, anchor=W)
id = Entry(app)
lbNome = Label(app, text="Nome")#, anchor=W)
nome = Entry(app)
lbFone = Label(app, text="Telefone")#, anchor=W)
fone = Entry(app)


tv = ttk.Treeview(app, columns=('Id', 'Nome', 'Fone'), show='headings')
tv.column('Id', minwidth=0, width=50)
tv.column('Nome', minwidth=0, width=250)
tv.column('Fone', minwidth=0, width=100)

tv.heading('Id', text="ID")
tv.heading('Nome', text="Nome")
tv.heading('Fone', text="Telefone")

btn_Inserir = Button(app, text="Inserir", command=Inserir)
btn_Deletar = Button(app, text="Deletar", command=Deletar)
btn_Obter = Button(app, text="Obter", command=Obter)

lbId.grid(column=0, row=0, sticky=W)
id.grid(column=0, row=1)
lbNome.grid(column=1, row=0, sticky=W)
nome.grid(column=1, row=1)
lbFone.grid(column=2, row=0, sticky=W)
fone.grid(column=2, row=1)

tv.grid(column=0, row=3, columnspan=3, pady=5)

btn_Inserir.grid(column=0, row=4)
btn_Deletar.grid(column=1, row=4)
btn_Obter.grid(column=2, row=4)

#tv.insert("", "end", values=(i, n, f))


app.mainloop()