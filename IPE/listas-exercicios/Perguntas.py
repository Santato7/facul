lista = ["Telefonou para a vítima?","Esteve no local do crime?","Mora perto da vítima?","Devia para a vítima?","Já trabalhou com a vítima?"]

soma = 0
for pergunta in lista:
    resposta = input(f"{pergunta} (sim/não): ").strip().lower()
    
    if resposta == "sim":
        soma = soma + 1
    elif resposta == "não":
        continue
    else:
        print("Responda com 'sim' ou 'não'.")
        
if soma == 2:
    classificaçao = "suspeita"
elif soma == 3 or soma == 4:
    classificaçao = "Cúmplice"
elif soma == 5:
    classificaçao = "ASSASINO"
else:
    classificaçao = "inocente"
    
print(f"vôce é {classificaçao} de um crime")
    
        
        
    