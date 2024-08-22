import os
carros=[]

class Carro:
    nome=""
    pot=0
    velMax=0
    ligado=False
    def __init__(self, nome, pot):
        self.nome = nome
        self.pot = pot
        self.velMax = int(pot)*2
        self.ligado = False

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def info(self):
        print("Nome......: "+self.nome)
        print("Potencia..: "+str(self.pot))
        print("Vel Maxima: "+str(self.velMax))
        print("Ligado....: "+ "Sim" if self.ligado==True else "Não")


def Menu():
    os.system("cls") or None
    print("1 - Novo Carro")
    print("2 - Informações do Carro")
    print("3 - Excluir do Carro")
    print("4 - Ligar Carro")
    print("5 - Desligar Carro")
    print("6 - Listar Carros")
    print("7 - Sair do Programa")
    print("Quantidade de carros: "+str(len(carros)))
    opc=int(input("Digite uma opcao: "))
    return opc

def NovoCarro():
    os.system("cls") or None
    n=input("Digite o nome do carro....: ")
    p=input("Digite a potencia do carro: ")
    car = Carro(n,p)
    carros.append(car)
    print("Novo Carro Criado")
    os.system("pause")

def Informacoes():
    os.system("cls") or None
    n=input("Digite o numero do carro que deseja ver as informações: ")
    try:
        carros[int(n)].info()
    except:
        print("Carro não existe na lista")
    os.system("pause")

def ExcluirCarro():
    os.system("cls") or None
    n=input("Digite o numero do carro que deseja excluir: ")
    try:
        del carros[int(n)]
    except:
        print("Carro não existe na lista")
    os.system("pause")

def LigarCarro():
    os.system("cls") or None
    n=input("Digite o numero do carro que deseja Ligar: ")
    try:
        carros[int(n)].ligar()
        print("Carro Ligado")
    except:
        print("Carro não existe na lista")
    os.system("pause")

def DesligarCarro():
    os.system("cls") or None
    n=input("Digite o numero do carro que deseja Desligar: ")
    try:
        carros[int(n)].desligar()
        print("Carro Desligado")
    except:
        print("Carro não existe na lista")
    os.system("pause")

def ListarCarros():
    os.system("cls") or None
    p=0
    for c in carros:
        print(str(p) + " - " + c.nome)
        p=p+1
    os.system("pause")