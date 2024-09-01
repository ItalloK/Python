import re # RegEx

texto = "Curso de Python CFB Cursos"

res = re.findall("so", texto) # Procura oq tiver de so dentro de 'texto'

print(res)

print("----------------------------------------------------------------")

pesq = input("Pesquisar: ")
res = re.findall(pesq, texto)
print(res)
qtde = len(res) # Conta quantidade de resultados
print("Quantidade de elementos:" + str(qtde))

print("----------------------------------------------------------------")

for t in res:
    print(t)
