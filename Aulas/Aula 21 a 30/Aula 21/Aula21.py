Valores = [1,5,3,2]
def Somar(num): # Passagem por Lista
    r = 0
    for x in num:
        r += x
    return r # Agora tem um Retorno
print("Somatorio de: "+str(Valores)+" é: "+str(Somar(Valores)))