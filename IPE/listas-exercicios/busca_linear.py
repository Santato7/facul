lista = [10, 23, 45, 70, 11, 15]

elemento = int(input("Informe o elemento que deseja procurar: "))

encontrado = False

for i in range(len(lista)):
    if lista[i] == elemento:
        print(f"Elemento {elemento} encontrado no índice {i}.")
        encontrado = True
        break  

if not encontrado:
    print(f"Elemento {elemento} não encontrado na lista.")
