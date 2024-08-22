l_Carros = ["HRV","Golf","Argo"] # Lista

t_Carros = ("HRV","Golf","Argo") # Tupla

#Diferença de tupla pra lista -> 
#l_Carros[2] = "Focus" # na tupla não é possivel alteração

l_Carros = list(t_Carros) # Cria uma lista carros q recebe os valores da tupla convertido para lista
l_Carros[2] = "Focus"
t_Carros = tuple(l_Carros) # Converte a lista para tupla dnv

for x in t_Carros:
    print(x)