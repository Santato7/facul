n = int(input("quantos numeros voce vai digitar: "))

for i in range(n):

    number = int(input("Numero: "))

    if number < 0:
        print("O numero é negativo")
    elif number > 0:
        print("O numero é positivo")
    else:
        print("O numero é zero")
