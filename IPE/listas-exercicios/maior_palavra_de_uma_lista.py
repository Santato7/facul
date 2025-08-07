listaPalavras = ["apple", "banana", "cherry", "abacaxi"]
maiorPalavra = "Nao sei"
tamanhoMaiorPalavra = 0

for palavra in listaPalavras:
  tamanho = 0
  for letra in palavra:
    tamanho = tamanho + 1
  if (tamanho > tamanhoMaiorPalavra):
    maiorPalavra = palavra
    tamanhoMaiorPalavra = tamanho
  print("Palavra: " + palavra)
  print("Tamanho: " + str(tamanho))
  print("Maior Palavra: " + maiorPalavra)
  print("--------------------------") 

print("A maior palavra é: " + maiorPalavra + " com tamanho = "+ str(tamanhoMaiorPalavra))
