"""
Carros = ["HRV","Golf","Focus","Argo"] # Array normal
Carros[2] = "Fusion" # Array normal
print(Carros[1]) # Array normal
for x in Carros: # Array normal
    print(x)
"""
############ Matriz ############

Motos = [
    ["Modelo", "HRV"],  # Linha, Coluna
    ["Fabricante","Honda"],
    ["Ano",2016]
] # Matriz
print(Motos[0][0])
Motos[2][1] = 2019

Motos.append(["Cor","Prata"]) # Adiciona a lista de matriz

for l,c in Motos:
    print("Linha: "+str(l)+"|| Coluna: "+str(c))