n = int(input("Digite o número de itens: "))
itens = []
for i in range(n):
    nome_item = input(f"Digite o nome do {i + 1}° item: ")
    peso_item = int(input(f"Digite o peso do {i + 1}° item: "))
    valor_item = int(input(f"Digite o valor do {i + 1}° item: "))
    itens.append({"nome": nome_item, "peso": peso_item, "valor": valor_item})

max_kg = int(input("Digite o peso máximo da mochila: "))


def gerar_combinacoes(lista):
    resultados = [[]]

    for item in lista:
        novas_combinacoes = []
        for combinacao in resultados:
            novas_combinacoes.append(combinacao + [item])
        resultados.extend(novas_combinacoes)

    resultados.remove([])

    return resultados


combinacoes = gerar_combinacoes(itens)

comb_remover = []

for i in combinacoes:
    peso_total_combinacao = 0
    for j in i:
        peso_total_combinacao = peso_total_combinacao + j["peso"]
    if peso_total_combinacao > max_kg:
        comb_remover.append(i)

for i in comb_remover:
    combinacoes.remove(i)


def encontrar_maior_valor(_combinacoes):
    maior_combinacao = None
    maior_valor_total = 0

    for combinacao in _combinacoes:
        valor_total = 0
        for item in combinacao:
            valor_total = valor_total + item["valor"]

        if valor_total > maior_valor_total:
            maior_valor_total = valor_total
            maior_combinacao = combinacao

    return maior_combinacao, maior_valor_total


maior_combinacao, maior_valor_total = encontrar_maior_valor(combinacoes)

print("Combinação com o maior valor total:", maior_combinacao)
print("Valor total:", maior_valor_total)
