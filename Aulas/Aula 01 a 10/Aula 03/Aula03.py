num1=num2=res=0
#Nome = "Italo"


def cn():
    global Nome # Ao declarar como global deve ser iniciada depois e não na mesma linha
    Nome = "Italo" #iniciando a variavel global

cn()


print(Nome)
