carros=["HRV","Polo","Jetta","Cruise","Fusion"]

itCarros=iter(carros) # Iterator

#print(next(itCarros)) # Usando Iterator ( Imprime e passa pro proximo )
#print(next(itCarros)) 
#print(next(itCarros)) 
#print(next(itCarros)) 
#print(next(itCarros)) 
#print(next(itCarros)) # se usar mais doq precisa, gera excessão

"""
i=0
while i<5: # Usando While
    print(carros[i])
    i+=1
"""

while itCarros:
    try:
        print(next(itCarros))
    except StopIteration:
        print("Fim da Lista")
        break