import json # Nescessario para trabalhar com Json


carros_json='{"Marca":"Honda","Modelo":"Hrv","Cor":"Prata"}'

carros = json.loads(carros_json)

print(carros["Marca"]) # pode ser editado igual é editado um Dictionary

for x in carros:
    print(x)

for x in carros.values():
    print(x)

for x in carros.items():
    print(x)

for k,v in carros.items():
    print(k+" -",v)

print("-----------------------------------------------")


carros2={
    "Marca":"Honda",
    "Modelo":"Hrv",
    "Cor":"Prata"
}

carros2_json = json.dumps(carros2) # converteu o dictionary carros2 em json


print(carros2_json)