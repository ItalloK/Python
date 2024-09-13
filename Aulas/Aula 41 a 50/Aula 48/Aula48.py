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

###########################################################################################
vsql="""CREATE TABLE tb_contatos (
            N_IDCONTATO INTEGER PRIMARY KEY AUTOINCREMENT,
            T_NOMECONTATO VARCHAR(30),
            T_TELEFONECONTATO VARCHAR(14),
            T_EMAILCONTATO VARCHAR(30)
        );"""
###########################################################################################

def CriarTabela(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        print("Tabela Criada")
    except Error as ex:
        print(ex)

CriarTabela(vcon, vsql)


vcon.close()