numero = int(input("Digite um número: "))
if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")

if numero % 2 == 0:
    print("Número par.")
else:
    print("Número impar.")
