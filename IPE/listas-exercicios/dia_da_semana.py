def dia_da_semana(numero):
    dias = {
        1: "Domingo",
        2: "Segunda-feira",
        3: "Terça-feira",
        4: "Quarta-feira",
        5: "Quinta-feira",
        6: "Sexta-feira",
        7: "Sábado"
    }
    
    return dias.get(numero, "Número inválido. Insira um número entre 1 e 7.")

numero = int(input("Digite um número (1-7): "))
print(dia_da_semana(numero))
