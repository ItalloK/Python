import mysql.connector 
from datetime import datetime

conn = mysql.connector.connect(
    host="localhost",      
    user="root",           
    password="root",       
    database="teste" 
)

def MostrarTodos():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")
    resultados = cursor.fetchall()
    for linha in resultados:
        print(linha)
    cursor.close()

def CadastrarPessoa():
    nome = input("Digite o nome da pessoa: ")
    data = input("Digite a data de nascimento (DD/MM/AAAA): ")
    dataAmericana = datetime.strptime(data, "%d/%m/%Y")
    telefone = input("Digite o telefone: ")
    email = input("Digite o email: ")
    try:
        query = conn.cursor()
        query.execute("INSERT INTO usuarios (nome, datadenascimento, telefone, email) VALUES (%s, %s, %s, %s)", 
                      (nome, dataAmericana, telefone, email))
        conn.commit()
        if query.rowcount > 0:
            print("Cadastro realizado com sucesso!")
        else:
            print("Nenhuma linha afetada. O cadastro pode não ter sido realizado.")
    except Exception as e:
        print(f"Ocorreu um erro ao tentar cadastrar a pessoa: {e}")
        conn.rollback()

def AtualizarPessoa():
    id = int(input("Digite o ID que deseja atualizar: "))
    nome = input("Digite o novo nome para esta pessoa: ")
    data = input("Digite a nova data de nascimento para essa pessoa (DD/MM/AAAA): ")
    dataAmericana = datetime.strptime(data, "%d/%m/%Y")
    telefone = input("Digite o novo telefone para esta pessoa: ")
    email = input("Digite um novo email para esta pessoa: ")
    try:
        query = conn.cursor()
        query.execute("""
            UPDATE usuarios 
            SET nome = %s, datadenascimento = %s, telefone = %s, email = %s 
            WHERE id = %s
            """, (nome, dataAmericana, telefone, email, id))
        conn.commit()
        if query.rowcount > 0:
            print("Atualizado com sucesso!")
        else:
            print("Nenhuma linha afetada. A atualizacao pode não ter sido realizada.")
    except Exception as e:
        print(f"Ocorreu um erro ao tentar atualizar a pessoa: {e}")
        conn.rollback()




def DeletarPessoa():
    id = int(input("Digite o ID que deseja deletar: "))
    try:
        query = conn.cursor()
        query.execute("DELETE FROM usuarios WHERE id = %s", (id,))
        conn.commit()
        if query.rowcount > 0:
            print("Deletado com sucesso!")
        else:
            print("Nenhuma linha afetada. Delete pode não ter sido concluido.")
    except Exception as e:
        print(f"Ocorreu um erro ao tentar atualizar a pessoa: {e}")
        conn.rollback()



print("1 - Para exibir todos.")
print("2 - Para cadastrar uma pessoa.")
print("3 - Para atualizar os dados de uma pessoa.")
print("4 - Para deletar uma pessoa.")
res = int(input("Digite um numero: "))

if(res == 1):
    MostrarTodos()
elif(res == 2):
    CadastrarPessoa()
elif(res == 3):
    AtualizarPessoa()
elif(res == 4):
    DeletarPessoa()
else:
    print("Encerrando Programa")








conn.close()
