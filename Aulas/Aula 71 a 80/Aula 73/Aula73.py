from tkinter import *

app = Tk()
app.title("Ohayo Pokko")
app.geometry("500x300")

lb_Esportes = LabelFrame(app, text="Esportes", borderwidth=1, relief=SOLID)
lb_Esportes.place(x=10, y=10, width=300, height=100)

le1 = Label(lb_Esportes, text="Futebol")
le1.pack()

le2 = Label(lb_Esportes, text="Volei")
le2.pack()

le3 = Label(lb_Esportes, text="Basquete")
le3.pack()

app.mainloop()