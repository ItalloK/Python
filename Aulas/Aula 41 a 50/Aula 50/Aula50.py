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

def Inserir(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Registro Inserido")
    except Error as ex:
        print(ex)

def Deletar(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print("Deletado com Sucesso")

vsql="DELETE FROM tb_contatos WHERE N_IDCONTATO = 2"
Deletar(vcon, vsql)

"""nome = input("Digite um nome: ")
telefone = input("Digite um telefone: ")
email = input("Digite um Email: ")"""



vcon.close()