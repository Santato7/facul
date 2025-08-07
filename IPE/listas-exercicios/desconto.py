valor = float(input("Digite o valor do produto: "))
desconto = float(input("Digite o valor do desconto: "))

x =  (desconto / 100) * valor
valor_final = valor - x


print(f"Valor final: {valor_final}")
