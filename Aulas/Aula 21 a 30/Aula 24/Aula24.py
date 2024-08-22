class Carro: # Declarando Classe
    velMax = 0
    ligado = False
    cor = ""
    def __init__(self, v, l, c): # Metodo padrão( iniciado sempre que é instanciado ) -- Self == this
        self.velMax = v
        self.ligado = l
        self.cor = c
    def mostrar(self, nomeCar):
        Estado = "Sim" if self.ligado else "Não"
        print(nomeCar+" -> Vel Max: "+str(self.velMax)+" Cor: "+self.cor+" Ligado: "+Estado) # Exibindo Dados do Objeto
        print("-------------------------------------------------------------------")
    def ligar(self):
        self.ligado = True
    def desligar(self):
        self.ligado = False
    def andar(self):
        if (self.ligado):
            print("Andando")
        else:
            print("Carro Desligado")


c1 = Carro(200, False, "Preto") # Instanciou o Objeto
c2 = Carro(120, False, "Branco")
c3 = Carro(350, False, "Vermelho")

c1.ligar()
c1.mostrar("Carro 1")
c2.mostrar("Carro 2")
c3.mostrar("Carro 3")

c1.andar()
c2.andar()
