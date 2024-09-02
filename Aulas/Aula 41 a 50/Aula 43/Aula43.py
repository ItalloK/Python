import re

texto = "Curso de Python CFB Cursos"

res = re.sub(" ", "-", texto) # Substitui o 'Espaço' por ' - '

print(res)
