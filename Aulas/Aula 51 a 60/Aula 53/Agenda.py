import os
import sqlite3
from sqlite3 import Error

def ConexaoBanco(): ##Conexão
    caminho = "E:\\Programação\\Python\\Aulas\\Banco\\agenda.db"
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

vcon = ConexaoBanco() # Chama a conexão

def Query(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print("Operação realizada com Sucesso.")
        #conexao.close()

def Consultar(conexao, sql):
    c = conexao.cursor()
    c.execute(sql)
    res = c.fetchall()
    #conexao.close()
    return res


def MenuPrincipal():
    os.system('cls')
    print("1 - Inserir novo registro")
    print("2 - Deletar registro")
    print("3 - Atualizar registro")
    print("4 - Consultar registro por ID")
    print("5 - Consultar registro por Nome")
    print("6 - Sair")

def MenuInserir():
    os.system('cls')
    nome = input("Digite o Nome: ")
    telefone = input("Digite o Telefone: ")
    email = input("Digite o Email: ")
    vsql = "INSERT INTO tb_contatos (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO) VALUES ('"+nome+"','"+telefone+"','"+email+"')"
    Query(vcon, vsql)

def MenuDeletar():
    print("")

def MenuAtualizar():
    print("")

def MenuConsultarID():
    print("")

def MenuConsultarNomes():
    print("")



opcao = 0
while opcao != 6:
    MenuPrincipal()
    opcao = int(input("Digite uma opção: "))
    if opcao == 1:
        MenuInserir()
    elif opcao == 2:
        MenuDeletar()
    elif opcao == 3:
        MenuAtualizar()
    elif opcao == 4:
        MenuConsultarID()
    elif opcao == 5:
        MenuConsultarNomes()
    elif opcao == 6:
        os.system('cls')
        print("Programa Finalizado!")
    else:
        os.system('cls')
        print("Opcao inválida")
        os.system('pause')

os.system('pause')
    
