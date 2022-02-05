"""
7. Dado um vetor de 100 elementos, determine o maior e o menor elemento do vetor. (Não utilize as funções min() e max() )
"""

vet = []
tam = 100

for i in range(tam):
    vet.append(int(input()))
j = 0
max = vet[j]
while(j != len(vet)):
    if(vet[j] > max): #Verificar se vet[j] é maior que o antigo maior numero
        max = vet[j]
    cont = 0
    for i in range(len(vet)): #Verificar se vet[j] é menor que todas as posições do vetor VET
        if(vet[j] < vet[i]):
            cont += 1
    if(cont == len(vet) - 1):
        min = vet[j]
    j += 1
print(f"Maior {max} e Menor {min}")