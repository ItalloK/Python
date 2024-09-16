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
    print("4 - Consultar registros")
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
    os.system('cls')
    id = int(input("Digite o ID do registro a ser Deletado: "))
    vsql = "DELETE FROM tb_usuarios WHERE N_IDCONTATO = "+id
    Query(vcon, vsql)


def MenuAtualizar():
    os.system('cls')
    id = int(input("Digite o ID do registro a ser Alterado: "))
    r = Consultar(vcon, "SELECT * FROM tb_contatos WHERE N_IDCONTATO = "+str(id))
    resNome = r[0][1]
    resTelefone = r[0][2]
    resEmail = r[0][3]
    nome = input("Digite o Nome: ")
    telefone = input("Digite o Telefone: ")
    email = input("Digite o Email: ")
    if len(nome) == 0:
        nome = resNome
    if len(telefone) == 0:
        telefone = resTelefone
    if len(email) == 0:
        email = resEmail
    vsql = "UPDATE tb_contatos SET T_NOMECONTATO = '"+nome+"', T_TELEFONECONTATO = '"+telefone+"', T_EMAILCONTATO = '"+email+"' WHERE N_IDCONTATO = "+str(id)
    Query(vcon, vsql)

def MenuConsultar():
    vsql = "SELECT * FROM tb_contatos"
    res = Consultar(vcon, vsql)
    vLimite = 10
    vCont = 0
    for r in res:
        print("ID: {0:_<3} Nome: {1:_<30} Telefone: {2:_<14} Email: {3:_<30}".format(r[0],r[1],r[2],r[3]))
        vCont+=1
        if(vCont >= vLimite):
            vCont = 0
            os.system("pause")
            os.system("cls")
    print("Fim da Lista")
    os.system("pause")


def MenuConsultarNomes():
    vnome = input("Digite o Nome: ")
    vsql = "SELECT * FROM tb_contatos WHERE T_NOMECONTATO LIKE '%"+vnome+"%'"
    res = Consultar(vcon, vsql)
    vLimite = 10
    vCont = 0
    for r in res:
        print("ID: {0:_<3} Nome: {1:_<30} Telefone: {2:_<14} Email: {3:_<30}".format(r[0],r[1],r[2],r[3]))
        vCont+=1
        if(vCont >= vLimite):
            vCont = 0
            os.system("pause")
            os.system("cls")
    print("Fim da Lista")
    os.system("pause")



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
        MenuConsultar()
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
    
