# Dictionary
Carro={
    "Fabricante":"Honda",
    "Modelo":"HRV", 
    "Ano":"2016", 
    "Cor":"Prata"
} # Sempre nescessario [Chave - Valor]

Carro["Estado"] = "Novo" # Adiciona ao Dicitionary ( Sempre adicionar Chave e Valor )

Carro.pop("Estado") # Remover do Dictionary
del Carro["Cor"] # Tambem Deleta do Dictionary

#Pode ser feito assim:
fab = Carro["Fabricante"]
print(fab)

#Pode ser feito assim tambem:
fab2 = Carro.get("Fabricante")
print(fab2)

Carro["Cor"] = "Preto" # Alterando a Cor
print(Carro.get("Cor"))

print(Carro["Fabricante"]) # Imprimindo por Chave

for x in Carro: # Assim imprime as Chaves
    print(x)

for x in Carro: # Assim imprime por Value
    print(Carro[x])

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

for c,v in Carro.items(): # Imprimindo Key e Value Juntos.
    print("Chave: "+c+" Valor: "+v)

if "Modelo" in Carro: # Procura por Chave dentro do Dictionary
    print("Sim, modelo é uma chave\n")

Carro.clear() # Limpa o Dictionary

print("Tamanho do Dictionary: " + str(len(Carro))) # Verifica o tamanho do dictionary ( cada conjunto é 1 )


Carros2 = {
    "Carro1":{
        "Fabricante":"Honda",
        "Modelo":"HRV"
    },
    "Carro2":{
        "Fabricante":"Volks",
        "Modelo":"Golf"
    },
    "Carro3":{
        "Fabricante":"Ford",
        "Modelo":"Focus"
    }
}

print(Carros2["Carro1"]["Fabricante"]) # Imprime Dictionary dentro do Dictionary

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")



Carro1={
    "Fabricante":"Honda",
    "Modelo":"HRV"
    }
Carro2={
    "Fabricante":"Volks",
    "Modelo":"Golf"
}
Carro3={
    "Fabricante":"Ford",
    "Modelo":"Focus"
}

TodosCarros={
    "C1":Carro1,
    "C2":Carro2,
    "C3":Carro3
}

print(TodosCarros["C1"]["Modelo"]) # ou só print(TodosCarros["C1"])