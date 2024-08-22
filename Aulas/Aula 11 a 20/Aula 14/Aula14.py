i = 0
carros = ["Hrv","Golf","Argo","Onix","Focus"]
tam = len(carros)

while i < tam:
    print(carros[i])
    i+=1
print("\nFim do Loop 1")
i = 0
while i < 10:
    print(i)
    i+=1
    if(i>=5):
        break
print("\nFim do Loop 2")

i = 0
motos  = []
moto = input("Digite um nome de uma Moto: ")
while moto != "-1":
    motos.append(moto)
    moto = input("Digite um nome de uma Moto: ")

for x in motos:
    print(x)