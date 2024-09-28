from tkinter import *
from tkinter import ttk

app = Tk()
app.title("ohayo pokko")
app.geometry("500x300")

nb=ttk.Notebook(app)
nb.place(x=0, y=0, width=500, height=300)

tb1=Frame(nb)
tb2=Frame(nb)

nb.add(tb1, text="Nomes")
nb.add(tb2, text="Animais")

lb1=Label(tb1, text="Italo")
lb1.pack()

lb2=Label(tb1, text="Gabriel")
lb2.pack()


lb3=Label(tb2, text="Cavalo")
lb3.pack()


app.mainloop()