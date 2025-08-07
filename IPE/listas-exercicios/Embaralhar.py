def embaralhar():
    palavra = str(input("Digite a palavra: "))
    lista = []
    for i in palavra:
        lista.append(i) 
        
    lista.reverse(i)
    print(lista)
    
embaralhar()
