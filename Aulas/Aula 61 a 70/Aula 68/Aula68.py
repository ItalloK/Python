from tkinter import *
import os

pastaApp = os.path.dirname(__file__)


app = Tk()
app.title("Ohayo Pokko")
app.geometry("500x300")

img = PhotoImage(file=pastaApp+"\\rodinei.gif")
lb_img = Label(app, image=img)
lb_img.place(x=10, y=10)

app.mainloop()