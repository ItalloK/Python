import random

num_i = 10
num_f = 5.2
num_c = 1j

num_r=random.randrange(0,59) # Gera apenas um valor
print(num_r)

numr=[
    random.randrange(0,59),
    random.randrange(0,59),
    random.randrange(0,59),
    random.randrange(0,59),
    random.randrange(0,59),
    random.randrange(0,59),
] # Gera 6 valores aleatorios e salva no array
print("Valor 1: " + str(numr[0]))
print("Valor 2: " + str(numr[1]))
print("Valor 3: " + str(numr[2]))
print("Valor 4: " + str(numr[3]))
print("Valor 5: " + str(numr[4]))
print("Valor 6: " + str(numr[5]))



#x=int(num_f) # Operação de Cast, transforma float em int
x=num_f
print("Valor variavel: " + str(x) + " - Tipo: " + str(type(x))) # 1º ele transformou o inteiro para string, 2º transformou tipo para string
