class NPC: # Classe Base / Pai / Super-Classe
    def __init__(self, nome, time, forca, municao): # Classe construtora
        self.nome = nome
        self.time = time
        self.forca = forca
        self.municao = municao
        self.vivo = True
        self.energia = 100
    def info(self):
        print("Nome: "+ self.nome)
        print("Time: "+ str(self.time))
        print("Força: "+str(self.forca))
        print("Munição: "+ str(self.municao))
        print("Vivo: " + "Sim" if self.vivo else "Não")
        print("Energia: "+ str(self.energia))
        print("-----------------------------------------------")

class Soldado(NPC):# Entre parenteses de onde ele herda
    def __init__(self, nome, time):
        self.forca = 200
        self.municao = 200
        super().__init__(nome,time,self.forca, self.municao) # Super serve para invocar um metodo da classe pai

class Guarda(NPC):
    def __init__(self, nome, time):
        self.forca = 100
        self.municao = 20
        super().__init__(nome,time,self.forca, self.municao) # passando parametros para init de NPC    

class Elite(NPC):
    def __init__(self, nome, time):
        self.forca = 400
        self.municao = 500
        super().__init__(nome,time,self.forca, self.municao) # passando parametros para init de NPC    
    def inf(self):
        super().info()


s1 = Guarda("Olho Vivo", 1)
s2 = Soldado("Bala na Agulha",1)
s3 = Elite("Ninja", 1)

s4 = Guarda("Super Atento", 2)
s5 = Soldado("Tiro Certo", 2)
s6 = Elite("Samurai", 2)

s1.vivo = False
s6.vivo = False

s1.info()
s2.info()
s3.info()
s4.info()
s5.info()
s6.inf()