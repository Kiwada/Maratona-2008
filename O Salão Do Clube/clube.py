'''
Bacharelado em ciencia da computação Bloco 2 
05/07/2023
Kaio Felipe Castro Fontenele 
Arthur Dutra Costa Lima 

'''


arquivo = open("valores.txt","r")
lista = [] 
quant = 0  


for i in arquivo:
    i = i.strip() 
    quant+=1 
    lista.append(i) 


for i in range(0, quant,2):
    if lista[i]== '0':
        break
    lista[i] = [float(valor) for valor in lista[i].split()]
    lista[i+1] = [float(valor) for valor in lista[i+1].split()]
    dados = lista[i]
    comprimentos = lista[i+1]
    comprimentos = sorted(comprimentos) 
    A = dados[0]*dados[1]
    K = dados[-1]  
    L = dados[2]   
    L /=100
    soma = 0
    quantidade = 0
    i=1



    while i<=K:
        soma += comprimentos[-i] * L
        quantidade+=1
        if soma > A:
            soma-=comprimentos[-i] * L
            quantidade-=1
        i+=1
    if soma == A:
        print(quantidade)
    else:
        print("impossivel")
