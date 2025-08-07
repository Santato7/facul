peso = float(input("Informe o seu peso em kg: "))
altura = float(input("Informe a sua altura em metros: "))

imc = peso / (altura ** 2)

print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif 18.5 <= imc <= 24.9:
    classificacao = "Peso normal"
elif 25.0 <= imc <= 29.9:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obesidade"

print(f"Sua classificação é: {classificacao}")

if 18.5 <= imc <= 24.9:
    print("Seu IMC está na faixa normal.")
else:
    print("Seu IMC não está na faixa normal.")
