lista = [int(x) for x in input("Digite os números separados por espaço: ").split()]

for i in range(len(lista)):
    for j in range(0, len(lista) - i - 1):
        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]

print("Lista ordenada em ordem crescente:", lista)
