"""
2.Faça um programa que preencha por leitura um vetor de 10 posições, 
e conta quantos valores diferentes existem no vetor.
"""
tam = 10
j = 0
cont = 0
vet = [0] * 10
dif = 0

for i in range(len(vet)): #Adquirir valor do vetor
    vet[i] = int(input(f"Digite o valor {i + 1} do vetor:\n"))
while (j != len(vet)): #Criar uma posição J do vetor
    cont = 0
    for i in range(len(vet)): #Comparar essa posicao J com todos os termos vetor
        if(vet[j] != vet[i]): #Se ele for diferente, adicionar 1 ao contador
            cont += 1
    if(cont == (tam - 1)): #Se o contador for igual ao tamanho - 1 (diferente de todos menos ele mesmo), adicionar 1 no contador de diferente
        dif += 1
    j += 1
print(dif) #Imprimir quantos termos diferentes foram encontrados