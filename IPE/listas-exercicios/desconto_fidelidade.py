def descontoFidelidade():
    fidelidade = int(input("Cliente Fidelidade?\n[1] - Sim | [0] - Não\n"))
    desconto = (15/100) if (fidelidade == 1) else 5/100

    return desconto
def descontoCupom():
    cupom = input("CUPOM: ")
    if cupom == "CUPOM10":
        desconto_adicional = 10/100
    elif cupom == "CUPOM20":
        desconto_adicional = 20/100
    else:
        desconto_adicional = 0
        print("Cupom inexistente!")
    
    return desconto_adicional

preco_original = float(input("Informe o preço original do produto: R$"))
fidelidade = descontoFidelidade()
cupom = descontoCupom()
preco_final = preco_original - (preco_original * fidelidade) - (preco_original * cupom)

print(f"\nCom o produto custando R${preco_original:.2f}\nCom os descontos aplicados custará R${preco_final:.2f}")