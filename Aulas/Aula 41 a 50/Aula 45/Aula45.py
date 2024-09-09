import re

nomeArquivo = "teste.txt"
f = open("E:/Programação/Python/Aulas/Aula 41 a 50/Aula 45/"+nomeArquivo,"rt") #pode o T ou B vem depois do W 

#print(f.read()) # assim ele ler tudo do arquivo
#print(f.read(10)) # Ler apenas os 10 primeiros caracteres
#print(f.readline()) # Ler a linha

#for l in f:
#    print(l) # Ler todas as linhas

res = re.sub("/s", "-",f.readline())
f.close()


f = open("E:/Programação/Python/Aulas/Aula 41 a 50/Aula 45/"+nomeArquivo,"wt")
f.write(res)
f.close()


print(res)


print("Fim do Programa")