palavra = input("Digite uma palavra: ")

soma = 0

for caractere in palavra:
    if caractere == "a" or caractere =="e" or caractere =="i" or caractere =="o" or caractere =="u":
        soma = soma + 1

print(soma)
