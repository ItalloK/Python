import json

with open('E:/Programação/Python/Aulas/Aula 31 a 40/Aula 39/jogador.json') as f:
    jogador=json.load(f)


def linha():
    print("-------------------------------------------------------------------------------")

#Imprime as Chaves
for c in jogador:
    print(c)
linha()

#Imprime Itens
for i in jogador.items():
    print(i)
linha()

#Imprime Valores
for v in jogador.values():
    print(v)
linha()