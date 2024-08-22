"""
num = -10
if num < 1:
    raise Exception("Valor não permitido") #Gera uma exceção
"""

num = "Italo"
if not type(num) is int: # verifica o tipo de num.
    raise Exception ("Somento numeros são permitidos")
else:
    print(num)







"""
try:
    print(x)
except:
    print("Erro no programa")
else:
    print("Tudo certo")
finally:
    print("Fim do programa")
"""
