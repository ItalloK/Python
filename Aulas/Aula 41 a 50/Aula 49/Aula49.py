import sqlite3
from sqlite3 import Error

############# Criar Conexão #############
def ConexaoBanco(): 
    caminho = "E:\\Programação\\Python\\Aulas\\Banco\\agenda.db"
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

vcon = ConexaoBanco()

nome = input("Digite um nome: ")
telefone = input("Digite um telefone: ")
email = input("Digite um Email: ")


vsql="INSERT INTO tb_contatos (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO) VALUES('"+nome+"','"+telefone+"','"+email+"')"

def Inserir(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Registro Inserido")
    except Error as ex:
        print(ex)

Inserir(vcon, vsql)

vcon.close()