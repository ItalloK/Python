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
#Inserir()

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
#Deletar(vcon, vsql)

def Atualizar(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print("Atualizado com Sucesso")
vsql="UPDATE tb_contatos SET T_NOMECONTATO = 'Italluzinho', T_TELEFONECONTATO = '98999999999', T_EMAILCONTATO = 'Italo@ceuma.com.br' WHERE N_IDCONTATO = 1"
#Atualizar(vcon, vsql)


def Consultar(conexao, sql):
    c = conexao.cursor()
    c.execute(sql)
    resultado = c.fetchall()
    return resultado
vsql="SELECT * FROM tb_contatos"
res = Consultar(vcon, vsql)

for r in res:
    print(r)


vcon.close()