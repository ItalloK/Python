import random
import os

Erros = 0
Sorteado=random.randrange(0,100)

Jogador = int(input("Digite seu numero (0 a 100): "))
while (Jogador != Sorteado):
    os.system('cls')
    if(Sorteado > Jogador):
        print("Erro, o numero: "+str(Jogador)+", é maior do que o valor sorteado.")
    elif(Sorteado < Jogador):
        print("Erro, o numero: "+str(Jogador)+", é menor do que o valor sorteado.")
    Erros += 1
    Jogador = int(input("Digite seu numero(0 a 100): "))
print("Numero: "+str(Jogador)+" ,você acertou em: "+str(Erros)+" tentativar.")