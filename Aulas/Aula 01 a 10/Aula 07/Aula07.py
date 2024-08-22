Nome = "Italo"
Sobrenome = "Gabriel"
"""res="Gabriel" in Nome # Verifica se 'Gabriel' está em 'Nome'
res2="Gabriel" not in Nome # O contrario de in
print(res)
print(res2)
palavra = "Gabriel"
res = palavra.upper() in Nome.upper() # Converte tudo para maisuculo para verificar se o nome existe.
print(res)
res = Nome+" "+Sobrenome # Concatenação
print(res)"""

Cidade = "São Luis"
Dia = 13
Mes = "Junho"
Ano = 2024
NomeCompleto = "Italo Gabriel"
Data="{}, {} de {} de {}\n\"{}\"" # Usando String Format ( tambem pode usar o caractere de escape \n ), tem as aspas tambem no caractere de escape

"""
    \'
    \"
    \n
    \r = retorno de alguma cosia
    \t = tabulação ( Tab )
    \b = backspace ( apaga o caractere anterior )
"""


print(Data.format(Cidade, Dia, Mes, Ano, NomeCompleto)) # Usando String Format
print(Cidade+", "+str(Dia)+" de "+Mes+" de "+str(Ano)) # Sem string format



