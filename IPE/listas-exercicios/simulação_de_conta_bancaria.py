def consultar(saldoBancario):
    return (f"Seu saldo atual é: R${saldoBancario:.2f}")
def sacar(qtdSacar, saldoBancario):
    if qtdSacar > saldoBancario:
        return (f"Seu saldo é R${saldoBancario:.2f}. Não foi possível sacar essa quantia!")
    else:
        saldoBancario -= qtdSacar
        return saldoBancario

saldo_bancario = 0
print("--------------------- CRIAÇÃO DE CONTA ---------------------")
name = input("Nome Completo: ")
saldo_inicial = int(input("Saldo Inicial: R$"))
saldo_bancario += saldo_inicial

while True:
    print(f"\nNome: {name}                Tipo de Conta: Corrente\n[0] - Depositar | [1] - Sacar | [2] - Saldo Atual | [3] - Sair")
    option = int(input("Opção: "))

    if option == 0:
        quantia_depositar = float(input("Valor que deseja depositar: R$"))
        saldo_bancario += quantia_depositar
    elif option == 1:
        quantia_sacar = float(input("Valor que deseja sacar: R$"))
        res = sacar(quantia_sacar, saldo_bancario)
        if type(res) is str:
            print(res)
        else:
            saldo_bancario = res
    elif option == 2:
        print(consultar(saldo_bancario))
    elif option == 3:
        break
    else:
        print("Opção não encontrada!")