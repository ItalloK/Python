#x = 1 # int
#x = "Italo" # string
#x = 15.6 #float
#x = False #bool
#n1 = 5; n2 = 2; x = complex(n1,n2) # pode usar para numero complexo tambem complex(1j)

#print(x.real) #Numero Real
#print(x.imag) #Numero Imaginario
#print("Res: " + str(x))
#print("Valor de X: " + str(x))
#print("Tipo: " + str(type(x))) # retorna o tipo do objeto

#x=["Carro","Avião","Navio"] #List ou Array
#x[0] = "Onibus" # setando valores para List/Array
#print(x[0]) # imprime o indice 0 do list/array


#x["Arroz", 1, 2.5, True] # Tambem pode ser feito assim
#x[0] = "Feijão" # Isso não funciona com Tupla

#x("Carro", 1.5, 5, True) #Tupla

#x = range(0, 100, 1) #criou um list de 0 a 100 ( 1º Numero inicial, 2º Numero final, 3º De quantos em quantos numeros deve ser colocado)
#print("Valor: " + str(x[55])) # Para imprimir isso acima

"""
x={
    "Nome":"Italo",
    "Link":"Github",
    "Link2":"Instagram"
} # Dictionary ( Chave / Valor )
# x.keys ou x.values ( Dictionary )
#print(x["Nome"]) # Indice a chave e ele exibe o valor"""

x={5,5,4,2,9,9,4,3} # Tipo Set
print(str(x)) # Não repete valores 


x=frozenset({5,5,4,2,9,9,4,3}) # Tipo frozenset ( não pode ser alterado os valores )
