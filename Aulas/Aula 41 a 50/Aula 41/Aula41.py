import re

texto = "Curso de Python CFB Cursos"

res = re.search("Python", texto) #Retorna posicao da primeira ocorrencia
if(res != None):
    pi = res.start()
    pf = res.end()
    tam = pf-pi
    print("Tamanho da palavra: "+ str(tam))
    print(res.end()) #.start() pega o indice da primeira letra, #.end() pega o indice da ultima letra
else:
    print("Não Encontrado")

