import Aula342 as Au # As serve para alterar o nome dentro deste arquivo # importa outro arquivo python

from Aula342 import jogador # importa apenas o ' jogador '
print("Nome: " + jogador["Nome"]) # usado com a linha de cima

Au.ohayo() # chama função de outro arquivo
print(Au.jogador["Nome"]) # imprime o nome do jogador do outro arquivo
