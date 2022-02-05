"""
9. Dado um vetor com 20 elementos, gerar outro vetor que contenha somente números múltiplos de 3 encontrados no primeiro vetor.
"""

tam = 5
vet = []
vetmult3 = []

for i in range(tam):
    vet.append(int(input()))
    if(vet[i] % 3 == 0):
        vetmult3.append(vet[i])
print(sorted(vetmult3))