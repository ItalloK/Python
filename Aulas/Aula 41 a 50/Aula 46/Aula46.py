import re
import os


nomeArquivo = "teste.txt"
caminho = "E:/Programação/Python/Aulas/Aula 41 a 50/Aula 46/"

if os.path.exists(caminho+nomeArquivo):
    print("Arquivo existente") 
else:
    f = open(caminho+nomeArquivo,"x")
    f.close()
    print("Arquivo Criado")

if os.path.exists(caminho+nomeArquivo):
    os.remove(caminho+nomeArquivo)
    print("Arquivo Removido")
else:
    print("Arquivo Inexistente")