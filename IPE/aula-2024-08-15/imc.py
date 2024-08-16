weight = float(input("Digite seu peso: "))
height = float(input("Digite sua altura: "))

imc = weight / height**2

if imc < 18.5:
    print(f"Seu IMC é {imc:.2f} e está abaixo da faixa normal.")
elif imc > 24.9:
    print(f"Seu IMC é {imc:.2f} e está acima da faixa normal.")
else:
    print(f"Seu IMC é {imc:.2f} e está dentro da faixa normal.")
