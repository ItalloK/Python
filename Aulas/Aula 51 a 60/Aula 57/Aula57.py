from tkinter import *

app = Tk()
app.title("Ohayo Pokko") # Titulo
app.geometry("500x300")
app.configure(background="#008")

txt1 = Label(app, text="Curso de Python", background="#FF0", foreground="#000")
txt1.place(x=10, y=10, width=100, height=20)

vtxt = "Tkinter"
vbg = "#FF0"
vfg = "#000"

txt2 = Label(app, text=vtxt, bg=vbg, fg=vfg)
txt2.pack(ipadx=20, ipady=20, padx=5, pady=5, side="top", fill=X, expand=True)

app.mainloop()