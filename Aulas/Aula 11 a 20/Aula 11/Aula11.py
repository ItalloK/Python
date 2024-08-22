a = 10
b = 5
res = 0
op = "+"

if op == "+":
    res = a+b
elif op == "-":
    res = a-b
elif op == "*":
    res = a*b
elif op == "/":
    res = a/b
else:
    print("Operador inválido")

print(str(res))


clima = "Sol"
dinheiro = 600
local = ""

if clima == "Sol" and (dinheiro >= 300 and dinheiro <= 500):
    lugar = "Clube"
else:
    lugar = "Cinema"

print("Vou ao " + lugar)