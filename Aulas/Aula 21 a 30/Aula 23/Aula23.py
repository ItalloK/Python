class Carro: # Declarando Classe
    velMax = 0
    ligado = False
    cor = ""

c1 = Carro() # Instanciou o Objeto
c2 = Carro()
c3 = Carro()

c1.velMax = 200
c1.cor = "Preto"
c1.ligado = False
Estado = "Sim" if c1.ligado else "Não"
print("Vel Max: "+str(c1.velMax)+" Cor: "+c1.cor+" Ligado: "+Estado) # Exibindo Dados do Objeto