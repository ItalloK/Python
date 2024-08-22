import datetime

data=datetime.datetime.now() # pega a data completa -> 2024-07-04 02:28:48.172210

print(data.hour) # Imprime apenas a hora

print(str(data.day)+"/" +str(data.month)+ "/"+str(data.year))


dataNasc=datetime.datetime(1978,3,7)
print("Data nascimento: "+str(dataNasc))

print(dataNasc.strftime("%A")) # assim imprime o dia da semana completo ( str )
print(dataNasc.strftime("%a")) # assim imprime o dia da semana resumido ( str )
print(dataNasc.strftime("%w")) # assim imprime o numero do dia da semana ( int )
print(dataNasc.strftime("%d")) # assim imprime o dia do mês ( int )
print(dataNasc.strftime("%b")) # assim imprime o mes abreviado ( str )
print(dataNasc.strftime("%B")) # assim imprime o mes completo ( str )
print(dataNasc.strftime("%m")) # assim imprime o numero do mes ( int )
print(dataNasc.strftime("%y")) # assim imprime o ano com 2 digitos ( int )
print(dataNasc.strftime("%Y")) # assim imprime o ano com 4 digitos ( int )

print(dataNasc.strftime("%H")) # assim imprime a hora com 2 ( 0 a 23 horas ) digitos ( int )
print(dataNasc.strftime("%I")) # assim imprime a hora com 2 ( 0 a 12 horas ) digitos ( int )
print(dataNasc.strftime("%p")) # assim imprime AM ou PM ( str )
print(dataNasc.strftime("%M")) # assim imprime minutos ( int )
print(dataNasc.strftime("%S")) # assim imprime segundos ( int )
print(dataNasc.strftime("%F")) # assim imprime microsegundos ( int )
print(dataNasc.strftime("%j")) # assim imprime o dia do ano ( 001 ate 366 ) ( int )
print(dataNasc.strftime("%W")) # assim imprime o numero da semana do ano ( int )