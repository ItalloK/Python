import json

carros_dictionary={
    "Marca":"Honda",
    "Modelo":"HRV",
    "Cor":"Prata"
}
#Dictionary -> Objeto Json

jogador_j={
    "Nome":"Italo",
    "Time":"Aviadores",
    "Vivo":"True",
    "Energia":100,
    "Mochila":["Pederneira","Corda","Linha","Arame"],
    "Aeronaves":[
        {"Tipo" : "Transporte", "Habilidade" : 80},
        {"Tipo" : "Ataque", "Habilidade" : 100},
        {"Tipo" : "Reconhecimento", "Habilidade" : 50}
    ]
}

jogador=json.loads(jogador_j)

print(jogador)

"""
carros_list = ["Honda", "Volkswagen","Ford","Fiat","Chevrolet"]
#List -> Array Json

carros_tupla = ("Honda", "Volkswagen","Ford","Fiat","Chevrolet")
#Tupla -> Array Json

carros_j = json.dumps(carros_dictionary, indent=8, separators=(": ","="), sort_keys=True) # identa com espaço de 8, muda o : para =, muda a ordem das coisas 
print(carros_j)
"""