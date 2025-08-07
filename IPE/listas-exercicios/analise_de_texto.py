frase = input("Digite a frase a ser analisada:").lower()
listaPalavras = frase.split()
print(listaPalavras)
print("O total de palavras é:", len(listaPalavras))

totalLetras = 0
for palavra in listaPalavras:
  totalLetras += len(palavra)
print("Total de letras:", totalLetras)

vogais = "aeiou"
totalVogais = 0
for palavra in listaPalavras:
  for letra in palavra:
    if letra in vogais:
      totalVogais += 1
print("Total de vogais", totalVogais)
print("Porcentagem de vogais: ", str(totalVogais/totalLetras * 100))