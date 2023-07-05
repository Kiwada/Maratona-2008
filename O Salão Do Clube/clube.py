'''
M = Largura
N = Comprimento

L = Largura da Tabua

K = número de tabuas doadas = [] lista que vai variar de acordo com a quantidade de tabuas


'''


arquivo = open("valores.txt","r")
lista = []
for i in arquivo:
    
    i = i.strip()
    
    lista.append(i)


lista[0] = [float(valor) for valor in lista[0].split()]
lista[1] = [float(valor) for valor in lista[1].split()]

dados = lista[0]

comprimentos = lista[1]

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
