Carros = ["HRV","Golf","Argo","Focus"]

#print(Carros[-1]) #imprime da direita pra esquerda, começa de -1

Carros.append("Fit")
Carros.append("Fusion")
Carros.append("Polo") # Append adiciona itens a lista
print(str(len(Carros))) # len - Conta quantidade de itens
print(Carros) # Imprime a Lista

Carros.remove("Fusion") # Remove um item da Lista ( caso tente remover algo que não tem ele da erro )
Carros.pop() # Remove o ultimo elemento da Lista
del Carros[2] # Remove por Indice
#Carros.clear() # Limpa todos os elementos da Lista
#Carros2=list(Carros) # Copia lista Carros para Carros2

Carros2 = ["Fusca", "147", "Brasilia", "Celta"]
Carros3 = Carros+Carros2 # Une as 2 listas

print("Carros 3: " + str(Carros3)) # Imprime a Lista
