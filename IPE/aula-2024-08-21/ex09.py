lista = ["manga", "palavra", "teste", "pneumonia"]
maior_palavra = ""
tamanho = 0

for palavra in lista:
    if len(palavra) > tamanho:
        maior_palavra = palavra
        tamanho = len(palavra)
    print(f"{palavra}: {len(palavra)} caracteres")

print(f"A maior palavra é {maior_palavra} que possui {tamanho} caracteres.")
