import math

numero = int(input("Digite um número: "))

if numero >= 0:
    print(math.sqrt(numero))
else:
    print("Não é possível calcular a raiz quadrada de um número negativo.")
