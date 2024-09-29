from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os

def Mp(mm):
    return mm / 0.352777

pastaApp = os.path.dirname(__file__)

def CriarPDF():
    try:
        cnv = canvas.Canvas(pastaApp+"\\Aula83.pdf", pagesize = A4)
        cnv.drawImage(pastaApp+"\\rodinei.gif", x=Mp(0), y=Mp(200))
        cnv.circle(Mp(100), Mp(100), Mp(25))
        cnv.drawString(Mp(100),Mp(100), "Ohayo Pokko")
        cnv.save()
    except:
        messagebox.showerror(title="ERRO", message="Erro ao criar arquivo PDF")
        return
    messagebox.showinfo(title="PDF", message="PDF Criado")


app = Tk()
app.title("Ohayo Pokko")
app.geometry("600x450")


btn_CriarPdf = Button(app, text="Criar PDF", command=CriarPDF)
btn_CriarPdf.pack(side=LEFT, padx=10)

app.mainloop()