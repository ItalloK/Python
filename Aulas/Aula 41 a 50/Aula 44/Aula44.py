nomeArquivo = "teste.txt"
f = open("E:/Programação/Python/Aulas/Aula 41 a 50/Aula 44/"+nomeArquivo,"at") #pode o T ou B vem depois do W 

# r = read ( Leitura )
# a = append ( Anexar algo ao arquivo )
# w = write ( Escrita ) ----> Caso arquivo não exista, ele cria
# x = create ( Criar o arquivo )
# t = modo texto
# b = modo binario

txt=input("Digite um texto: ")
f.write(txt+"\n")

f.close() # Fecha o arquivo no final
print("Fim do Programa")