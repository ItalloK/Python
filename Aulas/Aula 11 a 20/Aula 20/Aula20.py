def somar(n1, n2):
    r = n1+n2
    print("Soma de "+str(n1)+" + "+str(n2)+" = "+str(r))
somar(5,7)

print("")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("")

def textos(*txt): # qualquer quantidade de argumentos.
    for t in txt:
        print(t)
textos("Teste1","Teste2")

print("")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("")

def somar2(*num): # qualquer quantidade de argumentos.
    r = 0
    for n in num:
        r += n
    print("Soma: "+str(r))
somar2(10,20,30,40,50)

print("")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("")

def Carros(c="Golf"): # Se não for passado nada ele usa esse ' golf ' como padrão.
    print("Modelo: " + c)
Carros()

print("")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("")

Valores = [1,5,3,2]
def Somar3(num): # Passagem por Lista
    r = 0
    for x in num:
        r += x
    print("Soma da Lista: "+str(r))
Somar3(Valores)