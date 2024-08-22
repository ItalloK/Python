Soma = lambda a,b: a+b # Função Lambda / Anonima
print(Soma(2,5)) # Exibindo
Mult=lambda a,b,c: (a+b)*c # Lambda Complexa
print(Mult(2,5,3))
print("")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("")

print((lambda a,b: a+b)(3,2)) # Assim tambem executa a função
print("")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("")


r = lambda x, func: x+func(x) # Passando valor e Funcao ( X + Funcao( Entrada: Valor de X ))
res = r(2, lambda x: x*x)
print(res) # Valor: 6 = 2 + Func ( 2 x 2 )