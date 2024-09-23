from tkinter import *
from tkinter import messagebox

def MostrarMsg(tipoMsg, msg):
    if tipoMsg == "1":
        messagebox.showinfo(title="INFO", message=msg)
    elif tipoMsg == "2":
        messagebox.showwarning(title="AVISO", message=msg)
    elif tipoMsg == "3":
        messagebox.showerror(title="ERRO", message=msg)
    elif tipoMsg >= "4" or tipoMsg < "1":
        msg = "Valor Incorreto"
        messagebox.showerror(title="ERRO", message=msg)
    
def ResetarTb():
    res = messagebox.askyesno("Resetar", "Confirmar reset do tb")
    #opcoes: askquestion ( SIM e NAO == True ou False )
    #opcoes: askokcancel ( OK e CANCELAR == True ou False )
    #opcoes: askretrycancel ( REPETIR e CANCELAR == True ou False )
    #opcoes: askyesnocancel ( SIM, NÃO E CANCELAR == True, False e None )
    if res == True:
        tb_num.delete(0, END)
        tb_num.insert(0, "1")

vMsg = "Ohayo Pokko"

app = Tk()
app.title("Ohayo Pokko")
app.geometry("500x300")

caixaTexto = StringVar()

Label(app, text="Tipo de Caixa (1,2 ou 3)").pack()
tb_num = Entry(app, textvariable=caixaTexto)
caixaTexto.set("1")
tb_num.pack()

btnMsg = Button(app, text="Mostrar Mensagem", command=lambda:MostrarMsg(caixaTexto.get(), vMsg))
btnMsg.pack()

btnReset = Button(app, text="Resetar TextBox", command=ResetarTb)
btnReset.pack()

app.mainloop()
