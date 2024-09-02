import re

texto = "Curso de Python CFB Cursos"

res = re.split("\s", texto) # Onde ele contra o espaço ele divide a string ( e adiciona numa coleção ), \s é o msm q espaço

print(res)
print(res[2])

for t in res:
    print(t) # Imprime todos os elementos