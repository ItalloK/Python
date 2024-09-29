from tkinter import *
from tkinter import ttk


app = Tk()
app.title("Ohayo Pokko")
app.geometry("500x300")

listaNomes = [['0','Italo', '9898'], ['1','Gabriel', '9999'], ['2','Ana', '1010']]

tv = ttk.Treeview(app, columns=('Id', 'Nome', 'Fone'), show='headings')
tv.column('Id', minwidth=0, width=50)
tv.column('Nome', minwidth=0, width=250)
tv.column('Fone', minwidth=0, width=100)

tv.heading('Id', text="ID")
tv.heading('Nome', text="Nome")
tv.heading('Fone', text="Telefone")

tv.pack()

for (i, n, f) in listaNomes:
    tv.insert("", "end", values=(i, n, f))


app.mainloop()